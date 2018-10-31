# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest, Http404,JsonResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,user_passes_test
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.db.models import Avg, Max, Min
from .models import *
from staffregistration.models import *
import json
import datetime
import os
import unicodedata
from django.core.mail import send_mail, EmailMultiAlternatives, get_connection
import smtplib
from django.db.models import Q
import xlrd
import xlwt
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
import urllib2, operator, copy, csv

def calculate_age(dob):
    born = datetime.datetime.strptime(dob, "%Y-%m-%d")
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

# Create your views here.
def index(request):
	response = {}
	profile = StaffProfile.objects.get(user=request.user)
	response['profile'] = profile
	app = StaffApp.objects.get(user=request.user)
	if app.paymentUploaded == False:
		return redirect('/staffregister/paymentDetails')
	if StaffUser.objects.filter(app_id=app).exists() :
		response['generalData']=StaffUser.objects.get(app_id=app)
		response['corresAddr']=StaffUser.objects.get(app_id=app).correspond_addr
		response['permAddr']=StaffUser.objects.get(app_id=app).permanent_addr
	if request.method == "POST" :

		if request.POST.get('nextBtn'):
			return redirect('/staffrecruit/uploadpic/')

		if request.POST.get('savebutton'):

			if StaffUser.objects.filter(app_id=app).exists() :
				staff=StaffUser.objects.get(app_id=app)

			else :
				staff=StaffUser()
				staff.app_id = app
				permanent_addr = Address()
				permanent_addr.save()
				correspond_addr = Address()
				correspond_addr.save()
				staff.permanent_addr = permanent_addr
				staff.correspond_addr = correspond_addr

			#staff.app_id=app
			staff.full_name = request.POST['Name']
			staff.gender = request.POST.get('gender', 'Male')
			staff.father_name = request.POST['fatherName']
			staff.father_occ = request.POST.get('fatherOccupation')
			staff.mother_name = request.POST['motherName']
			staff.mother_occ = request.POST.get('motherOccupation')
			staff.nation = request.POST['nationality']
			staff.pob = request.POST['birthplace']
			staff.dob = request.POST['dateOfBirth']
			staff.age = calculate_age(staff.dob)
			staff.maritalstatus=request.POST['maritalstatus']

			staff.correspond_addr.addr1 = request.POST['corresAddr1']
			staff.correspond_addr.addr2 = request.POST.get('corresAddr2','')
			staff.correspond_addr.city = request.POST['corresCity']
			staff.correspond_addr.state = request.POST['corresState']
			staff.correspond_addr.country = request.POST['corresCountry']
			staff.correspond_addr.pin = request.POST['corresPin']
			staff.correspond_addr.save()

			# Permanent Address
			staff.permanent_addr.addr1 = request.POST['permAddr1']
			staff.permanent_addr.addr2 = request.POST.get('permAddr2', '')
			staff.permanent_addr.city = request.POST['permCity']
			staff.permanent_addr.state = request.POST['permState']
			staff.permanent_addr.country = request.POST['permCountry']
			staff.permanent_addr.pin = request.POST['permPin']
			staff.permanent_addr.save()

			staff.category = request.POST.get('category')
			staff.obccreamy=request.POST.get('obccreamy')
			#Think about obc creamy file

			staff.save()

			return redirect('/staffrecruit')

		

	return render(request,'staffrecruit/mainform.djt',response)

def uploadpic(request):
	response = {}
	profile = StaffProfile.objects.get(user=request.user)
	response['profile'] = profile
	if request.method == 'POST' :
		file = request.FILES['profilepic']
		profile.profilePic = file
		profile.save()
	return render(request,'staffrecruit/uploadpic.djt',response)

