# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest, Http404,JsonResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.models import User
from staffrecruit.models import StaffApp
import random
from .models import *
import datetime
from django.core.mail import send_mail
import smtplib
import os
import unicodedata

# Create your views here.
def index(request) :
	response = {}
	return render(request,'staffregistration/login.djt',response)

def send_to_register(request,errorNo='0') :
	response = {}
	if errorNo=='1' :
		msg = 'Registration for selected post has already been done using this'
		msg = msg + ' Email-id'
		response['error'] = msg
	if errorNo=='2' :
		response['error'] = 'Password do not match'
	if errorNo=='3':
		response['error'] = 'Password must be longer than 8 characters'
	#response['depts'] = Department.objects.all()
	response['posts'] = Post.objects.all()
	return render(request,'staffregistration/register.djt',response)

def createApp(request) :
	response = {}
	if request.method == 'POST' :

		emailid = request.POST['email']
		appPost = Post.objects.get(postID=request.POST['post'])
		if User.objects.filter(email=emailid).exists() :
			existingUsers = User.objects.filter(email=emailid)
			for existingUser in existingUsers :
				if StaffProfile.objects.filter(user=existingUser,postApplied=appPost).exists():
					return redirect('/staffregister/signup/1')

		pass1 = request.POST['password1']
		pass2 = request.POST['password2']
		if len(pass1) < 8:
			return redirect('/staffregister/signup/3')
		if pass1 != pass2 :
			return redirect('/staffregister/signup/2')
		else : 
			user = User()
			user.first_name = request.POST['firstName']
			user.last_name = request.POST['lastName']
			user.email = request.POST['email']

			#Application ID generation Logic
			year = datetime.datetime.now().year
			yy = str(year)
			p1 = yy[2:]
			p3 = str(appPost.postID)
			appPost.appCount = appPost.appCount + 1
			appPost.save()
			p4 = str(appPost.appCount).zfill(5)

			try:
				collegeName = Constants.objects.get(key = 'college')
			except:
				collegeName = "NITW"

			applicationID = collegeName+p1+p3+p4
			#####

			user.username = applicationID
			user.set_password(pass1)
			user.save()

			userprofile = StaffProfile()
			userprofile.user = user
			userprofile.postApplied = appPost
			userprofile.applicationID = applicationID
			userprofile.contact = request.POST['contact']
			userprofile.termsRead = False
			userprofile.save()

			app_data = StaffApp()
			app_data.user = user
			app_data.app_id = userprofile.applicationID
			app_data.post=userprofile.postApplied
			app_data.save()

			pay_data = PaymentDetails()
			pay_data.appID = applicationID
			pay_data.transID = request.POST['transID']
			pay_data.save()
			
			response['appID'] = applicationID
			#Mail application ID to applicant
			receiver = user.email
			sender = 'nitap_recruitment17@nitw.ac.in'
			content = 'Your Application ID is : '+applicationID+"\n Thanks for Registering."
			rlist = []
			rlist.append(receiver)
			try:
				send_mail('Application Id for Faculty Registration',content,sender,rlist,fail_silently=False,)
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return render(request,'registration/regDone.djt',response)
			#return redirect('/register/success')

	return redirect('/register/signup')

def signin(request) :
	response = {}
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username,password=password)
		if user is None :
			return render(request, 'staffregistration/login.djt', {'error': 'Wrong username or password'})
		else :
			login(request,user)
			user = request.user
			if request.user.is_superuser:
				return redirect('/faculty_admin')
			profile = StaffProfile.objects.get(user=request.user)
			if profile.termsRead :
				return redirect('/staffrecruit')
			else :
				return redirect('/staffregister/termsandconditions')

def termsandconditions(request) :
	response = {}
	profile = StaffProfile.objects.get(user=request.user)
	response['profile'] = profile

	if request.method == 'POST' :
		profile.termsRead = True
		profile.save()

	if profile.termsRead :
		return redirect('/staffrecruit')
	else :
		return render(request, 'staffregistration/termsandconditions.djt', response)


def paymentDetails(request):
	response = {}
	profile = StaffProfile.objects.get(user=request.user)
	pay_data = PaymentDetails.objects.get(appID=profile.applicationID)
	response['paydata'] = pay_data
	if request.method == 'POST' :
		pay_data.bankName = request.POST['bank']
		pay_data.accountNum = request.POST['account']
		pay_data.payDate = request.POST['paydate']
		pay_data.receipt = request.FILES['receipt']
		pay_data.payType = request.POST['paytype']
		if pay_data.payType == 'SC/ST/PWD':
			pay_data.amount = 'Rs.500'
		elif pay_data.payType == 'GEN/OBC':
			pay_data.amount = 'Rs.1000'
		elif pay_data.payType == 'abroad':
			pay_data.amount = '$25'
		
		if validateFormat(pay_data.receipt) :
			pay_data.save()
			app_data = StaffApp.objects.get(user=request.user)
			app_data.paymentUploaded = True
			app_data.save()
		else : 
			response['error'] = 'Only Pdf format is allowed'
			return render(request,'staffregistration/paymentDetails.djt',response)

		return redirect('/staffrecruit')

	return render(request,'staffregistration/paymentDetails.djt',response)

def validateFormat(filename):
    ext = os.path.splitext(filename.name)[1]
    valid_extentions = ['.pdf','.PDF']
    if not ext in valid_extentions:
        return False
    return True