def educationalqual(request):

	response={}
	app = StaffApp.objects.get(user=request.user)
	if StaffUser.objects.filter(app_id=app).exists():
		check=StaffUser.objects.get(app_id=app)
		for a in check.educationdet.all():
			if a.degree=='SSC':
				response['s']=a
			elif a.degree=='Intermediate':
				response['i']=a
			elif a.degree=='Degree':
				response['d']=a
			elif a.degree=='Masters':
				response['m']=a
			else:
				response['o']=a
	if request.method == 'POST' :
		if request.POST.get('savebutton'):

			#app = StaffApp.objects.get(user=request.user)
			staff=StaffUser.objects.get(app_id=app)
			ssc=Education()
			ssc.degree="SSC"
			ssc.university=request.POST['suniv']
			ssc.yearofpassing=request.POST['spassingyear']
			ssc.cgpa=request.POST['scgpa']
			ssc.classdiv=request.POST['sdivision']
			ssc.save()

			inter=Education()
			inter.degree="Intermediate"
			inter.university=request.POST['iuniv']
			inter.yearofpassing=request.POST['ipassingyear']
			inter.cgpa=request.POST['icgpa']
			inter.classdiv=request.POST['idivision']
			inter.save()

			deg=Education()
			deg.degree="Degree"
			deg.university=request.POST['duniv']
			deg.yearofpassing=request.POST['dpassingyear']
			deg.cgpa=request.POST['dcgpa']
			deg.classdiv=request.POST['ddivision']
			deg.save()

			master=Education()
			master.degree="Masters"
			master.university=request.POST['muniv']
			master.yearofpassing=request.POST['mpassingyear']
			master.cgpa=request.POST['mcgpa']
			master.classdiv=request.POST['mdivision']
			master.save()

			if request.POST['Ouniv']!="":
				other=Education()
				other.degree="Others"
				other.university=request.POST['Ouniv']
				other.yearofpassing=request.POST['Opassingyear']
				other.cgpa=request.POST['Ocgpa']
				other.classdiv=request.POST['Odivision']
				other.save()
				staff.educationdet.add(other)

			
			staff.educationdet.add(ssc)
			staff.educationdet.add(inter)
			staff.educationdet.add(deg)
			staff.educationdet.add(master)
			for afile in request.FILES.getlist('files'):
				proof1=Proof()
				proof1.appID=staff.app_id
				proof1.prooffile=afile;
				proof1.save()
    			staff.proof.add(proof1)
			
			staff.save()
		return redirect('/staffrecruit/experience/')
	return render(request,'staffrecruit/educationalQual.djt',response)

def experience(request):
	response={}
	app = StaffApp.objects.get(user=request.user)
	if StaffUser.objects.filter(app_id=app).exists():
		check=StaffUser.objects.get(app_id=app)
		ch=check.exprdet.all()
		
		# response['emp1']=ch[0]
		# response['emp2']=ch[1]

		ch1=check.adminpos.all()
	if request.method=="POST":
		if request.POST.get('savebutton'):
			staff=StaffUser.objects.get(app_id=app)
			emp1=Experience()
			emp1.org=request.POST['org1']
			emp1.designation=request.POST['des1']
			emp1.doj=request.POST['doj1']
			emp1.dol=request.POST['dol1']
			emp1.pay=request.POST['pay1']
			emp1.service=request.POST['service1']

			emp1.save()

			emp2=Experience()
			emp2.org=request.POST['org2']
			emp2.designation=request.POST['des2']
			emp2.doj=request.POST['doj2']
			emp2.dol=request.POST['dol2']
			emp2.pay=request.POST['pay2']
			emp2.service=request.POST['service2']
			emp2.save()

			staff.exprdet.add(emp1)
			staff.exprdet.add(emp2)

			for afile in request.FILES.getlist('files'):
				proof1=Proof()
				proof1.appID=staff.app_id
				proof1.prooffile=afile;
				proof1.save()
				staff.proof.add(proof1)

			admin1=Adminpos()
			admin1.resp_held=request.POST['resp1']
			admin1.duration=request.POST['dur1']
			admin1.save()

			admin2=Adminpos()
			admin2.resp_held=request.POST['resp2']
			admin2.duration=request.POST['dur2']
			admin2.save()

			staff.adminpos.add(admin1)
			staff.adminpos.add(admin2)
		redirect('/staffrecruit/experience/')
	return render(request,'staffrecruit/experiencedetails.djt',response)

def miscellaneous(request):
	app = StaffApp.objects.get(user=request.user)
	staff=StaffUser.objects.get(app_id=app)
	if request.method=="POST":
		member1=Membership()
		member1.name=request.POST['mem1']
		member1.save()

		member2=Membership()
		member2.name=request.POST['mem2']
		member2.save()

		extracurr1=Extracurr()
		extracurr1.name=request.POST['ext1']
		extracurr1.save()

		extracurr2=Extracurr()
		extracurr2.name=request.POST['ext2']
		extracurr2.save()



		staff.memberships.add(member1)
		staff.memberships.add(member2)

		staff.extracurr.add(extracurr1)
		staff.extracurr.add(extracurr2)



		redirect('staffrecruit/miscellaneous')
	return render(request,'staffrecruit/misc.djt')


def references(request):
	return render(request,'staffrecruit/references.djt')