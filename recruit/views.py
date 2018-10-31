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
from registration.models import *
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

def checkuserifpaymentuser(user):
    if user.groups.filter(name="paymentAdmin").exists() or user.is_superuser:
        return True
    else:
        return False

def checkuserifscrutinyuser(user):
    if user.groups.filter(name="scrutiny").exists() or user.is_superuser:
        return True
    else:
        return False

def checkuserifA2user(user):
    if user.groups.filter(name="A2").exists():
        return True
    else:
        return False

def checkuserifA1user(user):
    if user.groups.filter(name="A1").exists():
        return True
    else:
        return False

def checkuserifA3user(user):
    if user.groups.filter(name="A3").exists() or user.is_superuser:
        return True
    else:
        return False

def checkuserifmasteruser(user):
    if user.groups.filter(name="master").exists():
        return True
    else:
        return False

def checkuserifinternaluser(user):
    if user.groups.filter(name="internal").exists():
        return True
    else:
        return False

@login_required(login_url='/register')
def clone(request):
    response = {}
    # return HttpResponse('lol')
    # if request.method == 'POST':
    if True:
        # cloneid = request.POST['appid']
        cloneid = request.GET['from'] #from
        clone_id = Appdata.objects.get(app_id=cloneid)
        appid = request.GET['to']
        # return HttpResponse(cloneid+appid)
        app_id = Appdata.objects.get(app_id=appid)
        # app_id = Appdata.objects.get(user=request.user)

        app_id.specialize = clone_id.specialize
        app_id.save()
            
        if FacUser.objects.filter(app_id=clone_id).exists():
            FacUser.objects.filter(app_id=app_id).delete()
            fac = FacUser.objects.get(app_id=clone_id)
            fac.pk = None
            fac.id = None
            fac.app_id = app_id
            fac.save()
        if Experience.objects.filter(app_id=clone_id).exists():
            Experience.objects.filter(app_id=app_id).delete()
            fac = Experience.objects.get(app_id=clone_id)
            fac.pk = None
            fac.id = None
            fac.app_id = app_id
            fac.save()
        if Education.objects.filter(app_id=clone_id).exists():
            Education.objects.filter(app_id=app_id).delete()
            fac = Education.objects.get(app_id=clone_id)
            fac.pk = None
            fac.id = None
            fac.app_id = app_id
            fac.save()
        if Qualification.objects.filter(app_id=clone_id).exists():
            Qualification.objects.filter(app_id=app_id).delete()
            facs = Qualification.objects.filter(app_id=clone_id)
            for f in facs:
                fac = f
                fac.pk = None
                fac.id = None
                fac.app_id = app_id
                fac.save()
        if Research.objects.filter(app_id=clone_id).exists():
            Research.objects.filter(app_id=app_id).delete()
            fac = Research.objects.get(app_id=clone_id)
            fac.pk = None
            fac.id = None
            fac.app_id = app_id
            fac.save()
        if Other.objects.filter(app_id=clone_id).exists():
            Other.objects.filter(app_id=app_id).delete()
            fac = Other.objects.get(app_id=clone_id)
            fac.pk = None
            fac.id = None
            fac.app_id = app_id
            fac.save()
        if Paper.objects.filter(app_id=clone_id).exists():
            Paper.objects.filter(app_id=app_id).delete()
            fac = Paper.objects.get(app_id=clone_id)
            fac.pk = None
            fac.id = None
            fac.app_id = app_id
            fac.save()
        if Referral.objects.filter(app_id=clone_id).exists():
            Referral.objects.filter(app_id=app_id).delete()
            fac = Referral.objects.get(app_id=clone_id)
            fac.pk = None
            fac.id = None
            fac.app_id = app_id
            fac.save()
        if External_Sponsored_RnD.objects.filter(app_id=clone_id).exists():
            External_Sponsored_RnD.objects.filter(app_id=app_id).delete()
            fac = External_Sponsored_RnD.objects.get(app_id=clone_id)
            fac.pk = None
            fac.id = None
            fac.app_id = app_id
            fac.save()
        if Consultancy_Projects.objects.filter(app_id=clone_id).exists():
            Consultancy_Projects.objects.filter(app_id=app_id).delete()
            fac = Consultancy_Projects.objects.get(app_id=clone_id)
            fac.pk = None
            fac.id = None
            fac.app_id = app_id
            fac.save()
        if PhD_Completed.objects.filter(app_id=clone_id).exists():
            PhD_Completed.objects.filter(app_id=app_id).delete()
            fac = PhD_Completed.objects.get(app_id=clone_id)
            fac.pk = None
            fac.id = None
            fac.app_id = app_id
            fac.save()
        if Journal_Papers.objects.filter(app_id=clone_id).exists():
            Journal_Papers.objects.filter(app_id=app_id).delete()
            fac = Journal_Papers.objects.get(app_id=clone_id)
            fac.pk = None
            fac.id = None
            fac.app_id = app_id
            fac.save()
        if Conference_Paper_SCI.objects.filter(app_id=clone_id).exists():
            Conference_Paper_SCI.objects.filter(app_id=app_id).delete()
            fac = Conference_Paper_SCI.objects.get(app_id=clone_id)
            fac.pk = None
            fac.id = None
            fac.app_id = app_id
            fac.save()
        if Acad_Annex_A.objects.filter(app_id=clone_id).exists():
            Acad_Annex_A.objects.filter(app_id=app_id).delete()
            fac = Acad_Annex_A.objects.get(app_id=clone_id)
            fac.pk = None
            fac.id = None
            fac.app_id = app_id
            fac.save()
        if Acad_Annex_B.objects.filter(app_id=clone_id).exists():
            Acad_Annex_B.objects.filter(app_id=app_id).delete()
            fac = Acad_Annex_B.objects.get(app_id=clone_id)
            fac.pk = None
            fac.id = None
            fac.app_id = app_id
            fac.save()
        if Acad_Annex_C.objects.filter(app_id=clone_id).exists():
            Acad_Annex_C.objects.filter(app_id=app_id).delete()
            fac = Acad_Annex_C.objects.get(app_id=clone_id)
            fac.pk = None
            fac.id = None
            fac.app_id = app_id
            fac.save()
        if Acad_Annex_D.objects.filter(app_id=clone_id).exists():
            Acad_Annex_D.objects.filter(app_id=app_id).delete()
            fac = Acad_Annex_D.objects.get(app_id=clone_id)
            fac.pk = None
            fac.id = None
            fac.app_id = app_id
            fac.save()
        if Acad_Annex_E12.objects.filter(app_id=clone_id).exists():
            Acad_Annex_E12.objects.filter(app_id=app_id).delete()
            fac = Acad_Annex_E12.objects.get(app_id=clone_id)
            fac.pk = None
            fac.id = None
            fac.app_id = app_id
            fac.save()
        if Acad_Annex_F.objects.filter(app_id=clone_id).exists():
            Acad_Annex_F.objects.filter(app_id=app_id).delete()
            fac = Acad_Annex_F.objects.get(app_id=clone_id)
            fac.pk = None
            fac.id = None
            fac.app_id = app_id
            fac.save()
        if Acad_Annex_C.objects.filter(app_id=clone_id).exists():
            Acad_Annex_C.objects.filter(app_id=app_id).delete()
            fac = Acad_Annex_C.objects.get(app_id=clone_id)
            fac.pk = None
            fac.id = None
            fac.app_id = app_id
            fac.save()
        if Acad_Annex_G.objects.filter(app_id=clone_id).exists():
            Acad_Annex_G.objects.filter(app_id=app_id).delete()
            fac = Acad_Annex_G.objects.get(app_id=clone_id)
            fac.pk = None
            fac.id = None
            fac.app_id = app_id
            fac.save()
        if Acad_Annex_H.objects.filter(app_id=clone_id).exists():
            Acad_Annex_H.objects.filter(app_id=app_id).delete()
            fac = Acad_Annex_H.objects.get(app_id=clone_id)
            fac.pk = None
            fac.id = None
            fac.app_id = app_id
            fac.save()
        if Acad_Annex_I.objects.filter(app_id=clone_id).exists():
            Acad_Annex_I.objects.filter(app_id=app_id).delete()
            fac = Acad_Annex_I.objects.get(app_id=clone_id)
            fac.pk = None
            fac.id = None
            fac.app_id = app_id
            fac.save()
        if Acad_Annex_J.objects.filter(app_id=clone_id).exists():
            Acad_Annex_J.objects.filter(app_id=app_id).delete()
            fac = Acad_Annex_J.objects.get(app_id=clone_id)
            fac.pk = None
            fac.id = None
            fac.app_id = app_id
            fac.save()
        if Acad_Annex_K.objects.filter(app_id=clone_id).exists():
            Acad_Annex_K.objects.filter(app_id=app_id).delete()
            fac = Acad_Annex_K.objects.get(app_id=clone_id)
            fac.pk = None
            fac.id = None
            fac.app_id = app_id
            fac.save()
        if Acad_Annex_L.objects.filter(app_id=clone_id).exists():
            Acad_Annex_L.objects.filter(app_id=app_id).delete()
            fac = Acad_Annex_L.objects.get(app_id=clone_id)
            fac.pk = None
            fac.id = None
            fac.app_id = app_id
            fac.save()
        if Acad_Annex_M.objects.filter(app_id=clone_id).exists():
            Acad_Annex_M.objects.filter(app_id=app_id).delete()
            fac = Acad_Annex_M.objects.get(app_id=clone_id)
            fac.pk = None
            fac.id = None
            fac.app_id = app_id
            fac.save()
        if Acad_Annex_N.objects.filter(app_id=clone_id).exists():
            Acad_Annex_N.objects.filter(app_id=app_id).delete()
            fac = Acad_Annex_N.objects.get(app_id=clone_id)
            fac.pk = None
            fac.id = None
            fac.app_id = app_id
            fac.save()
        if Acad_Annex_O.objects.filter(app_id=clone_id).exists():
            Acad_Annex_O.objects.filter(app_id=app_id).delete()
            fac = Acad_Annex_O.objects.get(app_id=clone_id)
            fac.pk = None
            fac.id = None
            fac.app_id = app_id
            fac.save()
        if Acad_Annex_P.objects.filter(app_id=clone_id).exists():
            Acad_Annex_P.objects.filter(app_id=app_id).delete()
            fac = Acad_Annex_P.objects.get(app_id=clone_id)
            fac.pk = None
            fac.id = None
            fac.app_id = app_id
            fac.save()
        if Acad_Annex_Q.objects.filter(app_id=clone_id).exists():
            Acad_Annex_Q.objects.filter(app_id=app_id).delete()
            fac = Acad_Annex_Q.objects.get(app_id=clone_id)
            fac.pk = None
            fac.id = None
            fac.app_id = app_id
            fac.save()
        if Acad_Annex_R.objects.filter(app_id=clone_id).exists():
            Acad_Annex_R.objects.filter(app_id=app_id).delete()
            fac = Acad_Annex_R.objects.get(app_id=clone_id)
            fac.pk = None
            fac.id = None
            fac.app_id = app_id
            fac.save()
        if Acad_Annex_S.objects.filter(app_id=clone_id).exists():
            Acad_Annex_S.objects.filter(app_id=app_id).delete()
            fac = Acad_Annex_S.objects.get(app_id=clone_id)
            fac.pk = None
            fac.id = None
            fac.app_id = app_id
            fac.save()
        if Acad_Annex_T.objects.filter(app_id=clone_id).exists():
            Acad_Annex_T.objects.filter(app_id=app_id).delete()
            fac = Acad_Annex_T.objects.get(app_id=clone_id)
            fac.pk = None
            fac.id = None
            fac.app_id = app_id
            fac.save()
        if Acad_Annex_U.objects.filter(app_id=clone_id).exists():
            Acad_Annex_U.objects.filter(app_id=app_id).delete()
            fac = Acad_Annex_U.objects.get(app_id=clone_id)
            fac.pk = None
            fac.id = None
            fac.app_id = app_id
            fac.save()
        if Acad_Annex_V.objects.filter(app_id=clone_id).exists():
            Acad_Annex_V.objects.filter(app_id=app_id).delete()
            fac = Acad_Annex_V.objects.get(app_id=clone_id)
            fac.pk = None
            fac.id = None
            fac.app_id = app_id
            fac.save()
        if Acad_Annex_W1_W2.objects.filter(app_id=clone_id).exists():
            Acad_Annex_W1_W2.objects.filter(app_id=app_id).delete()
            fac = Acad_Annex_W1_W2.objects.get(app_id=clone_id)
            fac.pk = None
            fac.id = None
            fac.app_id = app_id
            fac.save()
        if Acad_Annex_X.objects.filter(app_id=clone_id).exists():
            Acad_Annex_X.objects.filter(app_id=app_id).delete()
            fac = Acad_Annex_X.objects.get(app_id=clone_id)
            fac.pk = None
            fac.id = None
            fac.app_id = app_id
            fac.save()
        if Acad_Annex_Y.objects.filter(app_id=clone_id).exists():
            Acad_Annex_Y.objects.filter(app_id=app_id).delete()
            fac = Acad_Annex_Y.objects.get(app_id=clone_id)
            fac.pk = None
            fac.id = None
            fac.app_id = app_id
            fac.save()
        if Acad_Annex_Z.objects.filter(app_id=clone_id).exists():
            Acad_Annex_Z.objects.filter(app_id=app_id).delete()
            fac = Acad_Annex_Z.objects.get(app_id=clone_id)
            fac.pk = None
            fac.id = None
            fac.app_id = app_id
            fac.save()
        if SubjectTaught.objects.filter(app_id=clone_id).exists():
            SubjectTaught.objects.filter(app_id=app_id).delete()
            facs = SubjectTaught.objects.filter(app_id=clone_id)
            for f in facs:
                fac = f
                fac.pk = None
                fac.id = None
                fac.app_id = app_id
                fac.save()

        return redirect('/')


    response['otherapps'] = []
    for otheruser in User.objects.filter(email=request.user.email):
        if otheruser != request.user:
            appln = Appdata.objects.get(user=otheruser)
            response['otherapps'].append(appln.app_id)
    response['len'] = len(response['otherapps'])

    return render(request,'recruit/clone.djt',response)


# @login_required(login_url='/register')
def unlock(request):
    app = Appdata.objects.get(user=User.objects.get(username='170610061'))
    entries = CallLetter.objects.get(dept=Department.objects.get(name=app.post_in), post=Post.objects.get(name=app.post_for), is_nitw=app.is_nitw)
    return HttpResponse([entries.is_sent,entries.dept.name,entries.post.name,entries.is_nitw])
    appid = request.GET['id']
    app_id = Appdata.objects.get(app_id=appid)
    app_id.submitted = False
    app_id.save()
    return redirect('/')


@login_required(login_url='/register')
def notsubmitted(request) :
    response = {}
    return render(request,'recruit/notsubmitted.djt',response)

# Landing view
@login_required(login_url='/register')
def index(request) :
    response = {}
    app = Appdata.objects.get(user=request.user)
    # entries = CallLetter.objects.get(dept=Department.objects.get(name=app.post_in), post=Post.objects.get(name=app.post_for), is_nitw=app.is_nitw)
    # if not entries.is_sent:
    #     logout(request)
    # 	return render(request,'registration/login.djt',{'error':'You are not allowed to login now.'})
    # if Shortlist.objects.filter(app_id=app).exists():
    #     return redirect('/call_letter')
    # return redirect('/printSummary')

    # if app.submitted:
    #     return redirect('/printSummary')
    # else:
    #     return redirect('/notsubmitted')

    if app.paymentUploaded == False and app.is_nitw == False:
        return redirect('/pay/')

    if app.submitted :
        return redirect('/printSummary')

    profile = UserProfile.objects.get(user=request.user)
    print(profile)
    response['profile'] = profile
    if request.method == "POST" :
        app_id = Appdata.objects.get(user=request.user)
        postID = Post.objects.get(name=app_id.post_for).postID
        if postID==1 :
            print request.POST.get('agp1')
            if request.POST.get('agp1')=='on' :
                app_id.agp1 = True
                app_id.save()
            else :
                app_id.agp1 = False
                app_id.save()
            if request.POST.get('agp2') :
                app_id.agp2 = True
                app_id.save()
            else :
                app_id.agp2 = False
                app_id.save()
            if request.POST.get('agp3') :
                app_id.agp3 = True
                app_id.save()
            else :
                app_id.agp3 = False
                app_id.save()
        #generalInfo part  :
        app_id.specialize = request.POST['specialization']
        app_id.save()

        if not FacUser.objects.filter(app_id=app_id).exists() :
            facuser = FacUser()
            facuser.app_id = app_id
            permanent_addr = Address()
            permanent_addr.save()
            correspond_addr = Address()
            correspond_addr.save()
            facuser.permanent_addr = permanent_addr
            facuser.correspond_addr = correspond_addr
        else :
            facuser = FacUser.objects.get(app_id=app_id)

        # Getting post data
        facuser.full_name = request.POST['Name']
        facuser.gender = request.POST.get('gender', 'Male')
        facuser.father_name = request.POST['fatherName']
        facuser.father_occ = request.POST.get('fatherOccupation')
        facuser.mother_name = request.POST['motherName']
        facuser.mother_occ = request.POST.get('motherOccupation')
        facuser.nation = request.POST['nationality']
        facuser.pob = request.POST['birthplace']
        facuser.dob = request.POST['dateOfBirth']
        facuser.age = calculate_age(facuser.dob)
        facuser.aadhaarNo = request.POST.get('aadhaar')

        # Correspond Addr
        facuser.correspond_addr.addr1 = request.POST['corresAddr1']
        facuser.correspond_addr.addr2 = request.POST.get('corresAddr2','')
        facuser.correspond_addr.city = request.POST['corresCity']
        facuser.correspond_addr.state = request.POST['corresState']
        facuser.correspond_addr.country = request.POST['corresCountry']
        facuser.correspond_addr.pin = request.POST['corresPin']
        facuser.correspond_addr.save()

        # Permanent Address
        facuser.permanent_addr.addr1 = request.POST['permAddr1']
        facuser.permanent_addr.addr2 = request.POST.get('permAddr2', '')
        facuser.permanent_addr.city = request.POST['permCity']
        facuser.permanent_addr.state = request.POST['permState']
        facuser.permanent_addr.country = request.POST['permCountry']
        facuser.permanent_addr.pin = request.POST['permPin']
        facuser.permanent_addr.save()

        facuser.category = request.POST.get('category', 'UR')
        facuser.pwd = request.POST.get('pwd','no')
        
        facuser.save()

        # Checking whether to goto next page or not.
        print "checking"
        if request.POST.get('nextBtn'):
            print "nextBtn clicked"
            return redirect('/register/uploadpic')
        else:
            print "save clicked"


    if Appdata.objects.filter(user=request.user).exists() :
        app_id = Appdata.objects.get(user=request.user)
        response['agp1'] = app_id.agp1
        response['agp2'] = app_id.agp2
        response['agp3'] = app_id.agp3
        response['postID'] = Post.objects.get(name=app_id.post_for).postID
        response['specialization'] = app_id.specialize
        if FacUser.objects.filter(app_id=app_id).exists():
            facuser = FacUser.objects.get(app_id=app_id)
            response['generalData'] = facuser
            response['corresAddr'] = facuser.correspond_addr
            response['permAddr'] = facuser.permanent_addr

    return render(request,'recruit/mainForm.djt',response)
 
# Educational Qualifications view
@login_required(login_url='/register')
def educationalQual(request):
    response = {}
    app_id = Appdata.objects.get(user=request.user)

    print "educational qualificatins"

    if request.method == "POST" :
        print request.POST
        print "post"

        if not Qualification.objects.filter(app_id=app_id,degreeType='UG').exists():
            ugdegree = Qualification()
        else :
            ugdegree = Qualification.objects.get(app_id=app_id,degreeType='UG')
        ugdegree.app_id = app_id
        ugdegree.degreeType = 'UG'
        ugdegree.degreeName = request.POST['Bdegree']
        ugdegree.university = request.POST['Buniv']
        ugdegree.passingYear = request.POST['Bpassingyear']
        ugdegree.marks = request.POST['Bmarks']
        ugdegree.division = request.POST['Bdivision']
        ugdegree.save()

        if not Qualification.objects.filter(app_id=app_id,degreeType='PG').exists():
            pgdegree = Qualification()
        else :
            pgdegree = Qualification.objects.get(app_id=app_id,degreeType='PG')
        pgdegree.app_id = app_id
        pgdegree.degreeType = 'PG'
        pgdegree.degreeName = request.POST['Mdegree']
        pgdegree.university = request.POST['Muniv']
        pgdegree.passingYear = request.POST['Mpassingyear']
        pgdegree.marks = request.POST['Mmarks']
        pgdegree.division = request.POST['Mdivision']
        pgdegree.save()

        if not Qualification.objects.filter(app_id=app_id,degreeType='PHD').exists():
            phdDegree = Qualification()
        else :
            phdDegree = Qualification.objects.get(app_id=app_id,degreeType='PHD')
        phdDegree.app_id = app_id
        phdDegree.degreeType = 'PHD'
        phdDegree.degreeName = request.POST['Phddegree']
        phdDegree.university = request.POST['Phduniv']
        phdDegree.passingYear = request.POST['Phdpassingyear']
        phdDegree.marks = request.POST.get('Phdmarks')
        phdDegree.division = request.POST.get('Phddivision')
        phdDegree.save()

        if not Qualification.objects.filter(app_id=app_id,degreeType='other').exists():
            if request.POST.get('Odegree') :
                ODegree = Qualification()
                ODegree.app_id = app_id
                ODegree.degreeType = 'other'
                ODegree.degreeName = request.POST.get('Odegree')
                ODegree.university = request.POST.get('Ouniv')
                ODegree.passingYear = request.POST.get('Opassingyear')
                ODegree.marks = request.POST.get('Omarks')
                ODegree.division = request.POST.get('Odivision')
                ODegree.save()
        else :
            ODegree = Qualification.objects.get(app_id=app_id,degreeType='other')
            ODegree.app_id = app_id
            ODegree.degreeType = 'other'
            ODegree.degreeName = request.POST.get('Odegree')
            ODegree.university = request.POST.get('Ouniv')
            ODegree.passingYear = request.POST.get('Opassingyear')
            ODegree.marks = request.POST.get('Omarks')
            ODegree.division = request.POST.get('Odivision')
            ODegree.save()

        # Save and go to annexxure A
        print "checking"
        if request.POST.get('annexAbutton'):
            print "annex a clicked"
            return redirect('/academic/annexure_a')
        elif request.POST.get('nextBtn'):
            print "next called"
            return redirect('/experiencedetails')
        else:
            print "save clicked"

    if Qualification.objects.filter(app_id=app_id,degreeType='UG').exists():
        response['Bqual'] = Qualification.objects.get(app_id=app_id,degreeType='UG')
    if Qualification.objects.filter(app_id=app_id,degreeType='PG').exists():
        response['Mqual'] = Qualification.objects.get(app_id=app_id,degreeType='PG')
    if Qualification.objects.filter(app_id=app_id,degreeType='PHD').exists():
        response['Phdqual'] = Qualification.objects.get(app_id=app_id,degreeType='PHD')
    if Qualification.objects.filter(app_id=app_id,degreeType='other').exists():
        response['Oqual'] = Qualification.objects.get(app_id=app_id,degreeType='other')
    acad_annex_a = Acad_Annex_A.objects.filter(app_id=app_id)
    if acad_annex_a.count() > 0:
        response['acad_annex_a'] = acad_annex_a[0].store
    return render(request,'recruit/appform/educationalQual.djt',response)

# Experience Details 
@login_required(login_url='/register')
def experienceDetails(request):
    response = {}
    print "experience details"
    app_id = Appdata.objects.get(user=request.user)

    if request.method == "POST" :
        print "post"
        print request.POST

        if not Experience.objects.filter(app_id=app_id).exists() :
            exp = Experience()
            exp.app_id = app_id
        else :
            exp = Experience.objects.get(app_id=app_id)

        exp.teaching_data = request.POST.get('teachingExpData','[]')
        exp.research_data = request.POST.get('researchExpData','[]')
        exp.industrial_data = request.POST.get('industryExpData','[]')
        exp.teaching_exp = request.POST['teachingExperience']
        exp.postPhd_exp = request.POST['phdExperience']
        exp.research_exp = request.POST['researchExperience']
        exp.industrial_exp = request.POST['industryExperience']
        exp.save()

        # Save and go upload supporting docs if necessary
        print "checking"
        if request.POST.get('supportDocBtn'):
            print "support docs clicked clicked"
            return redirect('/uploadExpDoc')
        elif request.POST.get('nextBtn'):
            print "next called"
            return redirect('/academic')
        else:
            print "save clicked"


    if Experience.objects.filter(app_id=app_id).exists():
        exp = Experience.objects.get(app_id=app_id)
        response['Experience'] = exp
        response['teachingData'] = json.loads(exp.teaching_data)
        response['researchData'] = json.loads(exp.research_data)
        response['industryData'] = json.loads(exp.industrial_data)

    # For supporting documents
    if Paper.objects.filter(app_id=app_id).exists() :
            paperobj = Paper.objects.get(app_id=app_id)
            response['paperobj'] = paperobj

    return render(request,'recruit/appform/experienceDetails.djt',response)


@login_required(login_url='/register')
def annexure_e12_main(request):
    print "HELOOO"
    response = {}
    app_id = Appdata.objects.get(user=request.user)

    if app_id.submitted :
        return redirect('/printSummary')

    external_sponsored_rnd = External_Sponsored_RnD.objects.filter(app_id=app_id)
    acad_annex_e12 = Acad_Annex_E12.objects.filter(app_id=app_id)

    if request.method == "POST":
        print "Boos"
        response['show'] = 1
        if external_sponsored_rnd.count() == 0:
            external_sponsored_rnd = External_Sponsored_RnD()
            external_sponsored_rnd.app_id = app_id
            external_sponsored_rnd.projects_not_pi = request.POST['projects_not_pi']
            external_sponsored_rnd.patents_not_pi = request.POST['patents_not_pi']
            external_sponsored_rnd.save()
        else:
            external_sponsored_rnd = external_sponsored_rnd[0]
        external_sponsored_rnd.total_projects = request.POST['total_projects']
        external_sponsored_rnd.project_as_PI = request.POST['projects_as_PI']
        external_sponsored_rnd.total_patents = request.POST['total_patents']
        external_sponsored_rnd.patents_as_pi = request.POST['patents_as_pi']
        external_sponsored_rnd.credit_val = request.POST['credits_1']
        # external_sponsored_rnd.patents_not_pi = request.POST['patents_not_pi']
        # if len(request.POST['projects_not_pi'])>2:
        #     oldstr = external_sponsored_rnd.projects_not_pi
        #     newstr = request.POST['projects_not_pi']
        #     external_sponsored_rnd.projects_not_pi = oldstr[:-1] + "," + newstr[1:]

        if len(request.POST['projects_not_pi'])>2:
            oldstr = external_sponsored_rnd.projects_not_pi
            newstr = request.POST['projects_not_pi']
            if oldstr == '[]':
                external_sponsored_rnd.projects_not_pi = "[" + newstr[1:]
            else:
                external_sponsored_rnd.projects_not_pi = oldstr[:-1] + "," + newstr[1:]
        
        # if len(request.POST['patents_not_pi'])>2:
        #     oldstr = external_sponsored_rnd.patents_not_pi
        #     newstr = request.POST['patents_not_pi']
        #     external_sponsored_rnd.patents_not_pi = oldstr[:-1] + "," + newstr[1:]
        if len(request.POST['patents_not_pi'])>2:
            oldstr = external_sponsored_rnd.patents_not_pi
            newstr = request.POST['patents_not_pi']
            if oldstr == '[]':
                external_sponsored_rnd.patents_not_pi = "[" + newstr[1:]
            else:
                external_sponsored_rnd.patents_not_pi = oldstr[:-1] + "," + newstr[1:]

        external_sponsored_rnd.save()

        response['external_sponsored_rnd'] = external_sponsored_rnd

        if external_sponsored_rnd.projects_not_pi:
            response['projects_not_pi'] = json.loads(external_sponsored_rnd.projects_not_pi)
        if external_sponsored_rnd.patents_not_pi:
            response['patents_not_pi'] = json.loads(external_sponsored_rnd.patents_not_pi)
    else:
        if external_sponsored_rnd.count() > 0:
            response['show'] = 1 #whether to enable or disable the button for annexures
            response['external_sponsored_rnd'] = external_sponsored_rnd[0]
            if external_sponsored_rnd[0].projects_not_pi:
                response['projects_not_pi'] = json.loads(external_sponsored_rnd[0].projects_not_pi)
            if external_sponsored_rnd[0].patents_not_pi:
                response['patents_not_pi'] = json.loads(external_sponsored_rnd[0].patents_not_pi)
        else:
            response['show'] = 0

    if acad_annex_e12.count() > 0:
            response['acad_annex_e12'] = acad_annex_e12[0]
            response['total_e'] = float(acad_annex_e12[0].total_e1 + acad_annex_e12[0].total_e2)

    return redirect('/academic')

@login_required(login_url='/register')
def annexure_f_main(request):
    response = {}
    app_id = Appdata.objects.get(user=request.user)

    if app_id.submitted :
        return redirect('/printSummary')

    consultancy_projects = Consultancy_Projects.objects.filter(app_id=app_id)
    acad_annex_f = Acad_Annex_F.objects.filter(app_id=app_id)
    if acad_annex_f.count() > 0:
        response['acad_annex_f'] = acad_annex_f[0]

    if request.method == "POST":
        response['show'] = 1
        if consultancy_projects.count() == 0:
            consultancy_projects = Consultancy_Projects()
            consultancy_projects.app_id = app_id
        else:
            consultancy_projects = consultancy_projects[0]
        consultancy_projects.consultancy_projects_completed = request.POST['consultancy_projects_completed']
        consultancy_projects.amount = request.POST['amount']
        consultancy_projects.credit_val = request.POST['credits_2']
        consultancy_projects.save()
        response['consultancy_projects'] = consultancy_projects
    else:
        if consultancy_projects.count() > 0:
            response['show'] = 1
            response['consultancy_projects'] = consultancy_projects[0]
        else:
            response['show'] = 0

    return redirect('/academic')

@login_required(login_url='/register')
def annexure_g_main(request):
    response = {}
    app_id = Appdata.objects.get(user=request.user)

    if app_id.submitted :
        return redirect('/printSummary')

    phd_completed = PhD_Completed.objects.filter(app_id=app_id)
    acad_annex_g = Acad_Annex_G.objects.filter(app_id=app_id)
    if acad_annex_g.count() > 0:
        response['acad_annex_g'] = acad_annex_g[0]

    if request.method == "POST":
        response['show'] = 1
        if phd_completed.count() == 0:
            phd_completed = PhD_Completed()
            phd_completed.app_id = app_id
            phd_completed.phds = request.POST['phds']
            phd_completed.save()
        else:
            phd_completed = phd_completed[0]
        phd_completed.total_phd = request.POST['total_phd']
        phd_completed.credit_val = request.POST['credits_3']
        phd_completed.as_first_supervisor = request.POST['as_first_supervisor_phd']
        if len(request.POST['phds'])>2:
            oldstr = phd_completed.phds
            newstr = request.POST['phds']
            if oldstr == "[]":
                phd_completed.phds = "[" + newstr[1:]
            else:
                phd_completed.phds = oldstr[:-1] + "," + newstr[1:]
        phd_completed.save()
        response['phd_completed'] = phd_completed
        if phd_completed.phds:
            response['phds'] = json.loads(phd_completed.phds)
    else:
        if phd_completed.count() > 0:
            response['show'] = 1
            response['phd_completed'] = phd_completed[0]
            if phd_completed[0].phds:
                response['phds'] = json.loads(phd_completed[0].phds)
        else:
            response['show'] = 0

    return redirect('/academic')

@login_required(login_url='/register')
def annexure_h_main(request):
    response = {}
    app_id = Appdata.objects.get(user=request.user)

    if app_id.submitted :
        return redirect('/printSummary')

    journal_papers = Journal_Papers.objects.filter(app_id = app_id)
    acad_annex_h = Acad_Annex_H.objects.filter(app_id=app_id)    
    if acad_annex_h.count() > 0:
        response['acad_annex_h'] = acad_annex_h[0]

    if request.method == "POST":
        response['show'] = 1
        if journal_papers.count() == 0:
            journal_papers = Journal_Papers()
            journal_papers.app_id = app_id
            journal_papers.papers = request.POST['papers']
            journal_papers.save()
        else:
            journal_papers = journal_papers[0]
        journal_papers.total_journal_papers = request.POST['total_journal_papers']
        journal_papers.as_first_supervisor = request.POST['as_first_supervisor_journal']
        journal_papers.credit_val = request.POST['credits_4']
        if len(request.POST['papers'])>2:
            oldstr = journal_papers.papers
            newstr = request.POST['papers']
            if oldstr == "[]":
                journal_papers.papers = "[" + newstr[1:]
            else:
                journal_papers.papers = oldstr[:-1] + "," + newstr[1:]

        journal_papers.save()
        response['journal_papers'] = journal_papers
        if journal_papers.papers:
            response['papers'] = json.loads(journal_papers.papers)
    else:
        if journal_papers.count() > 0:
            response['show'] = 1
            response['journal_papers'] = journal_papers[0]
            if journal_papers[0].papers:
                response['papers'] = json.loads(journal_papers[0].papers)
        else:
            response['show'] = 0

    return redirect('/academic')

@login_required(login_url='/register')
def annexure_i_main(request):
    response = {}
    app_id = Appdata.objects.get(user=request.user)

    if app_id.submitted :
        return redirect('/printSummary')

    conference_paper_sci = Conference_Paper_SCI.objects.filter(app_id = app_id)
    acad_annex_i = Acad_Annex_I.objects.filter(app_id=app_id)
    if acad_annex_i.count() > 0:
        response['acad_annex_i'] = acad_annex_i[0]

    if request.method == "POST":
        response['show'] = 1
        if conference_paper_sci.count() == 0:
            conference_paper_sci = Conference_Paper_SCI()
            conference_paper_sci.app_id = app_id
            conference_paper_sci.papers = request.POST['papers1']
            conference_paper_sci.save()
        else:
            conference_paper_sci = conference_paper_sci[0]
        conference_paper_sci.total_confernce_papers = request.POST['total_confernce_papers']
        conference_paper_sci.as_first_supervisor = request.POST['as_first_supervisor_conference']
        conference_paper_sci.credit_val = request.POST['credits_5']
        if len(request.POST['papers1'])>2:
            oldstr = journal_papers.papers
            newstr = request.POST['papers1']
            if oldstr == "[]":
                conference_paper_sci.papers = "[" + newstr[1:]
            else:
                conference_paper_sci.papers = oldstr[:-1] + "," + newstr[1:]

        conference_paper_sci.save()
        response['conference_paper_sci'] = conference_paper_sci
        if conference_paper_sci.papers:
            response['papers1'] = json.loads(conference_paper_sci.papers)
    else:
        if conference_paper_sci.count() > 0:
            response['show'] = 1
            response['conference_paper_sci'] = conference_paper_sci[0]
            if conference_paper_sci[0].papers:
                response['papers1'] = json.loads(conference_paper_sci[0].papers)
        else:
            response['show'] = 0

    return redirect('/academic')
        

@login_required(login_url='/register')
def annexure_j_main(request):
    response = {}
    app_id = Appdata.objects.get(user=request.user)

    if app_id.submitted :
        return redirect('/printSummary')

    acad_annex_j = Acad_Annex_J.objects.filter(app_id=app_id)

    if request.method == "POST":
        response['show'] = 1
        if acad_annex_j.count() == 0:
            acad_annex_j = Acad_Annex_J()
            acad_annex_j.app_id = app_id
        else:
            acad_annex_j = acad_annex_j[0]
        acad_annex_j.total_sem = request.POST['total_semj']
        acad_annex_j.credit_val = request.POST['credits_6']
        acad_annex_j.save()
        response['acad_annex_j'] = acad_annex_j
    else:
        if acad_annex_j.count() > 0:
            response['show'] = 1
            response['acad_annex_j'] = acad_annex_j[0]
        else:
            response['show'] = 0
    
    return redirect('/academic')


@login_required(login_url='/register')
def annexure_k_main(request):
    response = {}
    app_id = Appdata.objects.get(user=request.user)

    if app_id.submitted :
        return redirect('/printSummary')

    acad_annex_k = Acad_Annex_K.objects.filter(app_id=app_id)

    if request.method == "POST":
        response['show'] = 1
        if acad_annex_k.count() == 0:
            acad_annex_k = Acad_Annex_K()
            acad_annex_k.app_id = app_id
        else:
            acad_annex_k = acad_annex_k[0]
        acad_annex_k.total_sem = request.POST['total_semk']
        acad_annex_k.credit_val = request.POST['credits_7']
        acad_annex_k.save()
        response['acad_annex_k'] = acad_annex_k
    else:
        if acad_annex_k.count() > 0:
            response['show'] = 1
            response['acad_annex_k'] = acad_annex_k[0]
        else:
            response['show'] = 0

    return redirect('/academic')


@login_required(login_url='/register')
def annexure_l_main(request):
    response = {}
    app_id = Appdata.objects.get(user=request.user)

    if app_id.submitted :
        return redirect('/printSummary')

    acad_annex_l = Acad_Annex_L.objects.filter(app_id=app_id)

    if request.method == "POST":
        response['show'] = 1
        if acad_annex_l.count() == 0:
            acad_annex_l = Acad_Annex_L()
            acad_annex_l.app_id = app_id
        else:
            acad_annex_l = acad_annex_l[0]
        acad_annex_l.total_sem = request.POST['total_seml']
        acad_annex_l.credit_val = request.POST['credits_8']
        acad_annex_l.save()
        response['acad_annex_l'] = acad_annex_l
    else:
        if acad_annex_l.count() > 0:
            response['show'] = 1
            response['acad_annex_l'] = acad_annex_l[0]
        else:
            response['show'] = 0

    return redirect('/academic')


@login_required(login_url='/register')
def annexure_m_main(request):
    response = {}
    app_id = Appdata.objects.get(user=request.user)

    if app_id.submitted :
        return redirect('/printSummary')

    acad_annex_m = Acad_Annex_M.objects.filter(app_id=app_id)

    if request.method == "POST":
        response['show'] = 1
        if acad_annex_m.count() == 0:
            acad_annex_m = Acad_Annex_M()
            acad_annex_m.app_id = app_id
        else:
            acad_annex_m = acad_annex_m[0]
        acad_annex_m.total_sem = request.POST['total_semm']
        acad_annex_m.credit_val = request.POST['credits_9']
        acad_annex_m.save()
        response['acad_annex_m'] = acad_annex_m
    else:
        if acad_annex_m.count() > 0:
            response['show'] = 1
            response['acad_annex_m'] = acad_annex_m[0]
        else:
            response['show'] = 0

    return redirect('/academic')

@login_required(login_url='/register')
def annexure_n_main(request):
    response = {}
    app_id = Appdata.objects.get(user=request.user)

    if app_id.submitted :
        return redirect('/printSummary')

    acad_annex_n = Acad_Annex_N.objects.filter(app_id=app_id)

    if request.method == "POST":
        response['show'] = 1
        if acad_annex_n.count() == 0:
            acad_annex_n = Acad_Annex_N()
            acad_annex_n.app_id = app_id
        else:
            acad_annex_n = acad_annex_n[0]
        acad_annex_n.total_number = request.POST['total_numbern']
        acad_annex_n.credit_val = request.POST['credits_10']
        acad_annex_n.save()
        response['acad_annex_n'] = acad_annex_n
    else:
        if acad_annex_n.count() > 0:
            response['show'] = 1
            response['acad_annex_n'] = acad_annex_n[0]
        else:
            response['show'] = 0

    return redirect('/academic')


@login_required(login_url='/register')
def annexure_o_main(request):
    response = {}
    app_id = Appdata.objects.get(user=request.user)

    if app_id.submitted :
        return redirect('/printSummary')

    acad_annex_o = Acad_Annex_O.objects.filter(app_id=app_id)

    if request.method == "POST":
        response['show'] = 1
        if acad_annex_o.count() == 0:
            acad_annex_o = Acad_Annex_O()
            acad_annex_o.app_id = app_id
        else:
            acad_annex_o = acad_annex_o[0]
        acad_annex_o.prog_2_week_duration = request.POST['prog_2_week_duration']
        acad_annex_o.prog_1_week_duration = request.POST['prog_1_week_duration']
        acad_annex_o.credit_val = request.POST['credits_11']
        acad_annex_o.save()
        response['acad_annex_o'] = acad_annex_o
    else:
        if acad_annex_o.count() > 0:
            response['show'] = 1
            response['acad_annex_o'] = acad_annex_o[0]
        else:
            response['show'] = 0

    return redirect('/academic')

@login_required(login_url='/register')
def annexure_p_main(request):
    response = {}
    app_id = Appdata.objects.get(user=request.user)

    if app_id.submitted :
        return redirect('/printSummary')

    acad_annex_p = Acad_Annex_P.objects.filter(app_id=app_id)

    if request.method == "POST":
        response['show'] = 1
        if acad_annex_p.count() == 0:
            acad_annex_p = Acad_Annex_P()
            acad_annex_p.app_id = app_id
        else:
            acad_annex_p = acad_annex_p[0]
        acad_annex_p.total_number = request.POST['total_numberp']
        acad_annex_p.credit_val = request.POST['credits_12']
        acad_annex_p.save()
        response['acad_annex_p'] = acad_annex_p
    else:
        if acad_annex_p.count() > 0:
            response['show'] = 1
            response['acad_annex_p'] = acad_annex_p[0]
        else:
            response['show'] = 0

    return redirect('/academic')

@login_required(login_url='/register')
def annexure_q_main(request):
    response = {}
    app_id = Appdata.objects.get(user=request.user)

    if app_id.submitted :
        return redirect('/printSummary')

    acad_annex_q = Acad_Annex_Q.objects.filter(app_id=app_id)

    if request.method == "POST":
        response['show'] = 1
        if acad_annex_q.count() == 0:
            acad_annex_q = Acad_Annex_Q()
            acad_annex_q.app_id = app_id
        else:
            acad_annex_q = acad_annex_q[0]
        acad_annex_q.total_years = request.POST['total_years']
        acad_annex_q.total_months = request.POST['total_months']
        acad_annex_q.credit_val = request.POST['credits_13']
        acad_annex_q.save()
        response['acad_annex_q'] = acad_annex_q
    else:
        if acad_annex_q.count() > 0:
            response['show'] = 1
            response['acad_annex_q'] = acad_annex_q[0]
        else:
            response['show'] = 0

    return redirect('/academic')

@login_required(login_url='/register')
def annexure_r_main(request):
    response = {}
    app_id = Appdata.objects.get(user=request.user)

    if app_id.submitted :
        return redirect('/printSummary')

    acad_annex_r = Acad_Annex_R.objects.filter(app_id=app_id)

    if request.method == "POST":
        response['show'] = 1
        if acad_annex_r.count() == 0:
            acad_annex_r = Acad_Annex_R()
            acad_annex_r.app_id = app_id
        else:
            acad_annex_r = acad_annex_r[0]
        acad_annex_r.total_number = request.POST['total_numberr']
        acad_annex_r.credit_val = request.POST['credits_14']
        acad_annex_r.save()
        response['acad_annex_r'] = acad_annex_r
    else:
        if acad_annex_r.count() > 0:
            response['show'] = 1
            response['acad_annex_r'] = acad_annex_r[0]
        else:
            response['show'] = 0

    return redirect('/academic')

@login_required(login_url='/register')
def annexure_s_main(request):
    response = {}
    app_id = Appdata.objects.get(user=request.user)

    if app_id.submitted :
        return redirect('/printSummary')

    acad_annex_s = Acad_Annex_S.objects.filter(app_id=app_id)

    if request.method == "POST":
        response['show'] = 1
        if acad_annex_s.count() == 0:
            acad_annex_s = Acad_Annex_S()
            acad_annex_s.app_id = app_id
        else:
            acad_annex_s = acad_annex_s[0]
        acad_annex_s.total_credit = request.POST['total_creditss']
        acad_annex_s.credit_val = request.POST['credits_15']
        acad_annex_s.save()
        response['acad_annex_s'] = acad_annex_s
    else:
        if acad_annex_s.count() > 0:
            response['show'] = 1
            response['acad_annex_s'] = acad_annex_s[0]
        else:
            response['show'] = 0

    return redirect('/academic')

@login_required(login_url='/register')
def annexure_t_main(request):
    response = {}
    app_id = Appdata.objects.get(user=request.user)

    if app_id.submitted :
        return redirect('/printSummary')

    acad_annex_t = Acad_Annex_T.objects.filter(app_id=app_id)

    if request.method == "POST":
        response['show'] = 1
        if acad_annex_t.count() == 0:
            acad_annex_t = Acad_Annex_T()
            acad_annex_t.app_id = app_id
        else:
            acad_annex_t = acad_annex_t[0]
        acad_annex_t.total_number = request.POST['total_numbert']
        acad_annex_t.credit_val = request.POST['credits_16']
        acad_annex_t.save()
        response['acad_annex_t'] = acad_annex_t
    else:
        if acad_annex_t.count() > 0:
            response['show'] = 1
            response['acad_annex_t'] = acad_annex_t[0]
        else:
            response['show'] = 0

    return redirect('/academic')


@login_required(login_url='/register')
def annexure_u_main(request):
    response = {}
    app_id = Appdata.objects.get(user=request.user)

    if app_id.submitted :
        return redirect('/printSummary')

    acad_annex_u = Acad_Annex_U.objects.filter(app_id=app_id)

    if request.method == "POST":
        response['show'] = 1
        if acad_annex_u.count() == 0:
            acad_annex_u = Acad_Annex_U()
            acad_annex_u.app_id = app_id
        else:
            acad_annex_u = acad_annex_u[0]
        acad_annex_u.total_number = request.POST['total_numberu']
        acad_annex_u.credit_val = request.POST['credits_17']
        acad_annex_u.save()
        response['acad_annex_u'] = acad_annex_u
    else:
        if acad_annex_u.count() > 0:
            response['show'] = 1
            response['acad_annex_u'] = acad_annex_u[0]
        else:
            response['show'] = 0

    return redirect('/academic')

@login_required(login_url='/register')
def annexure_v_main(request):
    response = {}
    app_id = Appdata.objects.get(user=request.user)

    if app_id.submitted :
        return redirect('/printSummary')

    acad_annex_v = Acad_Annex_V.objects.filter(app_id=app_id)

    if request.method == "POST":
        response['show'] = 1
        if acad_annex_v.count() == 0:
            acad_annex_v = Acad_Annex_V()
            acad_annex_v.app_id = app_id
        else:
            acad_annex_v = acad_annex_v[0]
        acad_annex_v.total_number = request.POST['total_numberv']
        acad_annex_v.credit_val = request.POST['credits_18']
        acad_annex_v.save()
        response['acad_annex_v'] = acad_annex_v
    else:
        if acad_annex_v.count() > 0:
            response['show'] = 1
            response['acad_annex_v'] = acad_annex_v[0]
        else:
            response['show'] = 0

    return redirect('/academic')

@login_required(login_url='/register')
def annexure_w_main(request):
    response = {}
    app_id = Appdata.objects.get(user=request.user)

    if app_id.submitted :
        return redirect('/printSummary')

    acad_annex_w1_w2 = Acad_Annex_W1_W2.objects.filter(app_id=app_id)

    if request.method == "POST":
        response['show'] = 1
        if acad_annex_w1_w2.count() == 0:
            acad_annex_w1_w2 = Acad_Annex_W1_W2()
            acad_annex_w1_w2.app_id = app_id
        else:
            acad_annex_w1_w2 = acad_annex_w1_w2[0]
        acad_annex_w1_w2.total_number = request.POST['total_numberw1_w2']
        acad_annex_w1_w2.credit_val = request.POST['credits_19']
        acad_annex_w1_w2.save()
        response['acad_annex_w1_w2'] = acad_annex_w1_w2
    else:
        if acad_annex_w1_w2.count() > 0:
            response['show'] = 1
            response['acad_annex_w1_w2'] = acad_annex_w1_w2[0]
            response['total_w'] = float(acad_annex_w1_w2[0].total_w1 + acad_annex_w1_w2[0].total_w2)
        else:
            response['show'] = 0

    return redirect('/academic')

@login_required(login_url='/register')
def annexure_x_main(request):
    response = {}
    app_id = Appdata.objects.get(user=request.user)

    if app_id.submitted :
        return redirect('/printSummary')

    acad_annex_x = Acad_Annex_X.objects.filter(app_id=app_id)

    if request.method == "POST":
        response['show'] = 1
        if acad_annex_x.count() == 0:
            acad_annex_x = Acad_Annex_X()
            acad_annex_x.app_id = app_id
        else:
            acad_annex_x = acad_annex_x[0]
        acad_annex_x.total_number = request.POST['total_numberx']
        acad_annex_x.credit_val = request.POST['credits_20']
        acad_annex_x.save()
        response['acad_annex_x'] = acad_annex_x
    else:
        if acad_annex_x.count() > 0:
            response['show'] = 1
            response['acad_annex_x'] = acad_annex_x[0]
        else:
            response['show'] = 0

    return redirect('/academic')

@login_required(login_url='/register')
def annexure_y_main(request):
    response = {}
    app_id = Appdata.objects.get(user=request.user)

    if app_id.submitted :
        return redirect('/printSummary')

    acad_annex_y = Acad_Annex_Y.objects.filter(app_id=app_id)

    if request.method == "POST":
        response['show'] = 1
        if acad_annex_y.count() == 0:
            acad_annex_y = Acad_Annex_Y()
            acad_annex_y.app_id = app_id
        else:
            acad_annex_y = acad_annex_y[0]
        acad_annex_y.value = request.POST['valueyon']
        acad_annex_y.credit_val = request.POST['credits_21']
        acad_annex_y.save()
        response['acad_annex_y'] = acad_annex_y
    else:
        if acad_annex_y.count() > 0:
            response['show'] = 1
            response['acad_annex_y'] = acad_annex_y[0]
        else:
            response['show'] = 0

    return redirect('/academic')

@login_required(login_url='/register')
def annexure_z_main(request):
    response = {}
    app_id = Appdata.objects.get(user=request.user)

    if app_id.submitted :
        return redirect('/printSummary')

    acad_annex_z = Acad_Annex_Z.objects.filter(app_id=app_id)

    if request.method == "POST":
        response['show'] = 1
        if acad_annex_z.count() == 0:
            acad_annex_z = Acad_Annex_Z()
            acad_annex_z.app_id = app_id
        else:
            acad_annex_z = acad_annex_z[0]
        acad_annex_z.percentage = request.POST['percentagez']
        acad_annex_z.credit_val = request.POST['credits_22']
        acad_annex_z.save()
        response['acad_annex_z'] = acad_annex_z
    else:
        if acad_annex_z.count() > 0:
            response['show'] = 1
            response['acad_annex_z'] = acad_annex_z[0]
        else:
            response['show'] = 0

    return redirect('/academic')



@login_required(login_url='/register')
def academic(request, flag=0):

    response = {}
    app_id = Appdata.objects.get(user=request.user)
    if app_id.submitted and flag == 0:
        return redirect('/printSummary')
    # app_id = Appdata.objects.get(post_for='123')
    external_sponsored_rnd = External_Sponsored_RnD.objects.filter(app_id=app_id)
    consultancy_projects = Consultancy_Projects.objects.filter(app_id=app_id)
    phd_completed = PhD_Completed.objects.filter(app_id=app_id)
    journal_papers = Journal_Papers.objects.filter(app_id = app_id)
    conference_paper_sci = Conference_Paper_SCI.objects.filter(app_id = app_id)


    acad_annex_a = Acad_Annex_A.objects.filter(app_id=app_id)
    acad_annex_b = Acad_Annex_B.objects.filter(app_id=app_id)
    acad_annex_c = Acad_Annex_C.objects.filter(app_id=app_id)
    acad_annex_d = Acad_Annex_D.objects.filter(app_id=app_id)
    acad_annex_e12 = Acad_Annex_E12.objects.filter(app_id=app_id)
    acad_annex_f = Acad_Annex_F.objects.filter(app_id=app_id)
    acad_annex_g = Acad_Annex_G.objects.filter(app_id=app_id)
    acad_annex_h = Acad_Annex_H.objects.filter(app_id=app_id)
    acad_annex_i = Acad_Annex_I.objects.filter(app_id=app_id)
    acad_annex_j = Acad_Annex_J.objects.filter(app_id=app_id)
    acad_annex_k = Acad_Annex_K.objects.filter(app_id=app_id)
    acad_annex_l = Acad_Annex_L.objects.filter(app_id=app_id)
    acad_annex_m = Acad_Annex_M.objects.filter(app_id=app_id)
    acad_annex_n = Acad_Annex_N.objects.filter(app_id=app_id)
    acad_annex_o = Acad_Annex_O.objects.filter(app_id=app_id)
    acad_annex_p = Acad_Annex_P.objects.filter(app_id=app_id)
    acad_annex_q = Acad_Annex_Q.objects.filter(app_id=app_id)
    acad_annex_r = Acad_Annex_R.objects.filter(app_id=app_id)
    acad_annex_s = Acad_Annex_S.objects.filter(app_id=app_id)
    acad_annex_t = Acad_Annex_T.objects.filter(app_id=app_id)
    acad_annex_u = Acad_Annex_U.objects.filter(app_id=app_id)
    acad_annex_v = Acad_Annex_V.objects.filter(app_id=app_id)
    acad_annex_w1_w2 = Acad_Annex_W1_W2.objects.filter(app_id=app_id)
    acad_annex_x = Acad_Annex_X.objects.filter(app_id=app_id)
    acad_annex_y = Acad_Annex_Y.objects.filter(app_id=app_id)
    acad_annex_z = Acad_Annex_Z.objects.filter(app_id=app_id)

    if request.method == "POST":
        if external_sponsored_rnd.count() == 0:
            external_sponsored_rnd = External_Sponsored_RnD()
            external_sponsored_rnd.app_id = app_id
            external_sponsored_rnd.projects_not_pi = request.POST['projects_not_pi']
            external_sponsored_rnd.patents_not_pi = request.POST['patents_not_pi']
            external_sponsored_rnd.save()
        else:
            external_sponsored_rnd = external_sponsored_rnd[0]
        external_sponsored_rnd.total_projects = request.POST['total_projects']
        external_sponsored_rnd.project_as_PI = request.POST['projects_as_PI']
        external_sponsored_rnd.total_patents = request.POST['total_patents']
        external_sponsored_rnd.patents_as_pi = request.POST['patents_as_pi']
        external_sponsored_rnd.credit_val = request.POST['credits_1']
        # external_sponsored_rnd.patents_not_pi = request.POST['patents_not_pi']
        # if len(request.POST['projects_not_pi'])>2:
        #     oldstr = external_sponsored_rnd.projects_not_pi
        #     newstr = request.POST['projects_not_pi']
        #     external_sponsored_rnd.projects_not_pi = oldstr[:-1] + "," + newstr[1:]

        if len(request.POST['projects_not_pi'])>2:
            oldstr = external_sponsored_rnd.projects_not_pi
            newstr = request.POST['projects_not_pi']
            if oldstr == '[]':
                external_sponsored_rnd.projects_not_pi = "[" + newstr[1:]
            else:
                external_sponsored_rnd.projects_not_pi = oldstr[:-1] + "," + newstr[1:]
        
        # if len(request.POST['patents_not_pi'])>2:
        #     oldstr = external_sponsored_rnd.patents_not_pi
        #     newstr = request.POST['patents_not_pi']
        #     external_sponsored_rnd.patents_not_pi = oldstr[:-1] + "," + newstr[1:]
        if len(request.POST['patents_not_pi'])>2:
            oldstr = external_sponsored_rnd.patents_not_pi
            newstr = request.POST['patents_not_pi']
            if oldstr == '[]':
                external_sponsored_rnd.patents_not_pi = "[" + newstr[1:]
            else:
                external_sponsored_rnd.patents_not_pi = oldstr[:-1] + "," + newstr[1:]

        external_sponsored_rnd.save()

        response['external_sponsored_rnd'] = external_sponsored_rnd

        if external_sponsored_rnd.projects_not_pi:
            response['projects_not_pi'] = json.loads(external_sponsored_rnd.projects_not_pi)
        if external_sponsored_rnd.patents_not_pi:
            response['patents_not_pi'] = json.loads(external_sponsored_rnd.patents_not_pi)

        if consultancy_projects.count() == 0:
            consultancy_projects = Consultancy_Projects()
            consultancy_projects.app_id = app_id
        else:
            consultancy_projects = consultancy_projects[0]
        consultancy_projects.consultancy_projects_completed = request.POST['consultancy_projects_completed']
        consultancy_projects.amount = request.POST['amount']
        consultancy_projects.credit_val = request.POST['credits_2']
        consultancy_projects.save()
        response['consultancy_projects'] = consultancy_projects

        if phd_completed.count() == 0:
            phd_completed = PhD_Completed()
            phd_completed.app_id = app_id
            phd_completed.phds = request.POST['phds']
            phd_completed.save()
        else:
            phd_completed = phd_completed[0]
        phd_completed.total_phd = request.POST['total_phd']
        phd_completed.credit_val = request.POST['credits_3']
        phd_completed.as_first_supervisor = request.POST['as_first_supervisor_phd']
        if len(request.POST['phds'])>2:
            oldstr = phd_completed.phds
            newstr = request.POST['phds']
            if oldstr == "[]":
                phd_completed.phds = "[" + newstr[1:]
            else:
                phd_completed.phds = oldstr[:-1] + "," + newstr[1:]
        phd_completed.save()
        response['phd_completed'] = phd_completed
        if phd_completed.phds:
            response['phds'] = json.loads(phd_completed.phds)

        if journal_papers.count() == 0:
            journal_papers = Journal_Papers()
            journal_papers.app_id = app_id
            journal_papers.papers = request.POST['papers']
            journal_papers.save()
        else:
            journal_papers = journal_papers[0]
        journal_papers.total_journal_papers = request.POST['total_journal_papers']
        journal_papers.as_first_supervisor = request.POST['as_first_supervisor_journal']
        journal_papers.credit_val = request.POST['credits_4']
        if len(request.POST['papers'])>2:
            oldstr = journal_papers.papers
            newstr = request.POST['papers']
            if oldstr == "[]":
                journal_papers.papers = "[" + newstr[1:]
            else:
                journal_papers.papers = oldstr[:-1] + "," + newstr[1:]

        journal_papers.save()
        response['journal_papers'] = journal_papers
        if journal_papers.papers:
            response['papers'] = json.loads(journal_papers.papers)

        if conference_paper_sci.count() == 0:
            conference_paper_sci = Conference_Paper_SCI()
            conference_paper_sci.app_id = app_id
            conference_paper_sci.papers = request.POST['papers1']
            conference_paper_sci.save()
        else:
            conference_paper_sci = conference_paper_sci[0]
        conference_paper_sci.total_confernce_papers = request.POST['total_confernce_papers']
        conference_paper_sci.as_first_supervisor = request.POST['as_first_supervisor_conference']
        conference_paper_sci.credit_val = request.POST['credits_5']
        if len(request.POST['papers1'])>2:
            oldstr = journal_papers.papers
            newstr = request.POST['papers1']
            if oldstr == "[]":
                conference_paper_sci.papers = "[" + newstr[1:]
            else:
                conference_paper_sci.papers = oldstr[:-1] + "," + newstr[1:]

        conference_paper_sci.save()
        response['conference_paper_sci'] = conference_paper_sci
        if conference_paper_sci.papers:
            response['papers1'] = json.loads(conference_paper_sci.papers)

        if acad_annex_j.count() == 0:
            acad_annex_j = Acad_Annex_J()
            acad_annex_j.app_id = app_id
        else:
            acad_annex_j = acad_annex_j[0]
        acad_annex_j.total_sem = request.POST['total_semj']
        acad_annex_j.credit_val = request.POST['credits_6']
        acad_annex_j.save()
        response['acad_annex_j'] = acad_annex_j

        if acad_annex_k.count() == 0:
            acad_annex_k = Acad_Annex_K()
            acad_annex_k.app_id = app_id
        else:
            acad_annex_k = acad_annex_k[0]
        acad_annex_k.total_sem = request.POST['total_semk']
        acad_annex_k.credit_val = request.POST['credits_7']
        acad_annex_k.save()
        response['acad_annex_k'] = acad_annex_k

        if acad_annex_l.count() == 0:
            acad_annex_l = Acad_Annex_L()
            acad_annex_l.app_id = app_id
        else:
            acad_annex_l = acad_annex_l[0]
        acad_annex_l.total_sem = request.POST['total_seml']
        acad_annex_l.credit_val = request.POST['credits_8']
        acad_annex_l.save()
        response['acad_annex_l'] = acad_annex_l

        if acad_annex_m.count() == 0:
            acad_annex_m = Acad_Annex_M()
            acad_annex_m.app_id = app_id
        else:
            acad_annex_m = acad_annex_m[0]
        acad_annex_m.total_sem = request.POST['total_semm']
        acad_annex_m.credit_val = request.POST['credits_9']
        acad_annex_m.save()
        response['acad_annex_m'] = acad_annex_m

        if acad_annex_n.count() == 0:
            acad_annex_n = Acad_Annex_N()
            acad_annex_n.app_id = app_id
        else:
            acad_annex_n = acad_annex_n[0]
        acad_annex_n.total_number = request.POST['total_numbern']
        acad_annex_n.credit_val = request.POST['credits_10']
        acad_annex_n.save()
        response['acad_annex_n'] = acad_annex_n

        if acad_annex_o.count() == 0:
            acad_annex_o = Acad_Annex_O()
            acad_annex_o.app_id = app_id
        else:
            acad_annex_o = acad_annex_o[0]
        acad_annex_o.prog_2_week_duration = request.POST['prog_2_week_duration']
        acad_annex_o.prog_1_week_duration = request.POST['prog_1_week_duration']
        acad_annex_o.credit_val = request.POST['credits_11']
        acad_annex_o.save()
        response['acad_annex_o'] = acad_annex_o

        if acad_annex_p.count() == 0:
            acad_annex_p = Acad_Annex_P()
            acad_annex_p.app_id = app_id
        else:
            acad_annex_p = acad_annex_p[0]
        acad_annex_p.total_number = request.POST['total_numberp']
        acad_annex_p.credit_val = request.POST['credits_12']
        acad_annex_p.save()
        response['acad_annex_p'] = acad_annex_p

        if acad_annex_q.count() == 0:
            acad_annex_q = Acad_Annex_Q()
            acad_annex_q.app_id = app_id
        else:
            acad_annex_q = acad_annex_q[0]
        acad_annex_q.total_years = request.POST['total_years']
        acad_annex_q.total_months = request.POST['total_months']
        acad_annex_q.credit_val = request.POST['credits_13']
        acad_annex_q.save()
        response['acad_annex_q'] = acad_annex_q

        if acad_annex_r.count() == 0:
            acad_annex_r = Acad_Annex_R()
            acad_annex_r.app_id = app_id
        else:
            acad_annex_r = acad_annex_r[0]
        acad_annex_r.total_number = request.POST['total_numberr']
        acad_annex_r.credit_val = request.POST['credits_14']
        acad_annex_r.save()
        response['acad_annex_r'] = acad_annex_r

        if acad_annex_s.count() == 0:
            acad_annex_s = Acad_Annex_S()
            acad_annex_s.app_id = app_id
        else:
            acad_annex_s = acad_annex_s[0]
        acad_annex_s.total_credit = request.POST['total_creditss']
        acad_annex_s.credit_val = request.POST['credits_15']
        acad_annex_s.save()
        response['acad_annex_s'] = acad_annex_s

        if acad_annex_t.count() == 0:
            acad_annex_t = Acad_Annex_T()
            acad_annex_t.app_id = app_id
        else:
            acad_annex_t = acad_annex_t[0]
        acad_annex_t.total_number = request.POST['total_numbert']
        acad_annex_t.credit_val = request.POST['credits_16']
        acad_annex_t.save()
        response['acad_annex_t'] = acad_annex_t

        if acad_annex_u.count() == 0:
            acad_annex_u = Acad_Annex_U()
            acad_annex_u.app_id = app_id
        else:
            acad_annex_u = acad_annex_u[0]
        acad_annex_u.total_number = request.POST['total_numberu']
        acad_annex_u.credit_val = request.POST['credits_17']
        acad_annex_u.save()
        response['acad_annex_u'] = acad_annex_u

        if acad_annex_v.count() == 0:
            acad_annex_v = Acad_Annex_V()
            acad_annex_v.app_id = app_id
        else:
            acad_annex_v = acad_annex_v[0]
        acad_annex_v.total_number = request.POST['total_numberv']
        acad_annex_v.credit_val = request.POST['credits_18']
        acad_annex_v.save()
        response['acad_annex_v'] = acad_annex_v

        if acad_annex_w1_w2.count() == 0:
            acad_annex_w1_w2 = Acad_Annex_W1_W2()
            acad_annex_w1_w2.app_id = app_id
        else:
            acad_annex_w1_w2 = acad_annex_w1_w2[0]
        acad_annex_w1_w2.total_number = request.POST['total_numberw1_w2']
        acad_annex_w1_w2.credit_val = request.POST['credits_19']
        acad_annex_w1_w2.save()
        response['acad_annex_w1_w2'] = acad_annex_w1_w2

        if acad_annex_x.count() == 0:
            acad_annex_x = Acad_Annex_X()
            acad_annex_x.app_id = app_id
        else:
            acad_annex_x = acad_annex_x[0]
        acad_annex_x.total_number = request.POST['total_numberx']
        acad_annex_x.credit_val = request.POST['credits_20']
        acad_annex_x.save()
        response['acad_annex_x'] = acad_annex_x

        if acad_annex_y.count() == 0:
            acad_annex_y = Acad_Annex_Y()
            acad_annex_y.app_id = app_id
        else:
            acad_annex_y = acad_annex_y[0]
        acad_annex_y.value = request.POST['valueyon']
        acad_annex_y.credit_val = request.POST['credits_21']
        acad_annex_y.save()
        response['acad_annex_y'] = acad_annex_y

        if acad_annex_z.count() == 0:
            acad_annex_z = Acad_Annex_Z()
            acad_annex_z.app_id = app_id
        else:
            acad_annex_z = acad_annex_z[0]
        acad_annex_z.percentage = request.POST['percentagez']
        acad_annex_z.credit_val = request.POST['credits_22']
        acad_annex_z.save()
        response['acad_annex_z'] = acad_annex_z
	
	return redirect('/academic')	

        return redirect('/academic')

    else:
        if external_sponsored_rnd.count() > 0:
            response['external_sponsored_rnd'] = external_sponsored_rnd[0]
            if external_sponsored_rnd[0].projects_not_pi:
                response['projects_not_pi'] = json.loads(external_sponsored_rnd[0].projects_not_pi)
            if external_sponsored_rnd[0].patents_not_pi:
                response['patents_not_pi'] = json.loads(external_sponsored_rnd[0].patents_not_pi)

        if consultancy_projects.count() > 0:
            response['consultancy_projects'] = consultancy_projects[0]

        if phd_completed.count() > 0:
            response['phd_completed'] = phd_completed[0]
            if phd_completed[0].phds:
                response['phds'] = json.loads(phd_completed[0].phds)
            
        if journal_papers.count() > 0:
            response['journal_papers'] = journal_papers[0]
            if journal_papers[0].papers:
                response['papers'] = json.loads(journal_papers[0].papers)
            
        if conference_paper_sci.count() > 0:
            response['conference_paper_sci'] = conference_paper_sci[0]
            if conference_paper_sci[0].papers:
                response['papers1'] = json.loads(conference_paper_sci[0].papers)
            
        if acad_annex_a.count() > 0:
            response['acad_annex_a'] = acad_annex_a[0]

        if acad_annex_b.count() > 0:
            response['acad_annex_b'] = acad_annex_b[0]
        if acad_annex_c.count() > 0:
            response['acad_annex_c'] = acad_annex_c[0]

        if acad_annex_d.count() > 0:
            response['acad_annex_d'] = acad_annex_d[0]

        if acad_annex_e12.count() > 0:
            response['acad_annex_e12'] = acad_annex_e12[0]
            response['total_e'] = float(acad_annex_e12[0].total_e1 + acad_annex_e12[0].total_e2)

        if acad_annex_f.count() > 0:
            response['acad_annex_f'] = acad_annex_f[0]

        if acad_annex_g.count() > 0:
            response['acad_annex_g'] = acad_annex_g[0]

        if acad_annex_h.count() > 0:
            response['acad_annex_h'] = acad_annex_h[0]

        if acad_annex_i.count() > 0:
            response['acad_annex_i'] = acad_annex_i[0]

        if acad_annex_j.count() > 0:
            response['acad_annex_j'] = acad_annex_j[0]

        if acad_annex_k.count() > 0:
            response['acad_annex_k'] = acad_annex_k[0]

        if acad_annex_l.count() > 0:
            response['acad_annex_l'] = acad_annex_l[0]

        if acad_annex_m.count() > 0:
            response['acad_annex_m'] = acad_annex_m[0]

        if acad_annex_n.count() > 0:
            response['acad_annex_n'] = acad_annex_n[0]

        if acad_annex_o.count() > 0:
            response['acad_annex_o'] = acad_annex_o[0]

        if acad_annex_p.count() > 0:
            response['acad_annex_p'] = acad_annex_p[0]

        if acad_annex_q.count() > 0:
            response['acad_annex_q'] = acad_annex_q[0]  

        if acad_annex_r.count() > 0:
            response['acad_annex_r'] = acad_annex_r[0]

        if acad_annex_s.count() > 0:
            response['acad_annex_s'] = acad_annex_s[0]

        if acad_annex_t.count() > 0:
            response['acad_annex_t'] = acad_annex_t[0]

        if acad_annex_u.count() > 0:
            response['acad_annex_u'] = acad_annex_u[0]

        if acad_annex_v.count() > 0:
            response['acad_annex_v'] = acad_annex_v[0]

        if acad_annex_w1_w2.count() > 0:
            response['acad_annex_w1_w2'] = acad_annex_w1_w2[0]
            response['total_w'] = float(acad_annex_w1_w2[0].total_w1 + acad_annex_w1_w2[0].total_w2)

        if acad_annex_x.count() > 0:
            response['acad_annex_x'] = acad_annex_x[0]

        if acad_annex_y.count() > 0:
            response['acad_annex_y'] = acad_annex_y[0]

        if acad_annex_z.count() > 0:
            response['acad_annex_z'] = acad_annex_z[0]

    return render(request, 'recruit/acad_other_req.djt', response)


@login_required(login_url='/register')
def annexure_a(request):
    response = {}
    app_data = Appdata.objects.get(user = request.user)
    print app_data
    if(request.POST):
        print request.POST
        try:
            annexure = Acad_Annex_A.objects.get(app_id=app_data)
            if len(request.POST['annexure_a'])>2:
                oldstr = annexure.annexure_data
                newstr = request.POST['annexure_a']
                if oldstr == " " or oldstr=="[]" or len(oldstr) == 0:
                    annexure.annexure_data = "[" + newstr[1:]
                else:
                    annexure.annexure_data = oldstr[:-1] + "," + newstr[1:]
            annexure.total = 0
            annexure.store = True
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()
            print "puranaA"
        except ObjectDoesNotExist:
            annexure = Acad_Annex_A()
            annexure.app_id = Appdata.objects.get(app_id = app_data)
            annexure.annexure_data = request.POST['annexure_a']
            annexure.total = 0
            annexure.store = True
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()
            print annexure
        print "redirecting"
        return redirect('/educationalqual')
    annex_a = Acad_Annex_A.objects.filter(app_id=app_data)
    if annex_a.count() > 0:
        if len(unicodedata.normalize("NFKD",annex_a[0].annexure_data)) > 1:
            response['annex_a'] = json.loads(annex_a[0].annexure_data)
        response['annexure_file'] = annex_a[0].annexure_file
    return render(request,'recruit/annexure/annexure_a.djt',response)

@login_required(login_url='/register')
def annexure_b(request) :
    response = {}
    app_data = Appdata.objects.get(user = request.user)
    print app_data
    if(request.POST):
        print request.POST
        try:
            annexure = Acad_Annex_B.objects.get(app_id=app_data)
            annexure.annexure_data = request.POST['annexure_b']
            annexure.total = float(request.POST.get('total',0));
            annexure.store = True
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()
        except ObjectDoesNotExist:
            annexure = Acad_Annex_B()
            annexure.app_id = Appdata.objects.get(app_id = app_data)
            annexure.annexure_data = request.POST['annexure_b']
            annexure.total = float(request.POST.get('total',0));
            annexure.store = True
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()
        return redirect('/academic')
        annex_b = Acad_Annex_B.objects.filter(app_id=app_data)
        response= {}
        response['annexure_file'] = annex_b[0].annexure_file
    return render(request,'recruit/annexure/annexure-b.djt',response)

@login_required(login_url='/register')
def annexure_c(request) :
    response = {}
    app_data = Appdata.objects.get(user = request.user)
    print app_data
    if(request.POST):
        print request.POST
        try:
            annexure = Acad_Annex_C.objects.get(app_id=app_data)
            annexure.annexure_data = request.POST['annexure_c']
            annexure.total = float(request.POST.get('total',0));
            annexure.store = True
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()
        except ObjectDoesNotExist:
            annexure = Acad_Annex_C()
            annexure.app_id = Appdata.objects.get(app_id = app_data)
            annexure.annexure_data = request.POST['annexure_c']
            annexure.total = float(request.POST.get('total',0));
            annexure.store = True
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()
        return redirect('/academic')
        annex_c = Acad_Annex_C.objects.filter(app_id=app_data)
        response= {}
        response['annexure_file'] = annex_c[0].annexure_file
    return render(request,'recruit/annexure/annexure-c.djt',response)


@login_required(login_url='/register')
def annexure_d(request) :
    response= {}
    app_data = Appdata.objects.get(user = request.user)
    if(request.POST):
        try:
            annexure = Acad_Annex_D.objects.get(app_id=app_data)
            if(request.POST['basic_pay']):
                annexure.basic_pay_r = request.POST['basic_pay']
                annexure.payband_r = request.POST['payband']
                annexure.payband_end_r = request.POST['payband_b']
                annexure.total_r = request.POST['total_a']
            annexure.store = True
            if(request.POST['basic_pay_d']):
                annexure.basic_pay_d = request.POST['basic_pay_d']
                annexure.payband_d = request.POST['payband_d']
                annexure.payband_end_d = request.POST['payband_b_d']
                annexure.total_d = request.POST['total_ad']
            annexure.total = (request.POST.get('total',0));
            annexure.store = True
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()
        except ObjectDoesNotExist:
            annexure = Acad_Annex_D()
            annexure.app_id = Appdata.objects.get(app_id = app_data)
            if(request.POST['basic_pay']):
                annexure.basic_pay_r = request.POST['basic_pay']
                annexure.payband_r = request.POST['payband']
                annexure.payband_end_r = request.POST['payband_b']
                annexure.total_r = request.POST['total_a']
                annexure.store = True
            elif(request.POST['basic_pay_d']):
                annexure.basic_pay_d = request.POST['basic_pay_d']
                annexure.payband_d = request.POST['payband_d']
                annexure.payband_end_d = request.POST['payband_b_d']
                annexure.total_d = request.POST['total_ad']
            annexure.total = (request.POST.get('total',0));
            annexure.store = True
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()
        return redirect('/academic')
        annex_d = Acad_Annex_D.objects.filter(app_id=app_data)
        response['annexure_file'] = annex_d[0].annexure_file
    return render(request,'recruit/annexure/annexure_d.djt',response)

@login_required(login_url='/register')
def annexure_e_1(request) :
    response = {}
    app_data = Appdata.objects.get(user = request.user)
    if(request.POST):
        try:
            annexure = Acad_Annex_E12.objects.get(app_id=app_data)
            if len(request.POST['annexure_e1'])>2:
                oldstr = annexure.annexure_data_e1
                newstr = request.POST['annexure_e1']
                if oldstr == " " or oldstr=="[]":
                    annexure.annexure_data_e1 = "[" + newstr[1:]
                else:
                    annexure.annexure_data_e1 = oldstr[:-1] + "," + newstr[1:]
            annexure.store_e1 = True
            annexure.total_e1 = float(request.POST.get('total_e1',0));
            # annexure.total_e1 = request.POST['total_e1']
            if request.FILES:
                annexure.annexure_file_e1 = request.FILES['annexure_file']
            annexure.save()
        except ObjectDoesNotExist:
            annexure = Acad_Annex_E12()
            annexure.app_id = Appdata.objects.get(app_id = app_data)
            annexure.annexure_data_e1 = request.POST['annexure_e1']
            annexure.total_e1 = float(request.POST.get('total_e1',0))
            annexure.store_e1 = True
            if request.FILES:
                annexure.annexure_file_e1 = request.FILES['annexure_file']
            annexure.save()
            annexure.total_e1 = annexure.total_e1+float(request.POST.get('total_e1',0));
        return redirect('/academic')
    annex_e1 = Acad_Annex_E12.objects.filter(app_id=app_data)
    if annex_e1.count() > 0:
        if len(unicodedata.normalize("NFKD",annex_e1[0].annexure_data_e1)) > 1:
            response['annex_e1'] = json.loads(annex_e1[0].annexure_data_e1)
            response['total_e1'] = annex_e1[0].total_e1;
            response['annexure_file'] = annex_e1[0].annexure_file_e1
    return render(request,'recruit/annexure/annexure-e-1.djt',response)

@login_required(login_url='/register')
def annexure_e2(request):
    app_data = Appdata.objects.get(user = request.user)
    response = {}
    if(request.POST):
        try:
            annexure = Acad_Annex_E12.objects.get(app_id=app_data)
            if len(request.POST['annexure_e2'])>2:
                oldstr = annexure.annexure_data_e2
                newstr = request.POST['annexure_e2']
                if oldstr == " " or oldstr == "[]":
                    annexure.annexure_data_e2 = "[" + newstr[1:]
                else:
                    annexure.annexure_data_e2 = oldstr[:-1] + "," + newstr[1:]
            # annexure.total_e2 = request.POST['total_e2']
            annexure.store_e2 = True
            annexure.total_e2 = float(request.POST.get('total_e2',0));
            if request.FILES:
                annexure.annexure_file_e2 = request.FILES['annexure_file']
            annexure.save()
        except ObjectDoesNotExist:
            annexure = Acad_Annex_E12()
            annexure.app_id = Appdata.objects.get(app_id = app_data)
            annexure.annexure_data_e2 = request.POST['annexure_e2']
            annexure.total_e2 = request.POST['total_e2']
            annexure.store_e2 = True
            #annexure.total_e2 = annexure.total_e2+float(request.POST.get('total_e2',0));
            if request.FILES:
                annexure.annexure_file_e2 = request.FILES['annexure_file']
            annexure.save()
        return redirect('/academic')
    annex_e2 = Acad_Annex_E12.objects.filter(app_id=app_data)
    if annex_e2.count() > 0:
        if len(str((annex_e2[0].annexure_data_e2).encode("utf-8"))) > 1:
            response['annex_e2'] = json.loads(annex_e2[0].annexure_data_e2)
            response['total_e2'] = annex_e2[0].total_e2;
            response['annexure_file'] = annex_e2[0].annexure_file_e2
    return render(request,'recruit/annexure/annexure_e2.djt',response)

@login_required(login_url='/register')
def annexure_f(request):
    response = {}
    app_data = Appdata.objects.get(user = request.user)
    if(request.POST):
        try:
            annexure = Acad_Annex_F.objects.get(app_id=app_data)
            annexure.annexure_data = getValue(request, annexure, 'annexure_f')
            annexure.store = True
            annexure.credit_score = float(request.POST['credit'])
            annexure.total = float(request.POST.get('total',0));
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()
        except ObjectDoesNotExist:
            annexure = Acad_Annex_F()
            annexure.app_id = Appdata.objects.get(app_id = app_data)
            annexure.annexure_data = request.POST['annexure_f']
            annexure.store = True
            annexure.credit_score = float(request.POST['credit'])
            annexure.total = annexure.total+float(request.POST.get('total',0));
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()
        return redirect('/academic')
    annex_f = Acad_Annex_F.objects.filter(app_id=app_data)
    if annex_f.count() > 0:
        if annex_f[0].annexure_data:
            response['annex_f'] = json.loads(annex_f[0].annexure_data)
            response['credit'] = annex_f[0].credit_score
            response['total'] = annex_f[0].total
            response['annexure_file'] = annex_f[0].annexure_file
    return render(request,'recruit/annexure/annexure_f.djt',response)

@login_required(login_url='/register')
def annexure_g(request):
    response = {}
    app_data = Appdata.objects.get(user = request.user)
    if(request.POST):
        try:
            annexure = Acad_Annex_G.objects.get(app_id=app_data)
            annexure.annexure_data = getValue(request, annexure, 'annexure_g')
            annexure.total = float(request.POST.get('total',0));
            annexure.store = True
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()
        except ObjectDoesNotExist:
            annexure = Acad_Annex_G()
            annexure.app_id = Appdata.objects.get(app_id = app_data)
            annexure.annexure_data = request.POST['annexure_g']
            annexure.total = annexure.total+float(request.POST.get('total',0));
            annexure.store = True
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()
        return redirect('/academic')
    annex_g = Acad_Annex_G.objects.filter(app_id=app_data)
    if annex_g.count() > 0:
        if annex_g[0].annexure_data:
            response['annex_g'] = json.loads(annex_g[0].annexure_data)
            response['total'] = annex_g[0].total
            response['annexure_file'] = annex_g[0].annexure_file
    return render(request,'recruit/annexure/annexure_g.djt',response)

@login_required(login_url='/register')
def annexure_h(request):
    response = {}
    app_data = Appdata.objects.get(user = request.user)
    print app_data
    if(request.POST):
        print request.POST
        try:
            annexure = Acad_Annex_H.objects.get(app_id=app_data)
            annexure.annexure_data = getValue(request, annexure, 'annexure_h')
            annexure.last_prom = request.POST['last_prom']
            annexure.total = float(request.POST.get('total',0));
            annexure.store = True
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()
        except ObjectDoesNotExist:
            annexure = Acad_Annex_H()
            annexure.app_id = Appdata.objects.get(app_id = app_data)
            annexure.annexure_data = request.POST['annexure_h']
            annexure.last_prom = request.POST['last_prom']
            annexure.total = annexure.total+float(request.POST.get('total',0));
            annexure.store = True
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()
        return redirect('/academic')
    annex_h = Acad_Annex_H.objects.filter(app_id=app_data)
    if annex_h.count() > 0:
        if annex_h[0].annexure_data:
            response['annex_h'] = json.loads(annex_h[0].annexure_data)
            response['last_prom'] = annex_h[0].last_prom
            response['total'] = annex_h[0].total
            response['annexure_file'] = annex_h[0].annexure_file
    return render(request,'recruit/annexure/annexure_h.djt',response)

@login_required(login_url='/register')
def annexure_i(request):
    response = {}
    app_data = Appdata.objects.get(user = request.user)
    print app_data
    if(request.POST):
        print request.POST
        try:
            annexure = Acad_Annex_I.objects.get(app_id=app_data)
            annexure.annexure_data = getValue(request, annexure, 'annexure_i')
            annexure.total = float(request.POST.get('total',0));
            annexure.store = True
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()
        except ObjectDoesNotExist:
            annexure = Acad_Annex_I()
            annexure.app_id = Appdata.objects.get(app_id = app_data)
            annexure.annexure_data = request.POST['annexure_i']
            annexure.total = annexure.total+float(request.POST.get('total',0));
            annexure.store = True
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()
        return redirect('/academic')
    annex_i = Acad_Annex_I.objects.filter(app_id=app_data)
    if annex_i.count() > 0:
        if annex_i[0].annexure_data:
            response['annex_i'] = json.loads(annex_i[0].annexure_data)
            response['total'] = annex_i[0].total
            response['annexure_file'] = annex_i[0].annexure_file
    return render(request,'recruit/annexure/annexure_i.djt',response)

@login_required(login_url='/register')
def annexure_j(request):
    response = {}
    app_data = Appdata.objects.get(user = request.user)
    print app_data
    if(request.POST):
        print request.POST
        try:
            annexure = Acad_Annex_J.objects.get(app_id=app_data)
            annexure.annexure_data = getValue(request, annexure, 'annexure_j')
            annexure.store = True
            annexure.credit_score = float(request.POST.get('credit',0));
            annexure.total = float(request.POST.get('total',0));
            annexure.last_prom = request.POST['last_prom']
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()
        except ObjectDoesNotExist:
            annexure = Acad_Annex_J()
            annexure.app_id = Appdata.objects.get(app_id = app_data)
            annexure.annexure_data = request.POST['annexure_j']
            annexure.store = True
            annexure.credit_score = float(request.POST.get('credit',0));
            annexure.total = annexure.total+float(request.POST.get('total',0));
            annexure.last_prom = request.POST['last_prom']
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()
        return redirect('/academic')
    annex_j = Acad_Annex_J.objects.filter(app_id=app_data)
    if annex_j.count() > 0:
        if annex_j[0].annexure_data:
            response['annex_j'] = json.loads(annex_j[0].annexure_data)
            response['credit'] = annex_j[0].credit_score
            response['last_prom'] = annex_j[0].last_prom
            response['total'] = annex_j[0].total
            response['annexure_file'] = annex_j[0].annexure_file
    return render(request,'recruit/annexure/annexure_j.djt',response)

@login_required(login_url='/register')
def annexure_k(request):
    response = {}
    app_data = Appdata.objects.get(user = request.user)
    print app_data
    if(request.POST):
        try:
            annexure = Acad_Annex_K.objects.get(app_id=app_data)
            annexure.annexure_data = getValue(request, annexure, 'annexure_k')
            annexure.credit_score = float(request.POST.get('credit',0));
            annexure.last_prom = request.POST['last_prom']
            annexure.total = float(request.POST.get('total',0));
            annexure.store = True
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()
        except ObjectDoesNotExist:
            annexure = Acad_Annex_K()
            annexure.app_id = Appdata.objects.get(app_id = app_data)
            annexure.annexure_data = request.POST['annexure_k']
            annexure.credit_score = float(request.POST.get('credit',0));
            annexure.last_prom = request.POST['last_prom']
            annexure.total = annexure.total+float(request.POST.get('total',0));
            annexure.store = True
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()
        return redirect('/academic')
    annex_k = Acad_Annex_K.objects.filter(app_id=app_data)
    if annex_k.count() > 0:
        if annex_k[0].annexure_data:
            response['annex_k'] = json.loads(annex_k[0].annexure_data)
            response['credit'] = annex_k[0].credit_score
            response['last_prom'] = annex_k[0].last_prom
            response['total'] = annex_k[0].total
            response['annexure_file'] = annex_k[0].annexure_file
    return render(request,'recruit/annexure/annexure_k.djt',response)

@login_required(login_url='/register')
def annexure_l(request):
    response = {}
    app_data = Appdata.objects.get(user = request.user)
    print app_data
    if(request.POST):
        try:
            annexure = Acad_Annex_L.objects.get(app_id=app_data)
            annexure.annexure_data = getValue(request, annexure, 'annexure_l')
            annexure.credit_score = float(request.POST.get('credit',0));
            annexure.last_prom = request.POST['last_prom']
            annexure.total = float(request.POST.get('total',0));
            annexure.store = True
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()
        except ObjectDoesNotExist:
            annexure = Acad_Annex_L()
            annexure.app_id = Appdata.objects.get(app_id = app_data)
            annexure.annexure_data = request.POST['annexure_l']
            annexure.credit_score = float(request.POST.get('credit',0));
            annexure.last_prom = request.POST['last_prom']
            annexure.total = annexure.total+float(request.POST.get('total',0));
            annexure.store = True
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()
        return redirect('/academic')
    annex_l = Acad_Annex_L.objects.filter(app_id=app_data)
    if annex_l.count() > 0:
        if annex_l[0].annexure_data:
            response['annex_l'] = json.loads(annex_l[0].annexure_data)
            response['last_prom'] = annex_l[0].last_prom
            response['credit'] = annex_l[0].credit_score
            response['total'] = annex_l[0].total
            response['annexure_file'] = annex_l[0].annexure_file
    return render(request,'recruit/annexure/annexure_l.djt',response)

@login_required(login_url='/register')
def annexure_m(request):
    response = {}
    app_data = Appdata.objects.get(user = request.user)
    print app_data
    if(request.POST):
        print request.POST
        try:
            annexure = Acad_Annex_M.objects.get(app_id=app_data)
            annexure.annexure_data = getValue(request, annexure, 'annexure_m')
            annexure.credit_score = float(request.POST.get('credit',0));
            annexure.last_prom = request.POST['last_prom']
            annexure.total = float(request.POST.get('total',0));
            annexure.store = True
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()
        except ObjectDoesNotExist:
            annexure = Acad_Annex_M()
            annexure.app_id = Appdata.objects.get(app_id = app_data)
            annexure.annexure_data = request.POST['annexure_m']
            annexure.credit_score = float(request.POST.get('credit',0));
            annexure.last_prom = request.POST['last_prom']
            annexure.total = annexure.total+float(request.POST.get('total',0));
            annexure.store = True
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()
        return redirect('/academic')
    annex_m = Acad_Annex_M.objects.filter(app_id=app_data)
    if annex_m.count() > 0:
        if annex_m[0].annexure_data:
            response['annex_m'] = json.loads(annex_m[0].annexure_data)
            response['credit'] = annex_m[0].credit_score
            response['last_prom'] = annex_m[0].last_prom
            response['total'] = annex_m[0].total
            response['annexure_file'] = annex_m[0].annexure_file
    return render(request,'recruit/annexure/annexure_m.djt',response)

@login_required(login_url='/register')
def annexure_n(request):
    response = {}
    app_data = Appdata.objects.get(user = request.user)
    if(request.POST):
        try:
            annexure = Acad_Annex_N.objects.get(app_id=app_data)
            annexure.annexure_data = getValue(request, annexure, 'annexure_n')
            annexure.last_prom = request.POST['last_prom']
            annexure.total = float(request.POST.get('total',0));
            annexure.store = True
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()
        except ObjectDoesNotExist:
            annexure = Acad_Annex_N()
            annexure.app_id = Appdata.objects.get(app_id = app_data)
            annexure.annexure_data = request.POST['annexure_n']
            annexure.last_prom = request.POST['last_prom']
            annexure.total = annexure.total+float(request.POST.get('total',0));
            annexure.store = True
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()
        return redirect('/academic')
    annex_n = Acad_Annex_N.objects.filter(app_id=app_data)
    if annex_n.count() > 0:
        if annex_n[0].annexure_data:
            response['annex_n'] = json.loads(annex_n[0].annexure_data)
            response['last_prom'] = annex_n[0].last_prom
            response['total'] = annex_n[0].total
            response['annexure_file'] = annex_n[0].annexure_file
    return render(request,'recruit/annexure/annexure_n.djt',response)

@login_required(login_url='/register')
def annexure_o(request):
    response = {}
    app_data = Appdata.objects.get(user = request.user)
    print app_data
    if(request.POST):
        print request.POST
        try:
            annexure = Acad_Annex_O.objects.get(app_id=app_data)
            annexure.annexure_data = getValue(request, annexure, 'annexure_o')
            annexure.last_prom = request.POST['last_prom']
            annexure.total = float(request.POST.get('total',0));
            annexure.store = True
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()
        except ObjectDoesNotExist:
            annexure = Acad_Annex_O()
            annexure.app_id = Appdata.objects.get(app_id = app_data)
            annexure.annexure_data = request.POST['annexure_o']
            annexure.last_prom = request.POST['last_prom']
            annexure.total = annexure.total+float(request.POST.get('total',0));
            annexure.store = True
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()
        return redirect('/academic')
    annex_o = Acad_Annex_O.objects.filter(app_id=app_data)
    if annex_o.count() > 0:
        if annex_o[0].annexure_data:
            response['annex_o'] = json.loads(annex_o[0].annexure_data)
            response['last_prom'] = annex_o[0].last_prom
            response['total'] = annex_o[0].total
            response['annexure_file'] = annex_o[0].annexure_file
    return render(request,'recruit/annexure/annexure_o.djt',response)

@login_required(login_url='/register')
def annexure_p(request):
    response = {}
    app_data = Appdata.objects.get(user = request.user)
    print app_data
    if(request.POST):
        print request.POST
        try:
            annexure = Acad_Annex_P.objects.get(app_id=app_data)
            annexure.annexure_data = getValue(request, annexure, 'annexure_p')
            annexure.last_prom = request.POST['last_prom']
            annexure.total = float(request.POST.get('total',0));
            annexure.store = True
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()
        except ObjectDoesNotExist:
            annexure = Acad_Annex_P()
            annexure.app_id = Appdata.objects.get(app_id = app_data)
            annexure.annexure_data = request.POST['annexure_p']
            annexure.last_prom = request.POST['last_prom']
            annexure.total = annexure.total+float(request.POST.get('total',0));
            annexure.store = True
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()
        return redirect('/academic')
    annex_p = Acad_Annex_P.objects.filter(app_id=app_data)
    if annex_p.count() > 0:
        if annex_p[0].annexure_data:
            response['annex_p'] = json.loads(annex_p[0].annexure_data)
            response['last_prom'] = annex_p[0].last_prom
            response['total'] = annex_p[0].total
            response['annexure_file'] = annex_p[0].annexure_file
    return render(request,'recruit/annexure/annexure_p.djt',response)

@login_required(login_url='/register')
def annexure_q(request):
    response = {}
    app_data = Appdata.objects.get(user = request.user)
    print app_data
    if(request.POST):
        print request.POST
        try:
            annexure = Acad_Annex_Q.objects.get(app_id=app_data)
            annexure.annexure_data = getValue(request, annexure, 'annexure_q')
            annexure.last_prom = request.POST['last_prom']
            annexure.total_exp_after_phd = request.POST.get('exp_phd',0);
            annexure.total_exp_cur = request.POST.get('exp_cad',0);
            annexure.total_exp = float(request.POST.get('total',0));
            annexure.credit_score = float(request.POST.get('credit',0));
            annexure.total_yr = int(request.POST.get('total_yr',0));
            annexure.total_mnth = int(request.POST.get('total_mnth',0));
            annexure.store = True
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()
        except ObjectDoesNotExist:
            annexure = Acad_Annex_Q()
            annexure.app_id = Appdata.objects.get(app_id = app_data)
            annexure.annexure_data = request.POST['annexure_q']
            annexure.last_prom = request.POST['last_prom']
            annexure.total_exp_after_phd = request.POST.get('exp_phd',0);
            annexure.total_exp_cur = request.POST.get('exp_cad',0);
            annexure.total_exp = float(request.POST.get('total',0));
            annexure.credit_score = float(request.POST.get('credit',0));
            annexure.total_yr = annexure.total_yr+int(request.POST.get('total_yr',0));
            annexure.total_mnth = annexure.total_mnth+int(request.POST.get('total_mnth',0));
            annexure.store = True
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()
        return redirect('/academic')
    annex_q = Acad_Annex_Q.objects.filter(app_id=app_data)
    if annex_q.count() > 0:
        if annex_q[0].annexure_data:
            response['annex_q'] = json.loads(annex_q[0].annexure_data)
            response['last_prom'] = annex_q[0].last_prom
            response['exp_phd'] = annex_q[0].total_exp_after_phd
            response['exp_cur'] = annex_q[0].total_exp_cur
            response['tot_exp'] = annex_q[0].total_exp
            response['credit'] = annex_q[0].credit_score
            response['total_yr'] = annex_q[0].total_yr
            response['total_mnth'] = annex_q[0].total_mnth
            response['annexure_file'] = annex_q[0].annexure_file
    return render(request,'recruit/annexure/annexure_q.djt',response)

@login_required(login_url='/register')
def annexure_r(request):
    response = {}
    app_data = Appdata.objects.get(user = request.user)
    if(request.POST):
        print request.POST
        try:
            annexure = Acad_Annex_R.objects.get(app_id=app_data)
            annexure.annexure_data = getValue(request, annexure, 'annexure_r')
            annexure.last_prom = request.POST['last_prom']
            annexure.total = float(request.POST.get('total',0));
            annexure.store = True
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()
        except ObjectDoesNotExist:
            annexure = Acad_Annex_R()
            annexure.app_id = Appdata.objects.get(app_id = app_data)
            annexure.annexure_data = request.POST['annexure_r']
            annexure.last_prom = request.POST['last_prom']
            annexure.total = float(request.POST.get('total',0));
            annexure.store = True
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()
        return redirect('/academic')
    annex_r = Acad_Annex_R.objects.filter(app_id=app_data)
    if annex_r.count() > 0:
        if annex_r[0].annexure_data:
            response['annex_r'] = json.loads(annex_r[0].annexure_data)
            response['last_prom'] = annex_r[0].last_prom
            response['total'] = annex_r[0].total
            response['annexure_file'] = annex_r[0].annexure_file
    return render(request,'recruit/annexure/annexure_r.djt',response)

@login_required(login_url='/register')
def annexure_s(request):
    response = {}
    app_data = Appdata.objects.get(user = request.user)
    print app_data
    if(request.POST):
        print request.POST
        try:
            annexure = Acad_Annex_S.objects.get(app_id=app_data)
            annexure.annexure_data = getValue(request, annexure, 'annexure_s')
            annexure.last_prom = request.POST['last_prom']
            annexure.store = True
            annexure.extra_load = float(request.POST.get('extra_load',0));
            annexure.credit_score = float(request.POST.get('credit',0));
            annexure.avg_load = float(request.POST.get('avg_load',0));
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()
        except ObjectDoesNotExist:
            annexure = Acad_Annex_S()
            annexure.app_id = Appdata.objects.get(app_id = app_data)
            annexure.annexure_data = request.POST['annexure_s']
            annexure.last_prom = request.POST['last_prom']
            annexure.extra_load = float(request.POST.get('extra_load',0));
            annexure.credit_score = float(request.POST.get('credit',0));
            annexure.avg_load = float(request.POST.get('avg_load',0));
            annexure.store = True
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()
        return redirect('/academic')
    annex_s = Acad_Annex_S.objects.filter(app_id=app_data)
    if annex_s.count() > 0:
        if annex_s[0].annexure_data:
            response['annex_s'] = json.loads(annex_s[0].annexure_data)
            response['last_prom'] = annex_s[0].last_prom
            response['extra_load'] = annex_s[0].extra_load
            response['credit'] = annex_s[0].credit_score
            response['avg_load'] = annex_s[0].avg_load
            response['annexure_file'] = annex_s[0].annexure_file
    return render(request,'recruit/annexure/annexure_s.djt',response)

def getValue(request, annexure, str):
    if(len(request.POST[str])>2):
        oldstr = annexure.annexure_data
        #print(oldstr)
        newstr = request.POST[str]
        if oldstr == " " or oldstr == "[]" or oldstr == '[]':
            return "[" + newstr[1:]
        else:
            return oldstr[:-1] + "," + newstr[1:]
        return oldstr[:-1] + "," + newstr[1:]
    return " "

def getJsonStringVal(oldstr,newstr):
    if(len(oldstr)>2) :
        return oldstr[:-1] + "," + newstr[1:]
    else :
        return newstr

@login_required(login_url='/register')
def annexure_t(request):
    response = {}
    app_data = Appdata.objects.get(user = request.user)
    print app_data
    if(request.POST):
        try:
            annexure = Acad_Annex_T.objects.get(app_id=app_data)
            annexure.annexure_data = getValue(request, annexure, 'annexure_t')
            annexure.last_prom = request.POST['last_prom']
            annexure.total = float(request.POST.get('total',0));
            annexure.store = True
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()
        except ObjectDoesNotExist:
            annexure = Acad_Annex_T()
            annexure.app_id = Appdata.objects.get(app_id = app_data)
            annexure.annexure_data = request.POST['annexure_t']
            annexure.last_prom = request.POST['last_prom']
            annexure.total = float(request.POST.get('total',0));
            annexure.store = True
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()
        return redirect('/academic')
    annex_t = Acad_Annex_T.objects.filter(app_id=app_data)
    if annex_t.count() > 0:
        if annex_t[0].annexure_data:
            response['annex_t'] = json.loads(annex_t[0].annexure_data)
            response['last_prom'] = annex_t[0].last_prom
            response['total'] = annex_t[0].total
            response['annexure_file'] = annex_t[0].annexure_file
    return render(request,'recruit/annexure/annexure_t.djt',response)

@login_required(login_url='/register')
def annexure_u(request):
    response = {}
    app_data = Appdata.objects.get(user = request.user)
    if(request.POST):
        print request.POST
        try:
            annexure = Acad_Annex_U.objects.get(app_id=app_data)
            annexure.annexure_data = getValue(request, annexure, 'annexure_u')
            annexure.last_prom = request.POST['last_prom']
            annexure.total = float(request.POST.get('total',0));
            annexure.store = True
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()
        except ObjectDoesNotExist:
            annexure = Acad_Annex_U()
            annexure.app_id = Appdata.objects.get(app_id = app_data)
            annexure.annexure_data = request.POST['annexure_u']
            annexure.last_prom = request.POST['last_prom']
            annexure.total = float(request.POST.get('total',0));
            annexure.store = True
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()
        return redirect('/academic')
    annex_u = Acad_Annex_U.objects.filter(app_id=app_data)
    if annex_u.count() > 0:
        if annex_u[0].annexure_data:
            response['annex_u'] = json.loads(annex_u[0].annexure_data)
            response['last_prom'] = annex_u[0].last_prom
            response['total'] = annex_u[0].total
            response['annexure_file'] = annex_u[0].annexure_file
    return render(request,'recruit/annexure/annexure_u.djt',response)

@login_required(login_url='/register')
def annexure_v(request):
    response = {}
    app_data = Appdata.objects.get(user = request.user)
    if(request.POST):
        print request.POST
        try:
            annexure = Acad_Annex_V.objects.get(app_id=app_data)
            annexure.annexure_data = getValue(request, annexure, 'annexure_v')
            annexure.last_prom = request.POST['last_prom']
            annexure.total = float(request.POST.get('total',0));
            annexure.store = True
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()
        except ObjectDoesNotExist:
            annexure = Acad_Annex_V()
            annexure.app_id = Appdata.objects.get(app_id = app_data)
            annexure.annexure_data = request.POST['annexure_v']
            annexure.last_prom = request.POST['last_prom']
            annexure.total = float(request.POST.get('total',0));
            annexure.store = True
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()
        return redirect('/academic')
    annex_v = Acad_Annex_V.objects.filter(app_id=app_data)
    if annex_v.count() > 0:
        if annex_v[0].annexure_data:
            response['annex_v'] = json.loads(annex_v[0].annexure_data)
            response['last_prom'] = annex_v[0].last_prom
            response['total'] = annex_v[0].total
            response['annexure_file'] = annex_v[0].annexure_file
    return render(request,'recruit/annexure/annexure_v.djt',response)

@login_required(login_url='/register')
def annexure_w1(request) :
    response = {}
    app_data = Appdata.objects.get(user = request.user)
    print app_data
    if(request.POST):
        print request.POST
        try:
            annexure = Acad_Annex_W1_W2.objects.get(app_id=app_data)
            if len(request.POST['annexure_w1'])>2:
                oldstr = annexure.annexure_data1
                newstr = request.POST['annexure_w1']
                if oldstr == " " or oldstr == "[]":
                    annexure.annexure_data1 = "[" + newstr[1:]
                else:
                    annexure.annexure_data1 = oldstr[:-1] + "," + newstr[1:]
            annexure.last_prom_w1 = request.POST['last_prom']
            annexure.total_w1 = float(request.POST.get('total_w1',0));
            annexure.store_w1 = True
            if request.FILES:
                annexure.annexure_file_w1 = request.FILES['annexure_file']
            annexure.save()
        except ObjectDoesNotExist:
            annexure = Acad_Annex_W1_W2()
            annexure.app_id = Appdata.objects.get(app_id = app_data)
            annexure.annexure_data1 = request.POST['annexure_w1']
            annexure.last_prom_w1 = request.POST['last_prom']
            annexure.total_w1 = annexure.total_w1+float(request.POST.get('total_w1',0));
            annexure.store_w1 = True
            if request.FILES:
                annexure.annexure_file_w1 = request.FILES['annexure_file']
            annexure.save()
        return redirect('/academic')
    annex_w1 = Acad_Annex_W1_W2.objects.filter(app_id=app_data)
    if annex_w1.count() > 0:
        if len(str((annex_w1[0].annexure_data1).encode("utf-8"))) > 1:
            response['annex_w1'] = json.loads(annex_w1[0].annexure_data1)
            response['last_prom'] = annex_w1[0].last_prom_w1
            response['total_w1'] = annex_w1[0].total_w1
            response['annexure_file'] = annex_w1[0].annexure_file_w1
    return render(request,'recruit/annexure/annexure_w1.djt',response)

@login_required(login_url='/register')
def annexure_w2(request):
    app_data = Appdata.objects.get(user = request.user)
    response = {}
    if(request.POST):
        print request.POST
        try:
            annexure = Acad_Annex_W1_W2.objects.get(app_id=app_data)
            if len(request.POST['annexure_w2'])>2:
                oldstr = annexure.annexure_data2
                newstr = request.POST['annexure_w2']
                if oldstr == " " or oldstr == "[]":
                    annexure.annexure_data2 = "[" + newstr[1:]
                else:
                    annexure.annexure_data2 = oldstr[:-1] + "," + newstr[1:]
            annexure.last_prom_w2 = request.POST['last_prom']
            annexure.total_w2 = float(request.POST.get('total_w2',0));
            annexure.store_w2 = True
            if request.FILES:
                annexure.annexure_file_w2 = request.FILES['annexure_file']
            annexure.save()
        except ObjectDoesNotExist:
            annexure = Acad_Annex_W1_W2()
            annexure.app_id = Appdata.objects.get(app_id = app_data)
            annexure.annexure_data2 = request.POST['annexure_w2']
            annexure.last_prom_w2 = request.POST['last_prom']
            annexure.total_w2 = annexure.total_w2+float(request.POST.get('total_w2',0));
            annexure.store_w2 = True
            if request.FILES:
                annexure.annexure_file_w2 = request.FILES['annexure_file']
            annexure.save()
        return redirect('/academic')
    annex_w2 = Acad_Annex_W1_W2.objects.filter(app_id=app_data)
    if annex_w2.count() > 0:
        if len(str((annex_w2[0].annexure_data2).encode("utf-8"))) > 1:
            response['annex_w2'] = json.loads(annex_w2[0].annexure_data2)
            response['last_prom'] = annex_w2[0].last_prom_w2
            response['total_w2'] = annex_w2[0].total_w2
            response['annexure_file'] = annex_w2[0].annexure_file_w2
    return render(request,'recruit/annexure/annexure_w2.djt',response)

@login_required(login_url='/register')
def annexure_x(request):
    response = {}
    app_data = Appdata.objects.get(user = request.user)
    print app_data
    if(request.POST):
        print request.POST
        try:
            annexure = Acad_Annex_X.objects.get(app_id=app_data)
            annexure.annexure_data = getValue(request, annexure, 'annexure_x')
            annexure.last_prom = request.POST['last_prom']
            annexure.total = float(request.POST.get('total',0));
            annexure.store = True
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()
        except ObjectDoesNotExist:
            annexure = Acad_Annex_X()
            annexure.app_id = Appdata.objects.get(app_id = app_data)
            annexure.annexure_data = request.POST['annexure_x']
            annexure.last_prom = request.POST['last_prom']
            annexure.total = annexure.total+float(request.POST.get('total',0));
            annexure.store = True
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()
        return redirect('/academic')
    annex_x = Acad_Annex_X.objects.filter(app_id=app_data)
    if annex_x.count() > 0:
        if len(str((annex_x[0].annexure_data).encode("utf-8"))) > 1:
            response['annex_x'] = json.loads(annex_x[0].annexure_data)
            response['last_prom'] = annex_x[0].last_prom
            response['annexure_file'] = annex_x[0].annexure_file
            response['total'] = annex_x[0].total
    return render(request,'recruit/annexure/annexure_x.djt',response)

@login_required(login_url='/register')
def annexure_y(request):
    app_data = Appdata.objects.get(user = request.user)
    result = {}
    if request.POST:
        print request.POST
        result['ieee'] = False
        result['fna'] = False
        result['fnae']=False
        result['fnasc'] = False
        for key in request.POST:
            if(key == 'csrfmiddlewaretoken' or key == 'credit'):
                continue
            value = request.POST[key]
            if(len(value)>0):
                result[str(value)] = True
                print value
        try:
            annexure = Acad_Annex_Y.objects.get(app_id=app_data)
            annexure.annexure_data = result
            annexure.store = True
            annexure.credit_score = float(request.POST.get('credit',0))
            annexure.ieee = result['ieee']
            annexure.fna = result['fna']
            annexure.fnae = result['fnae']
            annexure.fnasc = result['fnasc']
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()
        except ObjectDoesNotExist:
            annexure = Acad_Annex_Y()
            annexure.app_id = Appdata.objects.get(app_id = app_data)
            annexure.ieee = result['ieee']
            annexure.fna = result['fna']
            annexure.fnae = result['fnae']
            annexure.fnasc = result['fnasc']
            annexure.credit_score = float(request.POST.get('credit',0))
            annexure.store = True
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()
        return redirect('/academic')
    annex_y = Acad_Annex_Y.objects.filter(app_id=app_data)
    response = {}
    if annex_y.count() > 0:
        response['credit'] = annex_y[0].credit_score
        response['ieee'] = annex_y[0].ieee 
        response['fna'] = annex_y[0].fna 
        response['fnae'] = annex_y[0].fnae 
        response['fnasc'] = annex_y[0].fnasc 
        response['annexure_file'] = annex_y[0].annexure_file
    return render(request,'recruit/annexure/annexure_y.djt',response)

@login_required(login_url='/register')
def annexure_z(request):
    response = {}
    app_data = Appdata.objects.get(user = request.user)
    if(request.POST):
        print request.POST
        try:
            annexure = Acad_Annex_Z.objects.get(app_id=app_data)
            annexure.annexure_data = getValue(request, annexure, 'annexure_z')
            annexure.store = True
            annexure.total = float(request.POST.get('total',0));
            annexure.last_prom=request.POST['last_prom']
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()
        except ObjectDoesNotExist:
            annexure = Acad_Annex_Z()
            annexure.app_id = Appdata.objects.get(app_id = app_data)
            annexure.annexure_data = request.POST['annexure_z']
            annexure.store = True
            annexure.total = annexure.total+float(request.POST.get('total',0));
            annexure.last_prom=request.POST['last_prom']
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()
        return redirect('/academic')
    annex_z = Acad_Annex_Z.objects.filter(app_id=app_data)
    if annex_z.count() > 0:
        if len(str((annex_z[0].annexure_data).encode("utf-8"))) > 1:
            response['annex_z'] = json.loads(annex_z[0].annexure_data)
            response['last_prom'] = annex_z[0].last_prom
            response['annexure_file'] = annex_z[0].annexure_file
            response['total'] = annex_z[0].total
    return render(request,'recruit/annexure/annexure_z.djt',response)

@login_required(login_url='/register')
def subject_ref(request):
    response = {}
    app_id = Appdata.objects.get(user=request.user)
    if app_id.submitted :
        return redirect('/printSummary')
    response['app'] = app_id

    if request.method == 'POST' :

        if not SubjectTaught.objects.filter(app_id=app_id,level='UG',courseType='core').exists() :
            coreUG = SubjectTaught()
            coreUG.app_id = app_id
            coreUG.level = 'UG'
            coreUG.courseType = 'core'
            coreUG.data = request.POST['coreUGdata']
        else :
            coreUG = SubjectTaught.objects.get(app_id=app_id,level='UG',courseType='core')
            if len(request.POST.get('coreUGdata'))>2 :
                oldstr = coreUG.data
                newstr = request.POST['coreUGdata']
                coreUG.data = getJsonStringVal(oldstr,newstr)
        coreUG.save()

        if not SubjectTaught.objects.filter(app_id=app_id,level='UG',courseType='elective').exists() :
            electiveUG = SubjectTaught()
            electiveUG.app_id = app_id
            electiveUG.level = 'UG'
            electiveUG.courseType = 'elective'
            electiveUG.data = request.POST['electiveUGdata']
        else :
            electiveUG = SubjectTaught.objects.get(app_id=app_id,level='UG',courseType='elective')
            if len(request.POST.get('electiveUGdata'))>2:
                oldstr2 = electiveUG.data
                newstr2 = request.POST['electiveUGdata']
                electiveUG.data = getJsonStringVal(oldstr2,newstr2)
        electiveUG.save()

        if not SubjectTaught.objects.filter(app_id=app_id,level='PG',courseType='core').exists() :
            corePG = SubjectTaught()
            corePG.app_id = app_id
            corePG.level = 'PG'
            corePG.courseType = 'core'
            corePG.data = request.POST['corePGdata']
        else :
            corePG = SubjectTaught.objects.get(app_id=app_id,level='PG',courseType='core')
            if len(request.POST['corePGdata'])>2 :
                oldstr3 = corePG.data
                newstr3 = request.POST['corePGdata']
                corePG.data = getJsonStringVal(oldstr3,newstr3)
        corePG.save()

        if not SubjectTaught.objects.filter(app_id=app_id,level='PG',courseType='elective').exists() :
            electivePG = SubjectTaught()
            electivePG.app_id = app_id
            electivePG.level = 'PG'
            electivePG.courseType = 'elective'
            electivePG.data = request.POST['electivePGdata']
        else :
            electivePG = SubjectTaught.objects.get(app_id=app_id,level='PG',courseType='elective')
            if len(request.POST['electivePGdata'])>2 :
                oldstr4 = electivePG.data
                newstr4 = request.POST['electivePGdata']
                electivePG.data = getJsonStringVal(oldstr4,newstr4)
        electivePG.save()

        if not Referral.objects.filter(app_id=app_id).exists() :
            refobj = Referral()
            refobj.app_id = app_id
            refobj.ref_data = request.POST['refFinaldata']
        else :
            refobj = Referral.objects.get(app_id=app_id)
            if len(request.POST['refFinaldata'])>2 :
                oldstr = refobj.ref_data
                newstr = request.POST['refFinaldata']
                refobj.ref_data = getJsonStringVal(oldstr,newstr)
        refobj.save()

    if SubjectTaught.objects.filter(app_id=app_id,level='UG',courseType='core').exists() :
        obj1 = SubjectTaught.objects.get(app_id=app_id,level='UG',courseType='core')
        response['coreUGobj'] = json.loads(obj1.data)
    if SubjectTaught.objects.filter(app_id=app_id,level='UG',courseType='elective').exists() :
        obj2 = SubjectTaught.objects.get(app_id=app_id,level='UG',courseType='elective')
        response['electiveUGobj'] = json.loads(obj2.data)
    if SubjectTaught.objects.filter(app_id=app_id,level='PG',courseType='core').exists() :
        obj3 = SubjectTaught.objects.get(app_id=app_id,level='PG',courseType='core')
        response['corePGobj'] = json.loads(obj3.data)
    if SubjectTaught.objects.filter(app_id=app_id,level='PG',courseType='elective').exists() :
        obj4 = SubjectTaught.objects.get(app_id=app_id,level='PG',courseType='elective')
        response['electivePGobj'] = json.loads(obj4.data)
    if Referral.objects.filter(app_id=app_id).exists() :
        obj5 = Referral.objects.get(app_id=app_id)
        response['refobjs'] = json.loads(obj5.ref_data)

    return render(request,'recruit/subject_ref.djt',response)

@login_required(login_url='/register')
def printSummary(request):
    response = {}
    app_id = request.user.username
    if Shortlist.objects.filter(app_id=Appdata.objects.get(app_id=app_id)).exists():
        return redirect('/call_letter')
    return render(request,'recruit/summary.djt',response)

@login_required(login_url='/register')
def print_main_application(request):
    response = {}
    response['profile'] = UserProfile.objects.get(user = request.user)
    app_id = Appdata.objects.get(user=request.user)
    response['specialization'] = app_id.specialize
    if FacUser.objects.filter(app_id=app_id).exists():
        response['generalData'] = FacUser.objects.get(app_id=app_id)
    if Experience.objects.filter(app_id=app_id).exists():
        exp = Experience.objects.get(app_id=app_id)
        response['Experience'] = exp
        response['teachingData'] = json.loads(exp.teaching_data)
        response['researchData'] = json.loads(exp.research_data)
        response['industryData'] = json.loads(exp.industrial_data)

    if Qualification.objects.filter(app_id=app_id,degreeType='UG').exists():
        response['Bqual'] = Qualification.objects.get(app_id=app_id,degreeType='UG')
    if Qualification.objects.filter(app_id=app_id,degreeType='PG').exists():
        response['Mqual'] = Qualification.objects.get(app_id=app_id,degreeType='PG')
    if Qualification.objects.filter(app_id=app_id,degreeType='PHD').exists():
        response['Phdqual'] = Qualification.objects.get(app_id=app_id,degreeType='PHD')
    if Qualification.objects.filter(app_id=app_id,degreeType='other').exists():
        response['Oqual'] = Qualification.objects.get(app_id=app_id,degreeType='other')

    external_sponsored_rnd = External_Sponsored_RnD.objects.filter(app_id=app_id)
    consultancy_projects = Consultancy_Projects.objects.filter(app_id=app_id)
    phd_completed = PhD_Completed.objects.filter(app_id=app_id)
    journal_papers = Journal_Papers.objects.filter(app_id = app_id)
    conference_paper_sci = Conference_Paper_SCI.objects.filter(app_id = app_id)


    acad_annex_a = Acad_Annex_A.objects.filter(app_id=app_id)
    acad_annex_b = Acad_Annex_B.objects.filter(app_id=app_id)
    acad_annex_c = Acad_Annex_C.objects.filter(app_id=app_id)
    acad_annex_d = Acad_Annex_D.objects.filter(app_id=app_id)
    acad_annex_e12 = Acad_Annex_E12.objects.filter(app_id=app_id)
    acad_annex_f = Acad_Annex_F.objects.filter(app_id=app_id)
    acad_annex_g = Acad_Annex_G.objects.filter(app_id=app_id)
    acad_annex_h = Acad_Annex_H.objects.filter(app_id=app_id)
    acad_annex_i = Acad_Annex_I.objects.filter(app_id=app_id)
    acad_annex_j = Acad_Annex_J.objects.filter(app_id=app_id)
    acad_annex_k = Acad_Annex_K.objects.filter(app_id=app_id)
    acad_annex_l = Acad_Annex_L.objects.filter(app_id=app_id)
    acad_annex_m = Acad_Annex_M.objects.filter(app_id=app_id)
    acad_annex_n = Acad_Annex_N.objects.filter(app_id=app_id)
    acad_annex_o = Acad_Annex_O.objects.filter(app_id=app_id)
    acad_annex_p = Acad_Annex_P.objects.filter(app_id=app_id)
    acad_annex_q = Acad_Annex_Q.objects.filter(app_id=app_id)
    acad_annex_r = Acad_Annex_R.objects.filter(app_id=app_id)
    acad_annex_s = Acad_Annex_S.objects.filter(app_id=app_id)
    acad_annex_t = Acad_Annex_T.objects.filter(app_id=app_id)
    acad_annex_u = Acad_Annex_U.objects.filter(app_id=app_id)
    acad_annex_v = Acad_Annex_V.objects.filter(app_id=app_id)
    acad_annex_w1_w2 = Acad_Annex_W1_W2.objects.filter(app_id=app_id)
    acad_annex_x = Acad_Annex_X.objects.filter(app_id=app_id)
    acad_annex_y = Acad_Annex_Y.objects.filter(app_id=app_id)
    acad_annex_z = Acad_Annex_Z.objects.filter(app_id=app_id)

    if external_sponsored_rnd.count() > 0:
        response['external_sponsored_rnd'] = external_sponsored_rnd[0]
        if external_sponsored_rnd[0].projects_not_pi:
            response['projects_not_pi'] = json.loads(external_sponsored_rnd[0].projects_not_pi)
        if external_sponsored_rnd[0].patents_not_pi:
            response['patents_not_pi'] = json.loads(external_sponsored_rnd[0].patents_not_pi)

    if consultancy_projects.count() > 0:
        response['consultancy_projects'] = consultancy_projects[0]

    if phd_completed.count() > 0:
        response['phd_completed'] = phd_completed[0]
        if phd_completed[0].phds:
            response['phds'] = json.loads(phd_completed[0].phds)
        response['phds'] = json.loads(phd_completed[0].phds)

    if journal_papers.count() > 0:
        response['journal_papers'] = journal_papers[0]
        if journal_papers[0].papers:
            response['papers'] = json.loads(journal_papers[0].papers)
        response['papers'] = json.loads(journal_papers[0].papers)

    if conference_paper_sci.count() > 0:
        response['conference_paper_sci'] = conference_paper_sci[0]
        if conference_paper_sci[0].papers:
            response['papers1'] = json.loads(conference_paper_sci[0].papers)
        response['papers1'] = json.loads(conference_paper_sci[0].papers)


    if acad_annex_a.count() > 0:
        response['acad_annex_a'] = acad_annex_a[0]

    if acad_annex_b.count() > 0:
        response['acad_annex_b'] = acad_annex_b[0]
    if acad_annex_c.count() > 0:
        response['acad_annex_c'] = acad_annex_c[0]

    if acad_annex_d.count() > 0:
        response['acad_annex_d'] = acad_annex_d[0]

    if acad_annex_e12.count() > 0:
        response['acad_annex_e12'] = acad_annex_e12[0]
        response['total_e'] = float(acad_annex_e12[0].total_e1 + acad_annex_e12[0].total_e2)

    if acad_annex_f.count() > 0:
        response['acad_annex_f'] = acad_annex_f[0]

    if acad_annex_g.count() > 0:
        response['acad_annex_g'] = acad_annex_g[0]

    if acad_annex_h.count() > 0:
        response['acad_annex_h'] = acad_annex_h[0]

    if acad_annex_i.count() > 0:
        response['acad_annex_i'] = acad_annex_i[0]

    if acad_annex_j.count() > 0:
        response['acad_annex_j'] = acad_annex_j[0]

    if acad_annex_k.count() > 0:
        response['acad_annex_k'] = acad_annex_k[0]

    if acad_annex_l.count() > 0:
        response['acad_annex_l'] = acad_annex_l[0]

    if acad_annex_m.count() > 0:
        response['acad_annex_m'] = acad_annex_m[0]

    if acad_annex_n.count() > 0:
        response['acad_annex_n'] = acad_annex_n[0]

    if acad_annex_o.count() > 0:
        response['acad_annex_o'] = acad_annex_o[0]

    if acad_annex_p.count() > 0:
        response['acad_annex_p'] = acad_annex_p[0]

    if acad_annex_q.count() > 0:
        response['acad_annex_q'] = acad_annex_q[0]  

    if acad_annex_r.count() > 0:
        response['acad_annex_r'] = acad_annex_r[0]

    if acad_annex_s.count() > 0:
        response['acad_annex_s'] = acad_annex_s[0]

    if acad_annex_t.count() > 0:
        response['acad_annex_t'] = acad_annex_t[0]

    if acad_annex_u.count() > 0:
        response['acad_annex_u'] = acad_annex_u[0]

    if acad_annex_v.count() > 0:
        response['acad_annex_v'] = acad_annex_v[0]

    if acad_annex_w1_w2.count() > 0:
        response['acad_annex_w1_w2'] = acad_annex_w1_w2[0]
        response['total_w'] = float(acad_annex_w1_w2[0].total_w1 + acad_annex_w1_w2[0].total_w2)

    if acad_annex_x.count() > 0:
        response['acad_annex_x'] = acad_annex_x[0]

    if acad_annex_y.count() > 0:
        response['acad_annex_y'] = acad_annex_y[0]

    if acad_annex_z.count() > 0:
        response['acad_annex_z'] = acad_annex_z[0]

    if SubjectTaught.objects.filter(app_id=app_id,level='UG',courseType='core').exists() :
        obj1 = SubjectTaught.objects.get(app_id=app_id,level='UG',courseType='core')
        response['coreUGobj'] = json.loads(obj1.data)
    if SubjectTaught.objects.filter(app_id=app_id,level='UG',courseType='elective').exists() :
        obj2 = SubjectTaught.objects.get(app_id=app_id,level='UG',courseType='elective')
        response['electiveUGobj'] = json.loads(obj2.data)
    if SubjectTaught.objects.filter(app_id=app_id,level='PG',courseType='core').exists() :
        obj3 = SubjectTaught.objects.get(app_id=app_id,level='PG',courseType='core')
        response['corePGobj'] = json.loads(obj3.data)
    if SubjectTaught.objects.filter(app_id=app_id,level='PG',courseType='elective').exists() :
        obj4 = SubjectTaught.objects.get(app_id=app_id,level='PG',courseType='elective')
        response['electivePGobj'] = json.loads(obj4.data)
    if Referral.objects.filter(app_id=app_id).exists() :
        obj5 = Referral.objects.get(app_id=app_id)
        response['refobjs'] = json.loads(obj5.ref_data)
    
    
    return render(request, 'recruit/print_main_application.djt', response)

@login_required(login_url='/register')
def print_annexures(request):
    response = {}
    response['profile'] = UserProfile.objects.get(user = request.user)
    app_id = Appdata.objects.get(user=request.user)
    response['specialization'] = app_id.specialize

    annex_e1 = Acad_Annex_E12.objects.filter(app_id=app_id)
    if annex_e1.count() > 0:
        if len(str((annex_e1[0].annexure_data_e1).encode("utf-8"))) > 1:
            response['annex_e1'] = json.loads(annex_e1[0].annexure_data_e1)

    annex_e2 = Acad_Annex_E12.objects.filter(app_id=app_id)
    if annex_e2.count() > 0:
        if len(str((annex_e2[0].annexure_data_e2).encode("utf-8"))) > 1:
            response['annex_e2'] = json.loads(annex_e2[0].annexure_data_e2)

    annex_f = Acad_Annex_F.objects.filter(app_id=app_id)
    if annex_f.count() > 0:
        if annex_f[0].annexure_data:
            response['annex_f'] = json.loads(annex_f[0].annexure_data)
            response['annex_f_credit'] = annex_f[0].credit_score

    annex_g = Acad_Annex_G.objects.filter(app_id=app_id)
    if annex_g.count() > 0:
        if annex_g[0].annexure_data:
            response['annex_g'] = json.loads(annex_g[0].annexure_data)

    annex_h = Acad_Annex_H.objects.filter(app_id=app_id)
    if annex_h.count() > 0:
        if annex_h[0].annexure_data:
            response['annex_h'] = json.loads(annex_h[0].annexure_data)
            response['annex_h_last_prom'] = annex_h[0].last_prom

    annex_i = Acad_Annex_I.objects.filter(app_id=app_id)
    if annex_i.count() > 0:
        if annex_i[0].annexure_data:
            response['annex_i'] = json.loads(annex_i[0].annexure_data)

    annex_j = Acad_Annex_J.objects.filter(app_id=app_id)
    if annex_j.count() > 0:
        if annex_j[0].annexure_data:
            response['annex_j'] = json.loads(annex_j[0].annexure_data)
            response['annex_j_credit'] = annex_j[0].credit_score
            response['annex_j_last_prom'] = annex_j[0].last_prom

    annex_k = Acad_Annex_K.objects.filter(app_id=app_id)
    if annex_k.count() > 0:
        if annex_k[0].annexure_data:
            response['annex_k'] = json.loads(annex_k[0].annexure_data)
            response['annex_k_credit'] = annex_k[0].credit_score
            response['annex_k_last_prom'] = annex_k[0].last_prom

    annex_l = Acad_Annex_L.objects.filter(app_id=app_id)
    if annex_l.count() > 0:
        if annex_l[0].annexure_data:
            response['annex_l'] = json.loads(annex_l[0].annexure_data)
            response['annex_l_last_prom'] = annex_l[0].last_prom
            response['annex_l_credit'] = annex_l[0].credit_score

    annex_m = Acad_Annex_M.objects.filter(app_id=app_id)
    if annex_m.count() > 0:
        if annex_m[0].annexure_data:
            response['annex_m'] = json.loads(annex_m[0].annexure_data)
            response['annex_m_credit'] = annex_m[0].credit_score
            response['annex_m_last_prom'] = annex_m[0].last_prom

    annex_n = Acad_Annex_N.objects.filter(app_id=app_id)
    if annex_n.count() > 0:
        if annex_n[0].annexure_data:
            response['annex_n'] = json.loads(annex_n[0].annexure_data)
            response['annex_n_last_prom'] = annex_n[0].last_prom

    annex_o = Acad_Annex_O.objects.filter(app_id=app_id)
    if annex_o.count() > 0:
        if annex_o[0].annexure_data:
            response['annex_o'] = json.loads(annex_o[0].annexure_data)
            response['annex_o_last_prom'] = annex_o[0].last_prom

    annex_p = Acad_Annex_P.objects.filter(app_id=app_id)
    if annex_p.count() > 0:
        if annex_p[0].annexure_data:
            response['annex_p'] = json.loads(annex_p[0].annexure_data)
            response['annex_p_last_prom'] = annex_p[0].last_prom

    annex_q = Acad_Annex_Q.objects.filter(app_id=app_id)
    if annex_q.count() > 0:
        if annex_q[0].annexure_data:
            response['annex_q'] = json.loads(annex_q[0].annexure_data)
            response['annex_q_last_prom'] = annex_q[0].last_prom
            response['annex_q_exp_phd'] = annex_q[0].total_exp_after_phd
            response['annex_q_exp_cur'] = annex_q[0].total_exp_cur
            response['annex_q_tot_exp'] = annex_q[0].total_exp
            response['annex_q_credit'] = annex_q[0].credit_score

    annex_r = Acad_Annex_R.objects.filter(app_id=app_id)
    if annex_r.count() > 0:
        if annex_r[0].annexure_data:
            response['annex_r'] = json.loads(annex_r[0].annexure_data)
            response['annex_r_last_prom'] = annex_r[0].last_prom

    annex_s = Acad_Annex_S.objects.filter(app_id=app_id)
    if annex_s.count() > 0:
        if annex_s[0].annexure_data:
            response['annex_s'] = json.loads(annex_s[0].annexure_data)
            response['annex_s_last_prom'] = annex_s[0].last_prom
            response['annex_s_extra_load'] = annex_s[0].extra_load
            response['annex_s_credit'] = annex_s[0].credit_score

    annex_t = Acad_Annex_T.objects.filter(app_id=app_id)
    if annex_t.count() > 0:
        if annex_t[0].annexure_data:
            response['annex_t'] = json.loads(annex_t[0].annexure_data)
            response['annex_t_last_prom'] = annex_t[0].last_prom

    annex_u = Acad_Annex_U.objects.filter(app_id=app_id)
    if annex_u.count() > 0:
        if annex_u[0].annexure_data:
            response['annex_u'] = json.loads(annex_u[0].annexure_data)
            response['annex_u_last_prom'] = annex_u[0].last_prom

    annex_v = Acad_Annex_V.objects.filter(app_id=app_id)
    if annex_v.count() > 0:
        if annex_v[0].annexure_data:
            response['annex_v'] = json.loads(annex_v[0].annexure_data)
            response['annex_v_last_prom'] = annex_v[0].last_prom
    
    annex_w1 = Acad_Annex_W1_W2.objects.filter(app_id=app_id)
    if annex_w1.count() > 0:
        if len(str((annex_w1[0].annexure_data1).encode("utf-8"))) > 1:
            response['annex_w1'] = json.loads(annex_w1[0].annexure_data1)
            response['annex_w1_last_prom'] = annex_w1[0].last_prom_w1

    annex_w2 = Acad_Annex_W1_W2.objects.filter(app_id=app_id)
    if annex_w2.count() > 0:
        if len(str((annex_w2[0].annexure_data2).encode("utf-8"))) > 1:
            response['annex_w2'] = json.loads(annex_w2[0].annexure_data2)
            response['annex_w2_last_prom'] = annex_w2[0].last_prom_w2

    annex_x = Acad_Annex_X.objects.filter(app_id=app_id)
    if annex_x.count() > 0:
        if len(str((annex_x[0].annexure_data).encode("utf-8"))) > 1:
            response['annex_x'] = json.loads(annex_x[0].annexure_data)
            response['annex_x_last_prom'] = annex_x[0].last_prom

    annex_y = Acad_Annex_Y.objects.filter(app_id=app_id)
    if annex_y.count() > 0:
        response['annex_y_credit'] = annex_y[0].credit_score
        response['annex_y_ieee'] = annex_y[0].ieee 
        response['annex_y_fna'] = annex_y[0].fna 
        response['annex_y_fnae'] = annex_y[0].fnae 
        response['annex_y_fnasc'] = annex_y[0].fnasc 

    annex_z = Acad_Annex_Z.objects.filter(app_id=app_id)
    if annex_z.count() > 0:
        if len(str((annex_z[0].annexure_data).encode("utf-8"))) > 1:
            response['annex_z'] = json.loads(annex_z[0].annexure_data)
            response['annex_z_last_prom'] = annex_z[0].last_prom

    annex_a = Acad_Annex_A.objects.filter(app_id=app_id)
    if annex_a.count() > 0:
        if len(str((annex_a[0].annexure_data).encode("utf-8"))) > 1:
            response['annex_a'] = json.loads(annex_a[0].annexure_data)

    return render(request, 'recruit/print_annexures.djt', response)

def uploadPaper(request,papernum=0) :
    response = {}
    app_id = Appdata.objects.get(user=request.user)
    response["app"] = app_id

    if Paper.objects.filter(app_id=app_id).exists() :
        obj = Paper.objects.get(app_id=app_id)
    else :
        obj = Paper()
        obj.app_id = app_id
        obj.save()

    if request.method == 'POST' :
        if papernum=='1' :
            obj.paper1 = request.FILES['paper1']
            if validateFormat(obj.paper1) :
                obj.save()
            else : 
                return HttpResponse('Only Pdf format is allowed')
        if papernum=='2' :
            obj.paper2 = request.FILES['paper2']
            if validateFormat(obj.paper2) :
                obj.save()
            else : 
                return HttpResponse('Only Pdf format is allowed')
        if papernum=='3' :
            obj.paper3 = request.FILES['paper3']
            if validateFormat(obj.paper3) :
                obj.save()
            else : 
                return HttpResponse('Only Pdf format is allowed')
        if papernum=='4' :
            obj.paper4 = request.FILES['paper4']
            if validateFormat(obj.paper5) :
                obj.save()
            else : 
                return HttpResponse('Only Pdf format is allowed')
        if papernum=='5' :
            obj.paper5 = request.FILES['paper5']
            if validateFormat(obj.paper5) :
                obj.save()
            else : 
                return HttpResponse('Only Pdf format is allowed')
        if papernum=='6' :
            obj.cvpaper = request.FILES['cvpaper']
            if validateFormat(obj.cvpaper) :
                obj.save()
            else : 
                return HttpResponse('Only Pdf format is allowed')
        

        if papernum=='7':
            obj.teachpaper = request.FILES['teachpaper']
            if validateFormat(obj.teachpaper):
                obj.save()
            else:
                return HttpResponse('Only Pdf format is allowed')

        if papernum=='8':
            obj.researchpaper = request.FILES['researchpaper']
            if validateFormat(obj.researchpaper):
                obj.save()
            else:
                return HttpResponse('Only Pdf format is allowed')

        return redirect('/uploadPaper/0')

    response['obj'] = obj
    return render(request,'recruit/upload_docs.djt',response)

def lockApplication(request) :
    response = {}
    app = Appdata.objects.get(user=request.user)
    app.submitted = True
    app.submitDate = datetime.datetime.now()
    app.save()

    mailid = request.user.email

    receiver = mailid
    sender = 'nitap_recruitment17@nitw.ac.in'
    content = 'Your Application for the post of '+app.post_for
    content = content + ' in '+app.post_in+' has been submitted on '
    content = content + app.submitDate.strftime('%Y-%m-%d %H:%M')
    rlist = []
    rlist.append(receiver)
    subject = 'Acknowlegement for Submission of Application'
    print (mailid+" : "+content)
    try:
        send_mail(subject,content,sender,rlist,fail_silently=False,)
    except BadHeaderError:
        return HttpResponse('Invalid header found.')

    return redirect('/subject_ref')

def printAck(request):
    response = {}
    app = Appdata.objects.get(user=request.user)
    response['facuser'] = FacUser.objects.get(app_id=app)
    response['app'] = app
    return render(request,'recruit/printAck.djt',response)

def validateFormat(filename):
    ext = os.path.splitext(filename.name)[1]
    valid_extentions = ['.pdf','.PDF']
    if not ext in valid_extentions:
        return False
    return True

def calculate_age(dob):
    born = datetime.datetime.strptime(dob, "%Y-%m-%d")
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def refresh(request,annexName) :
    response = {}
    app_data = Appdata.objects.get(user = request.user)
    if annexName == 'e_1' :
        if Acad_Annex_E12.objects.filter(app_id=app_data).exists() :
            annexure = Acad_Annex_E12.objects.get(app_id=app_data)
            annexure.store_e1 = False
            annexure.total_e1 = 0
            annexure.annexure_data_e1 = '[]'
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()

    if annexName == 'e2' :
        if Acad_Annex_E12.objects.filter(app_id=app_data).exists() :
            annexure = Acad_Annex_E12.objects.get(app_id=app_data)
            annexure.store_e2 = False
            annexure.total_e2 = 0
            annexure.annexure_data_e2 = '[]'
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()

    if annexName == 'f' :
        if Acad_Annex_F.objects.filter(app_id=app_data).exists() :
            annexure = Acad_Annex_F.objects.get(app_id=app_data)
            annexure.delete()

    if annexName == 'g' :
        if Acad_Annex_G.objects.filter(app_id=app_data).exists() :
            annexure = Acad_Annex_G.objects.get(app_id=app_data)
            annexure.delete()

    if annexName == 'h' :
        if Acad_Annex_H.objects.filter(app_id=app_data).exists() :
            annexure = Acad_Annex_H.objects.get(app_id=app_data)
            annexure.delete()

    if annexName == 'i' :
        if Acad_Annex_I.objects.filter(app_id=app_data).exists() :
            annexure = Acad_Annex_I.objects.get(app_id=app_data)
            annexure.delete()

    if annexName == 'j' :
        if Acad_Annex_J.objects.filter(app_id=app_data).exists() :
            annexure = Acad_Annex_J.objects.get(app_id=app_data)
            annexure.delete()

    if annexName == 'k' :
        if Acad_Annex_K.objects.filter(app_id=app_data).exists() :
            annexure = Acad_Annex_K.objects.get(app_id=app_data)
            annexure.delete()

    if annexName == 'l' :
        if Acad_Annex_L.objects.filter(app_id=app_data).exists() :
            annexure = Acad_Annex_L.objects.get(app_id=app_data)
            annexure.delete()

    if annexName == 'm' :
        if Acad_Annex_M.objects.filter(app_id=app_data).exists() :
            annexure = Acad_Annex_M.objects.get(app_id=app_data)
            annexure.delete()

    if annexName == 'n' :
        if Acad_Annex_N.objects.filter(app_id=app_data).exists() :
            annexure = Acad_Annex_N.objects.get(app_id=app_data)
            annexure.delete()

    if annexName == 'o' :
        if Acad_Annex_O.objects.filter(app_id=app_data).exists() :
            annexure = Acad_Annex_O.objects.get(app_id=app_data)
            annexure.delete()

    if annexName == 'p' :
        if Acad_Annex_P.objects.filter(app_id=app_data).exists() :
            annexure = Acad_Annex_P.objects.get(app_id=app_data)
            annexure.delete()

    if annexName == 'q' :
        if Acad_Annex_Q.objects.filter(app_id=app_data).exists() :
            annexure = Acad_Annex_Q.objects.get(app_id=app_data)
            annexure.delete()

    if annexName == 'r' :
        if Acad_Annex_R.objects.filter(app_id=app_data).exists() :
            annexure = Acad_Annex_R.objects.get(app_id=app_data)
            annexure.delete()

    if annexName == 's' :
        if Acad_Annex_S.objects.filter(app_id=app_data).exists() :
            annexure = Acad_Annex_S.objects.get(app_id=app_data)
            annexure.delete()

    if annexName == 't' :
        if Acad_Annex_T.objects.filter(app_id=app_data).exists() :
            annexure = Acad_Annex_T.objects.get(app_id=app_data)
            annexure.delete()

    if annexName == 'u' :
        if Acad_Annex_U.objects.filter(app_id=app_data).exists() :
            annexure = Acad_Annex_U.objects.get(app_id=app_data)
            annexure.delete()

    if annexName == 'v' :
        if Acad_Annex_V.objects.filter(app_id=app_data).exists() :
            annexure = Acad_Annex_V.objects.get(app_id=app_data)
            annexure.delete()

    if annexName == 'w1' :
        if Acad_Annex_W1_W2.objects.filter(app_id=app_data).exists() :
            annexure = Acad_Annex_W1_W2.objects.get(app_id=app_data)
            annexure.annexure_data1 = '[]'
            annexure.last_prom_w1 = ''
            annexure.total_w1 = 0
            annexure.store_w1 = False
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()

    if annexName == 'w2' :
        if Acad_Annex_W1_W2.objects.filter(app_id=app_data).exists() :
            annexure = Acad_Annex_W1_W2.objects.get(app_id=app_data)
            annexure.annexure_data2 = '[]'
            annexure.last_prom_w2 = ''
            annexure.total_w2 = 0
            annexure.store_w2 = False
            if request.FILES:
                annexure.annexure_file = request.FILES['annexure_file']
            annexure.save()

    if annexName == 'x' :
        if Acad_Annex_X.objects.filter(app_id=app_data).exists() :
            annexure = Acad_Annex_X.objects.get(app_id=app_data)
            annexure.delete()

    if annexName == 'y' :
        if Acad_Annex_Y.objects.filter(app_id=app_data).exists() :
            annexure = Acad_Annex_Y.objects.get(app_id=app_data)
            annexure.delete()

    if annexName == 'z' :
        if Acad_Annex_Z.objects.filter(app_id=app_data).exists() :
            annexure = Acad_Annex_Z.objects.get(app_id=app_data)
            annexure.delete()

    if annexName == 'a' :
        if Acad_Annex_A.objects.filter(app_id=app_data).exists() :
            annexure = Acad_Annex_A.objects.get(app_id=app_data)
            annexure.delete()


    return redirect('/academic/annexure_'+annexName)

def uploadExpDoc(request) :
    response = {}
    app_id = Appdata.objects.get(user=request.user)

    if Paper.objects.filter(app_id=app_id).exists() :
        obj = Paper.objects.get(app_id=app_id)
    else :
        obj = Paper()
        obj.app_id = app_id
        obj.save()

    if request.method == 'POST' :
        obj.paper1 = request.FILES['paper1']
        if validateFormat(obj.paper1) :
            obj.save()
        else : 
            return HttpResponse('Only Pdf format is allowed')
        return redirect('/uploadExpDoc')

    response['obj'] = obj
    return render(request,'recruit/uploadExpDocs.djt',response)

def all_annexures(request) :
    response = {}
    app_id = Appdata.objects.get(user=request.user)
    response['profile'] = UserProfile.objects.get(user = request.user)
    acad_annex_a = Acad_Annex_A.objects.filter(app_id=app_id)
    acad_annex_b = Acad_Annex_B.objects.filter(app_id=app_id)
    acad_annex_c = Acad_Annex_C.objects.filter(app_id=app_id)
    acad_annex_d = Acad_Annex_D.objects.filter(app_id=app_id)
    acad_annex_e12 = Acad_Annex_E12.objects.filter(app_id=app_id)
    acad_annex_f = Acad_Annex_F.objects.filter(app_id=app_id)
    acad_annex_g = Acad_Annex_G.objects.filter(app_id=app_id)
    acad_annex_h = Acad_Annex_H.objects.filter(app_id=app_id)
    acad_annex_i = Acad_Annex_I.objects.filter(app_id=app_id)
    acad_annex_j = Acad_Annex_J.objects.filter(app_id=app_id)
    acad_annex_k = Acad_Annex_K.objects.filter(app_id=app_id)
    acad_annex_l = Acad_Annex_L.objects.filter(app_id=app_id)
    acad_annex_m = Acad_Annex_M.objects.filter(app_id=app_id)
    acad_annex_n = Acad_Annex_N.objects.filter(app_id=app_id)
    acad_annex_o = Acad_Annex_O.objects.filter(app_id=app_id)
    acad_annex_p = Acad_Annex_P.objects.filter(app_id=app_id)
    acad_annex_q = Acad_Annex_Q.objects.filter(app_id=app_id)
    acad_annex_r = Acad_Annex_R.objects.filter(app_id=app_id)
    acad_annex_s = Acad_Annex_S.objects.filter(app_id=app_id)
    acad_annex_t = Acad_Annex_T.objects.filter(app_id=app_id)
    acad_annex_u = Acad_Annex_U.objects.filter(app_id=app_id)
    acad_annex_v = Acad_Annex_V.objects.filter(app_id=app_id)
    acad_annex_w1_w2 = Acad_Annex_W1_W2.objects.filter(app_id=app_id)
    acad_annex_x = Acad_Annex_X.objects.filter(app_id=app_id)
    acad_annex_y = Acad_Annex_Y.objects.filter(app_id=app_id)
    acad_annex_z = Acad_Annex_Z.objects.filter(app_id=app_id)

    if acad_annex_a.count() > 0:
        response['acad_annex_a'] = acad_annex_a[0].annexure_file

    if acad_annex_b.count() > 0:
        response['acad_annex_b'] = acad_annex_b[0].annexure_file
    if acad_annex_c.count() > 0:
        response['acad_annex_c'] = acad_annex_c[0].annexure_file

    if acad_annex_d.count() > 0:
        response['acad_annex_d'] = acad_annex_d[0].annexure_file

    if acad_annex_e12.count() > 0:
        response['acad_annex_e1'] = acad_annex_e12[0].annexure_file_e1
        response['acad_annex_e2'] = acad_annex_e12[0].annexure_file_e2
        # response['total_e'] = float(acad_annex_e12[0].total_e1 + acad_annex_e12[0].total_e2)

    if acad_annex_f.count() > 0:
        response['acad_annex_f'] = acad_annex_f[0].annexure_file

    if acad_annex_g.count() > 0:
        response['acad_annex_g'] = acad_annex_g[0].annexure_file

    if acad_annex_h.count() > 0:
        response['acad_annex_h'] = acad_annex_h[0].annexure_file

    if acad_annex_i.count() > 0:
        response['acad_annex_i'] = acad_annex_i[0].annexure_file

    if acad_annex_j.count() > 0:
        response['acad_annex_j'] = acad_annex_j[0].annexure_file

    if acad_annex_k.count() > 0:
        response['acad_annex_k'] = acad_annex_k[0].annexure_file

    if acad_annex_l.count() > 0:
        response['acad_annex_l'] = acad_annex_l[0].annexure_file

    if acad_annex_m.count() > 0:
        response['acad_annex_m'] = acad_annex_m[0].annexure_file

    if acad_annex_n.count() > 0:
        response['acad_annex_n'] = acad_annex_n[0].annexure_file

    if acad_annex_o.count() > 0:
        response['acad_annex_o'] = acad_annex_o[0].annexure_file

    if acad_annex_p.count() > 0:
        response['acad_annex_p'] = acad_annex_p[0].annexure_file

    if acad_annex_q.count() > 0:
        response['acad_annex_q'] = acad_annex_q[0].annexure_file  

    if acad_annex_r.count() > 0:
        response['acad_annex_r'] = acad_annex_r[0].annexure_file

    if acad_annex_s.count() > 0:
        response['acad_annex_s'] = acad_annex_s[0].annexure_file

    if acad_annex_t.count() > 0:
        response['acad_annex_t'] = acad_annex_t[0].annexure_file

    if acad_annex_u.count() > 0:
        response['acad_annex_u'] = acad_annex_u[0].annexure_file

    if acad_annex_v.count() > 0:
        response['acad_annex_v'] = acad_annex_v[0].annexure_file

    if acad_annex_w1_w2.count() > 0:
        response['acad_annex_w1'] = acad_annex_w1_w2[0].annexure_file_w1
        response['acad_annex_w2'] = acad_annex_w1_w2[0].annexure_file_w2
        # response['total_w'] = float(acad_annex_w1_w2[0].total_w1 + acad_annex_w1_w2[0].total_w2)

    if acad_annex_x.count() > 0:
        response['acad_annex_x'] = acad_annex_x[0].annexure_file

    if acad_annex_y.count() > 0:
        response['acad_annex_y'] = acad_annex_y[0].annexure_file

    if acad_annex_z.count() > 0:
        response['acad_annex_z'] = acad_annex_z[0].annexure_file

    if Paper.objects.filter(app_id=app_id).exists() :
        obj = Paper.objects.get(app_id=app_id)
        response['expDoc'] = obj.paper1

    return render(request, 'recruit/all_annexures.djt', response)

@login_required(login_url='/faculty_login/')
@user_passes_test(checkuserifmasteruser,login_url="/faculty_login/")
def pass_reset(request):
    users = User.objects.filter(groups__name='scrutiny')
    if request.method == 'POST':
        uname = request.POST['uname']
        passwd = request.POST['pass']
        u = User.objects.get(username=uname)
        try:
            u.set_password(passwd)
            u.save()
            return render(request, 'recruit/pass_reset.djt', {'users': users, 'err': 'Password reset successful'})
        except:
            return render(request, 'recruit/pass_reset.djt', {'users': users, 'err': 'Password reset failed'})

    return render(request, 'recruit/pass_reset.djt', {'users': users})

@login_required(login_url='/faculty_login/')
@user_passes_test(checkuserifmasteruser,login_url="/faculty_login/")
def call_letter_blank(request):
	if request.method != 'POST':
		depts = Department.objects.all()
		posts = Post.objects.all()
		return render(request, 'recruit/call_letter_blank.djt', {'depts':depts, 'posts':posts})
		
	if request.POST['post'] == '4':
		cl_id = 3
	else:
		cl_id = request.POST['post']
	if request.POST['dept'] == '100':
		data = {'dept':{'id':100, 'name': 'Physical Education Department'}, 'post': Post.objects.get(id=cl_id), 'is_nitw':1, 'interview_time': '2018-03-14 10:00:00+00:00'}
		phy = True
	else:
		phy = False
		data = CallLetter.objects.get(dept=Department.objects.get(id=request.POST['dept']), post=Post.objects.get(id=cl_id), is_nitw=True)
		data.post.id = int(request.POST['post'])
		if request.POST['batch'] == '2':
			data.report_time = data.report_time + datetime.timedelta(days=1)
			data.seminar_time = data.seminar_time + datetime.timedelta(days=1)
			data.interview_time = data.interview_time + datetime.timedelta(days=1)
	short = {}
	short['agp'] = request.POST['agp']#Post.objects.get(id=request.POST['post']).name if request.POST['post'] != '4' else 'Professor (HAG Scale)'
	short['is_accepted'] = 1
	if 'disc' in request.POST:
		disc = True
	else:
		disc = False
	disc_no = request.POST['disc_no']

	disp_no, disp_date, refno, dispcb = '', '', '', False
	if 'disp' in request.POST:
		dispcb = True
		disp_no = request.POST['disp_no']
		disp_date = request.POST['disp_date']
		refno = request.POST['refno']
	return render(request, 'recruit/call_letter.djt', {'data':data, 'app_id':request.POST['app_id'], 'name':request.POST['name'], 'addr':request.POST['addr'].split(','), 'short':short, 'custom':True, 'disc':disc, 'disc_no':disc_no, 'phy':phy, 'dispcb':dispcb, 'disp_no':disp_no, 'disp_date': disp_date, 'refno':refno})

@login_required(login_url='/faculty_login/')
@user_passes_test(checkuserifmasteruser,login_url="/faculty_login/")
def gen_shortlist_admin(request):
	depts = Department.objects.all()
	ds = []
	for dept in depts:
		# if True not in CallLetter.objects.filter(dept=dept).values_list('is_sent', flat=True):
		ds.append(dept)
	return render(request, 'recruit/gen_shortlist_admin.djt', {'depts':ds})

@login_required(login_url='/faculty_login/')
@user_passes_test(checkuserifmasteruser,login_url="/faculty_login/")
def gen_dets(request, dept_id):
	if checkuserifmasteruser(request.user):
		dept=Department.objects.get(id=dept_id)
		if dept.id == 9:
		    MULT = [7,6,6,6] #ur, sc, st, obc
		elif dept.id == 2:
		    MULT = [6,6,6,6] #ur, sc, st, obc
		else:
		    MULT = [5,5,5,5] #ur, sc, st, obc
		v = Vacancy.objects.get(dept=dept)
		ur_1_x = ScrutinizedValues.objects.filter(app_id__post_in=dept.name, app_id__post_for=Post.objects.get(id=1).name, application_status=3).order_by('-scrutiny_total').values_list('app_id__app_id', flat=True)
		ur_1 = list(ur_1_x[:v.ur_1*MULT[0]])
		if ur_1 != []:
		    cutoff = ScrutinizedValues.objects.get(app_id=Appdata.objects.get(app_id=ur_1[-1])).scrutiny_total
		    for app in ur_1_x[v.ur_1*MULT[0]:]:
		        if ScrutinizedValues.objects.get(app_id=Appdata.objects.get(app_id=app)).scrutiny_total == cutoff:
		            ur_1.append(app)
		for app in ur_1_x[v.ur_1*MULT[0]:]:
		    if Appdata.objects.get(app_id=app).is_nitw:
		        ur_1.append(app)
		sc_1_x, st_1_x, obc_1_x = [], [], []
		other = ScrutinizedValues.objects.filter(app_id__post_in=dept.name, app_id__post_for=Post.objects.get(id=1).name, application_status=3).exclude(app_id__app_id__in=ur_1).order_by('-scrutiny_total').values_list('app_id__app_id', flat=True)
		for e in other:
		    f = FacUser.objects.get(app_id=Appdata.objects.get(app_id=e))
		    if f.category == 'SC':
		        sc_1_x.append(f.app_id.app_id)
		    elif f.category == 'ST':
		        st_1_x.append(f.app_id.app_id)
		    elif f.category == 'OBC':
		        obc_1_x.append(f.app_id.app_id)
		sc_1 = sc_1_x[:v.sc_1*MULT[1]]
		if sc_1 != []:
		    cutoff = ScrutinizedValues.objects.get(app_id=Appdata.objects.get(app_id=sc_1[-1])).scrutiny_total
		    for app in sc_1_x[v.sc_1*MULT[1]:]:
		        if ScrutinizedValues.objects.get(app_id=Appdata.objects.get(app_id=app)).scrutiny_total == cutoff:
		            sc_1.append(app)
		for app in sc_1_x[v.sc_1*MULT[0]:]:
		    if Appdata.objects.get(app_id=app).is_nitw:
		        sc_1.append(app)
		st_1 = st_1_x[:v.st_1*MULT[1]]
		if st_1 != []:
		    cutoff = ScrutinizedValues.objects.get(app_id=Appdata.objects.get(app_id=st_1[-1])).scrutiny_total
		    for app in st_1_x[v.st_1*MULT[1]:]:
		        if ScrutinizedValues.objects.get(app_id=Appdata.objects.get(app_id=app)).scrutiny_total == cutoff:
		            st_1.append(app)
		for app in st_1_x[v.st_1*MULT[1]:]:
		    if Appdata.objects.get(app_id=app).is_nitw:
		        st_1.append(app)
		obc_1 = obc_1_x[:v.obc_1*MULT[1]]
		if obc_1 != []:
		    cutoff = ScrutinizedValues.objects.get(app_id=Appdata.objects.get(app_id=obc_1[-1])).scrutiny_total
		    for app in obc_1_x[v.obc_1*MULT[1]:]:
		        if ScrutinizedValues.objects.get(app_id=Appdata.objects.get(app_id=app)).scrutiny_total == cutoff:
		            obc_1.append(app)
		for app in obc_1_x[v.obc_1*MULT[1]:]:
		    if Appdata.objects.get(app_id=app).is_nitw:
		        obc_1.append(app)
		all_2 = ScrutinizedValues.objects.filter(app_id__post_in=dept.name, app_id__post_for=Post.objects.get(id=2).name, application_status=3).order_by('-scrutiny_total').values_list('app_id__app_id', flat=True)
		all_3 = ScrutinizedValues.objects.filter(app_id__post_in=dept.name, app_id__post_for=Post.objects.get(id=3).name, application_status=3).order_by('-scrutiny_total').values_list('app_id__app_id', flat=True)

		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename="'+dept.name+'.csv"'

		writer = csv.writer(response)
		writer.writerow(['Application ID', 'Full Name', 'Int/Ext', 'Age', 'PWD', 'Category', 'Shortlisted Category', 'Applied AGPs', 'Shortlisted AGP', 'Shortlisted Batch'])
		for app in all_3:
			a = Appdata.objects.get(app_id=app)
			fu = FacUser.objects.get(app_id=a)
			res = [app, fu.full_name, a.is_nitw, fu.age, fu.pwd, fu.category, fu.category, str(a.agp1)+str(a.agp2)+str(a.agp3)]
			try:
				s = Shortlist.objects.get(app_id=a)
				res += [s.agp, s.batch]
			except:
				pass
			writer.writerow(res)
		for app in all_2:
			a = Appdata.objects.get(app_id=app)
			fu = FacUser.objects.get(app_id=a)
			res = [app, fu.full_name, a.is_nitw, fu.age, fu.pwd, fu.category, fu.category, str(a.agp1)+str(a.agp2)+str(a.agp3)]
			try:
				s = Shortlist.objects.get(app_id=a)
				res += [s.agp, s.batch]
			except:
				pass
			writer.writerow(res)
		for app in ur_1:
			a = Appdata.objects.get(app_id=app)
			fu = FacUser.objects.get(app_id=a)
			res = [app, fu.full_name, a.is_nitw, fu.age, fu.pwd, fu.category, 'UR/'+fu.category, str(a.agp1)+str(a.agp2)+str(a.agp3)]
			try:
				s = Shortlist.objects.get(app_id=a)
				res += [s.agp, s.batch]
			except:
				pass
			writer.writerow(res)
		for app in obc_1:
			a = Appdata.objects.get(app_id=app)
			fu = FacUser.objects.get(app_id=a)
			res = [app, fu.full_name, a.is_nitw, fu.age, fu.pwd, fu.category, fu.category, str(a.agp1)+str(a.agp2)+str(a.agp3)]
			try:
				s = Shortlist.objects.get(app_id=a)
				res += [s.agp, s.batch]
			except:
				pass
			writer.writerow(res)
		for app in sc_1:
			a = Appdata.objects.get(app_id=app)
			fu = FacUser.objects.get(app_id=a)
			res = [app, fu.full_name, a.is_nitw, fu.age, fu.pwd, fu.category, fu.category, str(a.agp1)+str(a.agp2)+str(a.agp3)]
			try:
				s = Shortlist.objects.get(app_id=a)
				res += [s.agp, s.batch]
			except:
				pass
			writer.writerow(res)
		for app in st_1:
			a = Appdata.objects.get(app_id=app)
			fu = FacUser.objects.get(app_id=a)
			res = [app, fu.full_name, a.is_nitw, fu.age, fu.pwd, fu.category, fu.category, str(a.agp1)+str(a.agp2)+str(a.agp3)]
			try:
				s = Shortlist.objects.get(app_id=a)
				res += [s.agp, s.batch]
			except:
				pass
			writer.writerow(res)
		return response

MULT = [5,5,5,5] #ur, sc, st, obc

@login_required(login_url='/faculty_login/')
@user_passes_test(checkuserifmasteruser,login_url="/faculty_login/")
def gen_shortlist(request, dept_id):
    if checkuserifmasteruser(request.user):
        dept=Department.objects.get(id=dept_id)
        if dept.id == 9:
        	MULT = [7,6,6,6] #ur, sc, st, obc
        elif dept.id == 2:
        	MULT = [6,6,6,6] #ur, sc, st, obc
        else:
        	MULT = [5,5,5,5] #ur, sc, st, obc
        v = Vacancy.objects.get(dept=dept)
        ur_1_x = ScrutinizedValues.objects.filter(app_id__post_in=dept.name, app_id__post_for=Post.objects.get(id=1).name, application_status=3).order_by('-scrutiny_total').values_list('app_id__app_id', flat=True)
        ur_1 = list(ur_1_x[:v.ur_1*MULT[0]])
        if ur_1 != []:
	        cutoff = ScrutinizedValues.objects.get(app_id=Appdata.objects.get(app_id=ur_1[-1])).scrutiny_total
	        for app in ur_1_x[v.ur_1*MULT[0]:]:
	        	if ScrutinizedValues.objects.get(app_id=Appdata.objects.get(app_id=app)).scrutiny_total == cutoff:
	        		ur_1.append(app)
        for app in ur_1_x[v.ur_1*MULT[0]:]:
            if Appdata.objects.get(app_id=app).is_nitw:
                ur_1.append(app)
        if dept.id == 10:
        	ur_1.append('170710188')
        sc_1_x, st_1_x, obc_1_x = [], [], []
        other = ScrutinizedValues.objects.filter(app_id__post_in=dept.name, app_id__post_for=Post.objects.get(id=1).name, application_status=3).exclude(app_id__app_id__in=ur_1).order_by('-scrutiny_total').values_list('app_id__app_id', flat=True)
        for e in other:
            f = FacUser.objects.get(app_id=Appdata.objects.get(app_id=e))
            if f.category == 'SC':
                sc_1_x.append(f.app_id.app_id)
            elif f.category == 'ST':
                st_1_x.append(f.app_id.app_id)
            elif f.category == 'OBC':
                obc_1_x.append(f.app_id.app_id)
        sc_1 = sc_1_x[:v.sc_1*MULT[1]]
        if sc_1 != []:
	        cutoff = ScrutinizedValues.objects.get(app_id=Appdata.objects.get(app_id=sc_1[-1])).scrutiny_total
	        for app in sc_1_x[v.sc_1*MULT[1]:]:
	        	if ScrutinizedValues.objects.get(app_id=Appdata.objects.get(app_id=app)).scrutiny_total == cutoff:
	        		sc_1.append(app)
        for app in sc_1_x[v.sc_1*MULT[0]:]:
            if Appdata.objects.get(app_id=app).is_nitw:
                sc_1.append(app)
        st_1 = st_1_x[:v.st_1*MULT[1]]
        if st_1 != []:
	        cutoff = ScrutinizedValues.objects.get(app_id=Appdata.objects.get(app_id=st_1[-1])).scrutiny_total
	        for app in st_1_x[v.st_1*MULT[1]:]:
	        	if ScrutinizedValues.objects.get(app_id=Appdata.objects.get(app_id=app)).scrutiny_total == cutoff:
	        		st_1.append(app)
        for app in st_1_x[v.st_1*MULT[1]:]:
            if Appdata.objects.get(app_id=app).is_nitw:
                st_1.append(app)
        obc_1 = obc_1_x[:v.obc_1*MULT[1]]
        if obc_1 != []:
	        cutoff = ScrutinizedValues.objects.get(app_id=Appdata.objects.get(app_id=obc_1[-1])).scrutiny_total
	        for app in obc_1_x[v.obc_1*MULT[1]:]:
	        	if ScrutinizedValues.objects.get(app_id=Appdata.objects.get(app_id=app)).scrutiny_total == cutoff:
	        		obc_1.append(app)
        for app in obc_1_x[v.obc_1*MULT[1]:]:
            if Appdata.objects.get(app_id=app).is_nitw:
                obc_1.append(app)
        all_2 = ScrutinizedValues.objects.filter(app_id__post_in=dept.name, app_id__post_for=Post.objects.get(id=2).name, application_status=3).order_by('-scrutiny_total').values_list('app_id__app_id', flat=True)
        all_3 = ScrutinizedValues.objects.filter(app_id__post_in=dept.name, app_id__post_for=Post.objects.get(id=3).name, application_status=3).order_by('-scrutiny_total').values_list('app_id__app_id', flat=True)
        if request.method == 'POST':
            a = list(ur_1)+list(sc_1)+list(st_1)+list(obc_1)+list(all_2)+list(all_3)
            for app in a:
                if 'agp_'+app in request.POST and 'batch_'+app in request.POST:
                    n = Appdata.objects.get(app_id=app)
                    if Shortlist.objects.filter(app_id=n).exists():
                        var = Shortlist.objects.get(app_id=n)
                        var.agp = request.POST['agp_'+app]
                        var.batch = int(request.POST['batch_'+app])
                        var.save()
                    else:
                        var = Shortlist(app_id=n, msg_id='', is_msg_sent=False, is_mail_sent=False, is_accepted=0, agp=request.POST['agp_'+app], batch=request.POST['batch_'+app])
                        var.save()
            return redirect('/recruit/gen_shortlist/'+str(dept_id))
        dit = {}
        for no in (list(ur_1)+list(sc_1)+list(st_1)+list(obc_1)+list(all_2)+list(all_3)):
            p = Appdata.objects.get(app_id=no)
            dit[no] = {}
            dit[no]['f'] = FacUser.objects.get(app_id=p)
            dit[no]['a'] = p
            dit[no]['s'] = ScrutinizedValues.objects.get(app_id=p)
            if Shortlist.objects.filter(app_id=p).exists():
                dit[no]['h'] = Shortlist.objects.get(app_id=p)
        return render(request, 'recruit/gen_shortlist.djt', {'ur_1':ur_1, 'sc_1':sc_1, 'st_1':st_1, 'obc_1':obc_1, 'all_2':all_2, 'all_3':all_3, 'dit':sorted(dit.items(), key= lambda (k,v): v['s'].scrutiny_total, reverse=True), 'dept':dept})

@login_required(login_url='/faculty_login/')
@user_passes_test(checkuserifmasteruser,login_url="/faculty_login/")
def mailmsg_admin(request, type_id):
    if checkuserifmasteruser(request.user):
    	entries = CallLetter.objects.get(id=type_id)
    	apps = Shortlist.objects.filter(app_id__post_in=entries.dept.name, app_id__post_for=entries.post.name, app_id__is_nitw=entries.is_nitw).values_list('app_id__app_id', flat=True)
        dets = Appdata.objects.filter(app_id__in=apps)#.values_list('app_id__app_id', 'full_name')
        for det in dets:
            det.contact = UserProfile.objects.get(applicationID=det.app_id).contact
            det.acc = Shortlist.objects.get(app_id=det).is_accepted
    	mobs = UserProfile.objects.filter(applicationID__in=apps).values_list('contact', flat=True)
        apps1 = Shortlist.objects.filter(app_id__post_in=entries.dept.name, app_id__post_for=entries.post.name, app_id__is_nitw=entries.is_nitw, batch=1).values_list('app_id__app_id', flat=True)
        apps2 = Shortlist.objects.filter(app_id__post_in=entries.dept.name, app_id__post_for=entries.post.name, app_id__is_nitw=entries.is_nitw, batch=2).values_list('app_id__app_id', flat=True)
    	mails1 = list(User.objects.filter(username__in=apps1).values_list('email', flat=True))
        mails2 = list(User.objects.filter(username__in=apps2).values_list('email', flat=True))
    	body1 = render_to_string('recruit/mailmsg.djt', {'data':entries})
        entries2 = copy.deepcopy(entries)
        entries2.report_time = entries2.report_time + datetime.timedelta(days=1)
        entries2.seminar_time = entries2.seminar_time + datetime.timedelta(days=1)
        entries2.interview_time = entries2.interview_time + datetime.timedelta(days=1)
        body2 = render_to_string('recruit/mailmsg.djt', {'data':entries2})
    	msg = 'Dear Applicant, you are shortlisted for interview. Please check your mail for further instructions - Faculty Recruitment NITW'

    	if request.method == 'POST':
            connection = get_connection(host='smtp.gmail.com', port=587, username='recruitment17@nitw.ac.in', password='nitw12345', use_tls=True)
            if mails1 != []:
                try:
                    cls = EmailMultiAlternatives('Faculty Recruitment NITW', body1, 'recruitment17@nitw.ac.in', to=['recruitment_faculty@nitw.ac.in'], bcc=mails1, connection=connection)
                    cls.attach_alternative(body1, 'text/html')
                    cls.send(fail_silently=False)
                except Exception as e:
                    send_mail('FRNITW Error - '+str(type_id), str(e), 'recruitment17@nitw.ac.in', ['uvamsi@student.nitw.ac.in'], connection=connection, fail_silently=False)
            if mails2 != []:
                try:
                    cls2 = EmailMultiAlternatives('Faculty Recruitment NITW', body2, 'recruitment17@nitw.ac.in', to=['recruitment_faculty@nitw.ac.in'], bcc=mails2, connection=connection)
                    cls2.attach_alternative(body2, 'text/html')
                    cls2.send(fail_silently=False)
                except Exception as e:
                    send_mail('FRNITW Error - '+str(type_id), str(e), 'recruitment17@nitw.ac.in', ['uvamsi@student.nitw.ac.in'], connection=connection, fail_silently=False)
            msgurl = 'http://www.onlinebulksmslogin.com/spanelv2/api.php?username=nitwarangal1&password=nitwarangal2020&to=' + ','.join(mobs) + '&from=FRNITW&message=' + urllib2.quote(msg)
            entries.is_sent = True
            entries.send_date = datetime.datetime.now()
            entries.save()
            return HttpResponse(urllib2.urlopen(msgurl).read())
        
    	return render(request, 'recruit/mailmsg_admin.djt', {'entries':entries,'dets':dets})
    return redirect('/')

@login_required(login_url='/faculty_login/')
@user_passes_test(checkuserifmasteruser,login_url="/faculty_login/")
def print_cl(request, type_id):
    if checkuserifmasteruser(request.user):
        entries = CallLetter.objects.get(id=type_id)
        apps = Shortlist.objects.filter(app_id__post_in=entries.dept.name, app_id__post_for=entries.post.name, app_id__is_nitw=entries.is_nitw).values_list('app_id__app_id', flat=True)
        response = []
        for app in apps:
            shortlists = Shortlist.objects.get(app_id=Appdata.objects.get(app_id=app))
            appdata = Appdata.objects.get(app_id=app)
            try:
                facuser = FacUser.objects.get(app_id=app)
                name = facuser.full_name
                addr = facuser.correspond_addr
            except:
                name = ''
                addr = ''
            # data = CallLetter.objects.get(dept=Department.objects.get(name=appdata.post_in), post=Post.objects.get(name=appdata.post_for), is_nitw=entries.is_nitw)
            data = copy.deepcopy(entries)
            if shortlists.batch == 2:
                data.report_time = data.report_time + datetime.timedelta(days=1)
                data.seminar_time = data.seminar_time + datetime.timedelta(days=1)
                data.interview_time = data.interview_time + datetime.timedelta(days=1)
            response.append({'data': data, 'app_id': app, 'addr': addr.split(','), 'name': name, 'short':shortlists})
        return render(request, 'recruit/print_cl.djt', {'responses':response})

@login_required(login_url='/faculty_login/')
@user_passes_test(checkuserifmasteruser,login_url="/faculty_login/")
def call_letter_admin(request):
    if checkuserifmasteruser(request.user):
        if request.method == 'POST':
            for i in range(1, 85):
                entries = CallLetter.objects.get(dept=Department.objects.get(id=request.POST['dept_'+str(i)]), post=Post.objects.get(id=request.POST['post_'+str(i)]), is_nitw=request.POST['is_nitw_'+str(i)])
                entries.report_time = datetime.datetime.strptime(request.POST['report_time_'+str(i)], '%Y-%m-%d %H:%M')
                entries.seminar_time = request.POST['seminar_time_'+str(i)]
                entries.interview_time = request.POST['interview_time_'+str(i)]
                entries.seminar_place = request.POST['seminar_venue_'+str(i)]
                # entries.interview_venue = request.POST['interview_venue_'+str(i)]
                entries.send_time = request.POST['send_date_'+str(i)]
                entries.disp_no = request.POST['disp_no_'+str(i)]
                entries.save()
            return redirect('/call_letter_admin')
        entries = CallLetter.objects.all()
        return render(request, 'recruit/call_letter_admin.djt', {'types': entries})
    return redirect('/')

@login_required(login_url='/register/')
def call_letter_accept(request):
	app_id = request.user.username
	if request.method != 'POST' or ('checkbox' not in request.POST and 'acc' not in request.POST) or not Shortlist.objects.filter(app_id=Appdata.objects.get(app_id=app_id)).exists():
		return redirect('/')
	s = Shortlist.objects.get(app_id=Appdata.objects.get(app_id=app_id))
	if 'checkbox' in request.POST:
		s.is_accepted = 1
	if 'acc' in request.POST:
		s.is_accepted = request.POST['acc']
	s.save()
	return redirect('/call_letter')

@login_required(login_url='/register/')
def call_letter(request):
    app_id = request.user.username
    ad = Appdata.objects.get(app_id=app_id)
    if not Shortlist.objects.filter(app_id=ad).exists():
        return redirect('/printSummary')
    shortlists = Shortlist.objects.get(app_id=Appdata.objects.get(app_id=app_id))
    appdata = Appdata.objects.get(app_id=app_id)
    try:
        facuser = FacUser.objects.get(app_id=app_id)
        name = facuser.full_name
        addr = facuser.correspond_addr
    except:
        name = ''
        addr = ''
    data = CallLetter.objects.get(dept=Department.objects.get(name=appdata.post_in), post=Post.objects.get(name=appdata.post_for), is_nitw=appdata.is_nitw)
    if shortlists.batch == 2:
        data.report_time = data.report_time + datetime.timedelta(days=1)
        data.seminar_time = data.seminar_time + datetime.timedelta(days=1)
        data.interview_time = data.interview_time + datetime.timedelta(days=1)
    return render(request, 'recruit/call_letter.djt', {'data': data, 'app_id': app_id, 'addr': addr.split(','), 'name': name, 'short':shortlists})

@login_required(login_url='/faculty_login/')
@user_passes_test(checkuserifmasteruser,login_url="/faculty_login/")
@csrf_exempt
def getAppids(request):
    if checkuserifmasteruser(request.user):
    	if request.POST['short'] == '1':
        	ss = Shortlist.objects.all()
        	if request.POST['dept']:
        		ss = ss.filter(app_id__post_in=request.POST['dept'])
        	ids = ss.values_list('app_id__app_id', flat=True)
        	return HttpResponse(','.join(ids))
        facs = ScrutinizedValues.objects.filter(app_id__submitted=True, app_id__is_nitw=False, app_id__paymentUploaded=True)
        if request.POST['dept']:
            facs = facs.filter(app_id__post_in=request.POST['dept'])
        if request.POST['status']:
            facs = facs.filter(application_status=request.POST['status'])
        facs = facs.order_by('application_status', 'app_id__post_for')
        ids = list(facs.values_list('app_id__app_id', flat=True))
        return HttpResponse(','.join(ids))

@login_required(login_url='/faculty_login/')
@user_passes_test(checkuserifmasteruser,login_url="/faculty_login/")
def generate_pdf(request):
    if checkuserifmasteruser(request.user):
        if request.method != 'POST':
            response = {}
            # response['posts'] = Post.objects.all()
            response['departments'] = Department.objects.all()
            return render(request, 'recruit/csvinput.djt', response)
        sendlist = [i.strip('\n').strip('\s') for i in request.POST['sendlist'].split(',')]
        responses = []
        for app_id in sendlist:
            response = {}
            credit_total = 0.0
            system_total = 0.0
            annex_e1 = Acad_Annex_E12.objects.filter(app_id=app_id)
            response['annex_e1_total'] = 0.0
            if annex_e1.count() > 0:
                if annex_e1[0].annexure_file_e1:
                    response['annex_e1_file'] = annex_e1[0].annexure_file_e1
                if len(str((annex_e1[0].annexure_data_e1).encode("utf-8"))) > 1:
                    response['annex_e1'] = json.loads(annex_e1[0].annexure_data_e1)
                    total_e1 = float(annex_e1[0].total_e1)
                    response['annex_e1_total'] = total_e1
                    credit_total += total_e1
                    system_total += total_e1

            response['annex_e2_total'] = 0.0
            annex_e2 = Acad_Annex_E12.objects.filter(app_id=app_id)
            if annex_e2.count() > 0:
                if annex_e2[0].annexure_file_e2:
                    response['annex_e2_file'] = annex_e1[0].annexure_file_e2
                if len(str((annex_e2[0].annexure_data_e2).encode("utf-8"))) > 1:
                    response['annex_e2'] = json.loads(annex_e2[0].annexure_data_e2)
                    # total_patent=0
                    # pat_credit=0
                    # for item in response['annex_e2']:
                    #     total_patent+=1
                    #     pat_credit+=float(item['credit'])
                    # response['total_patent']=total_patent
                    # response['pat_credit']=pat_credit
                    total_e2 = float(annex_e2[0].total_e2)
                    response['annex_e2_total'] = total_e2
                    credit_total += total_e2
                    system_total += total_e2

            annex_f = Acad_Annex_F.objects.filter(app_id=app_id)
            if annex_f.count() > 0:
                if annex_f[0].annexure_file:
                    response['annex_f_file'] = annex_f[0].annexure_file
                if annex_f[0].annexure_data:
                    response['annex_f'] = json.loads(annex_f[0].annexure_data)
                    response['annex_f_credit'] = annex_f[0].credit_score
                    credit_total += annex_f[0].credit_score
                    
                    if(annex_f[0].credit_score > 10.0):
                        response['annex_f_system'] = 10.0
                        system_total += 10.0
                    else:
                        response['annex_f_system'] = annex_f[0].credit_score
                        system_total += annex_f[0].credit_score

            annex_g = Acad_Annex_G.objects.filter(app_id=app_id)
            if annex_g.count() > 0:
                if annex_g[0].annexure_file:
                    response['annex_g_file'] = annex_g[0].annexure_file
                if annex_g[0].annexure_data:
                    response['annex_g'] = json.loads(annex_g[0].annexure_data)
                    sole=0
                    sole_credit=0
                    superv=0
                    sup_credit=0
                    co=0
                    co_credit=0
                    total = 0.0
                    for item in response['annex_g']:
                        total += float(item['credit'])
                        if item['co_sup'] == 0:
                            sole+=1
                            sole_credit+=float(item['credit'])
                        elif item['role_main'][0]=='M' or item['role_main'][0]=='m':
                            superv+=1
                            sup_credit+=float(item['credit'])
                        else:
                            co+=1
                            co_credit+=float(item['credit'])
                    response['sole']=sole
                    response['sole_credit']=sole_credit
                    response['superv']=superv
                    response['sup_credit']=sup_credit
                    response['co']=co
                    response['co_credit']=co_credit
                    response['annex_g_total'] = total
                    credit_total += total
                    system_total += total

            # titles = []
            # scrutiny_h_indi = Scrutiny_h.objects.filter(app_id=app_id)
            # if scrutiny_h_indi.count() > 0:
            #     for i in scrutiny_h_indi:
            #         titles.append(i.single_annex_h)
            annex_h = Acad_Annex_H.objects.filter(app_id=app_id)
            if annex_h.count() > 0:
                if annex_h[0].annexure_file:
                    response['annex_h_file'] = annex_h[0].annexure_file

                if annex_h[0].annexure_data:
                    scrutiny_h_indi = Scrutiny_h.objects.filter(app_id=app_id)
                    data = json.loads(annex_h[0].annexure_data)
                    for index,h in enumerate(data):
                        data[index]['scrutinized_values'] = scrutiny_h_indi[index].points
                        data[index]['scrutinized_values2'] = scrutiny_h_indi[index].points2
                    response['annex_h'] = data
                    response['number_of_h'] = len(data)
                    response['annex_h_last_prom'] = annex_h[0].last_prom
                total = float(annex_h[0].total)
                response['annex_h_total'] = total
                credit_total += total
                system_total += total


            annex_i = Acad_Annex_I.objects.filter(app_id=app_id)
            if annex_i.count() > 0:
                if annex_i[0].annexure_file:
                    response['annex_i_file'] = annex_i[0].annexure_file
                if annex_i[0].annexure_data:
                    scrutiny_i_indi = Scrutiny_i.objects.filter(app_id=app_id)
                    data = json.loads(annex_i[0].annexure_data)
                    for index,h in enumerate(data):
                        data[index]['scrutinized_values'] = scrutiny_i_indi[index].points
                        data[index]['scrutinized_values2'] = scrutiny_i_indi[index].points2
                    response['annex_i'] = data
                    response['number_of_i'] = len(data)
                total = float(annex_i[0].total)
                response['annex_i_total'] = total
                credit_total += total
                if(total > 10.0):
                    response['annex_i_system'] = 10.0
                    system_total += 10.0
                else:
                    response['annex_i_system'] = total
                    system_total += total

            annex_j = Acad_Annex_J.objects.filter(app_id=app_id)
            if annex_j.count() > 0:
                if annex_j[0].annexure_file:
                    response['annex_j_file'] = annex_j[0].annexure_file
                if annex_j[0].annexure_data:
                    response['annex_j'] = json.loads(annex_j[0].annexure_data)
                    response['annex_j_credit'] = annex_j[0].credit_score
                    response['annex_j_last_prom'] = annex_j[0].last_prom
                    credit_total += annex_j[0].credit_score
                    if(annex_j[0].credit_score > 16.0):
                        response['annex_j_system'] = 16.0
                        system_total += 16.0
                    else:
                        response['annex_j_system'] = annex_j[0].credit_score
                        system_total += annex_j[0].credit_score

            annex_k = Acad_Annex_K.objects.filter(app_id=app_id)
            if annex_k.count() > 0:
                if annex_k[0].annexure_file:
                    response['annex_k_file'] = annex_k[0].annexure_file
                if annex_k[0].annexure_data:
                    response['annex_k'] = json.loads(annex_k[0].annexure_data)
                    response['annex_k_credit'] = annex_k[0].credit_score
                    response['annex_k_last_prom'] = annex_k[0].last_prom
                    credit_total += annex_k[0].credit_score
                    if(annex_k[0].credit_score > 8.0):
                        response['annex_k_system'] = 8.0
                        system_total += 8.0
                    else:
                        response['annex_k_system'] = annex_k[0].credit_score
                        system_total += annex_k[0].credit_score

            annex_l = Acad_Annex_L.objects.filter(app_id=app_id)
            if annex_l.count() > 0:
                if annex_l[0].annexure_file:
                    response['annex_l_file'] = annex_l[0].annexure_file
                if annex_l[0].annexure_data:
                    response['annex_l'] = json.loads(annex_l[0].annexure_data)
                    response['annex_l_last_prom'] = annex_l[0].last_prom
                    response['annex_l_credit'] = annex_l[0].credit_score
                    credit_total += annex_l[0].credit_score
                    if(annex_l[0].credit_score > 3.0):
                        response['annex_l_system'] = 3.0
                        system_total += 3.0
                    else:
                        response['annex_l_system'] = annex_l[0].credit_score
                        system_total += annex_l[0].credit_score


            annex_m = Acad_Annex_M.objects.filter(app_id=app_id)
            if annex_m.count() > 0:
                if annex_m[0].annexure_file:
                    response['annex_m_file'] = annex_m[0].annexure_file
                if annex_m[0].annexure_data:
                    response['annex_m'] = json.loads(annex_m[0].annexure_data)
                    response['annex_m_credit'] = annex_m[0].credit_score
                    response['annex_m_last_prom'] = annex_m[0].last_prom
                    credit_total += annex_m[0].credit_score
                    if(annex_m[0].credit_score > 3.0):
                        response['annex_m_system'] = 3.0
                        system_total += 3.0
                    else:
                        response['annex_m_system'] = annex_m[0].credit_score
                        system_total += annex_m[0].credit_score

            annex_n = Acad_Annex_N.objects.filter(app_id=app_id)
            if annex_n.count() > 0:
                if annex_n[0].annexure_file:
                    response['annex_n_file'] = annex_n[0].annexure_file
                if annex_n[0].annexure_data:
                    response['annex_n'] = json.loads(annex_n[0].annexure_data)
                    response['annex_n_last_prom'] = annex_n[0].last_prom
                    response['annex_n_credit'] = annex_n[0].total
                    response['total_noN'] = annex_n[0].total_number
                    credit_total += annex_n[0].total
                    if(annex_n[0].total > 8.0):
                        response['annex_n_system'] = 8.0
                        system_total += 8.0
                    else:
                        response['annex_n_system'] = annex_n[0].total
                        system_total += annex_n[0].total

            response['annex_o_credit'] = 0.0
            response['annex_o_system'] = 0.0
            annex_o = Acad_Annex_O.objects.filter(app_id=app_id)
            if annex_o.count() > 0:
                if annex_o[0].annexure_file:
                    response['annex_o_file'] = annex_o[0].annexure_file
                if annex_o[0].annexure_data:
                    response['annex_o'] = json.loads(annex_o[0].annexure_data)
                    response['annex_o_last_prom'] = annex_o[0].last_prom
                    response['prog_2_week_duration']=annex_o[0].prog_2_week_duration
                    response['prog_1_week_duration']=annex_o[0].prog_1_week_duration
                    response['annex_o_credit'] = annex_o[0].total
                    response['annex_o_system'] = annex_o[0].total
                    credit_total += annex_o[0].total
                    system_total += annex_o[0].total

            response['annex_p_credit'] = 0.0
            response['annex_p_system'] = 0.0
            annex_p = Acad_Annex_P.objects.filter(app_id=app_id)
            if annex_p.count() > 0:
                if annex_p[0].annexure_file:
                    response['annex_p_file'] = annex_p[0].annexure_file
                if annex_p[0].annexure_data:
                    response['annex_p'] = json.loads(annex_p[0].annexure_data)
                    response['annex_p_last_prom'] = annex_p[0].last_prom
                    response['annex_p_credit'] = annex_p[0].total
                    response['total_noP'] = annex_p[0].total_number
                    credit_total += annex_p[0].total
                    if(annex_p[0].total > 6.0):
                        response['annex_p_system'] = 6.0
                        system_total += 6.0
                    else:
                        response['annex_p_system'] = annex_p[0].total
                        system_total += annex_p[0].total

            response['annex_q_credit'] = 0.0
            response['annex_q_system'] = 0.0
            annex_q = Acad_Annex_Q.objects.filter(app_id=app_id)
            if annex_q.count() > 0:
                if annex_q[0].annexure_file:
                    response['annex_q_file'] = annex_q[0].annexure_file
                if annex_q[0].annexure_data:
                    response['annex_q'] = json.loads(annex_q[0].annexure_data)
                    response['annex_q_last_prom'] = annex_q[0].last_prom
                    response['annex_q_exp_phd'] = annex_q[0].total_exp_after_phd
                    response['annex_q_exp_cur'] = annex_q[0].total_exp_cur
                    response['annex_q_tot_exp'] = annex_q[0].total_exp
                    response['annex_q_credit'] = annex_q[0].credit_score
                    response['total_yearsQ']=annex_q[0].total_years
                    response['total_monthsQ']=annex_q[0].total_months
                    credit_total += annex_q[0].credit_score
                    if(annex_q[0].credit_score > 10.0):
                        response['annex_q_system'] = 10.0
                        system_total += 10.0
                    else:
                        response['annex_q_system'] = annex_q[0].credit_score
                        system_total += annex_q[0].credit_score

            response['annex_r_credit'] = 0.0
            response['annex_r_system'] = 0.0
            annex_r = Acad_Annex_R.objects.filter(app_id=app_id)
            if annex_r.count() > 0:
                if annex_r[0].annexure_file:
                    response['annex_r_file'] = annex_r[0].annexure_file
                if annex_r[0].annexure_data:
                    response['annex_r'] = json.loads(annex_r[0].annexure_data)
                    response['annex_r_last_prom'] = annex_r[0].last_prom
                    response['annex_r_credit']=annex_r[0].total
                    response['total_numberR']=annex_r[0].total_number
                    response['annex_r_system'] = annex_r[0].total
                    credit_total += annex_r[0].total
                    system_total += annex_r[0].total

            response['annex_s_credit'] = 0.0
            response['annex_s_system'] = 0.0
            annex_s = Acad_Annex_S.objects.filter(app_id=app_id)
            if annex_s.count() > 0:
                if annex_s[0].annexure_file:
                    response['annex_s_file'] = annex_s[0].annexure_file
                if annex_s[0].annexure_data:
                    response['annex_s'] = json.loads(annex_s[0].annexure_data)
                    response['annex_s_last_prom'] = annex_s[0].last_prom
                    response['annex_s_extra_load'] = annex_s[0].extra_load
                    response['annex_s_credit'] = annex_s[0].credit_score
                    credit_total += annex_s[0].credit_score
                    if(annex_s[0].credit_score > 15.0):
                        response['annex_s_system'] = 15.0
                        system_total += 15.0
                    else:
                        response['annex_s_system'] = annex_s[0].credit_score
                        system_total += annex_s[0].credit_score

            response['annex_t_total'] = 0.0
            response['annex_t_system'] = 0.0
            annex_t = Acad_Annex_T.objects.filter(app_id=app_id)
            if annex_t.count() > 0:
                if annex_t[0].annexure_file:
                    response['annex_t_file'] = annex_t[0].annexure_file
                if annex_t[0].annexure_data:
                    response['annex_t'] = json.loads(annex_t[0].annexure_data)
                    response['annex_t_last_prom'] = annex_t[0].last_prom
                total = float(annex_t[0].total)
                response['annex_t_total'] = total
                credit_total += total
                if(total > 10.0):
                    response['annex_t_system'] = 10.0
                    system_total += 10.0
                else:
                    response['annex_t_system'] = total
                    system_total += total

            response['annex_u_total'] = 0.0
            response['annex_u_system'] = 0.0
            annex_u = Acad_Annex_U.objects.filter(app_id=app_id)
            if annex_u.count() > 0:
                if annex_u[0].annexure_file:
                    response['annex_u_file'] = annex_u[0].annexure_file
                if annex_u[0].annexure_data:
                    response['annex_u'] = json.loads(annex_u[0].annexure_data)
                    response['annex_u_last_prom'] = annex_u[0].last_prom
                total = float(annex_u[0].total)
                response['annex_u_total'] = total
                credit_total += total
                if(total > 4.0):
                    response['annex_u_system'] = 4.0
                    system_total += 4.0
                else:
                    response['annex_u_system'] = total
                    system_total += total

            response['annex_v_total'] = 0.0
            response['annex_v_system'] = 0.0
            annex_v = Acad_Annex_V.objects.filter(app_id=app_id)
            if annex_v.count() > 0:
                if annex_v[0].annexure_file:
                    response['annex_v_file'] = annex_v[0].annexure_file
                if annex_v[0].annexure_data:
                    response['annex_v'] = json.loads(annex_v[0].annexure_data)
                    response['annex_v_last_prom'] = annex_v[0].last_prom
                total = float(annex_v[0].total)
                response['annex_v_total'] = total
                credit_total += total
                if(total > 18.0):
                    response['annex_v_system'] = 18.0
                    system_total += 18.0
                else:
                    response['annex_v_system'] = total
                    system_total += total

            response['annex_w1_total'] = 0.0
            response['annex_w1_system'] = 0.0
            total_w = 0.0
            annex_w1 = Acad_Annex_W1_W2.objects.filter(app_id=app_id)
            if annex_w1.count() > 0:
                if annex_w1[0].annexure_file_w1:
                    response['annex_w1_file'] = annex_w1[0].annexure_file_w1
                if len(str((annex_w1[0].annexure_data1).encode("utf-8"))) > 1:
                    response['annex_w1'] = json.loads(annex_w1[0].annexure_data1)
                    response['annex_w1_last_prom'] = annex_w1[0].last_prom_w1
                    response['annex_w1_total'] = annex_w1[0].total_w1
                    total_w += annex_w1[0].total_w1
                    if(total_w > 6.0):
                        response['annex_w1_system'] = 6.0
                        system_total += 6.0
                    else:
                        response['annex_w1_system'] = total_w
                        system_total += total_w


            response['annex_w2_total'] = 0.0
            response['annex_w2_system'] = 0.0
            annex_w2 = Acad_Annex_W1_W2.objects.filter(app_id=app_id)
            if annex_w2.count() > 0:
                if annex_w2[0].annexure_file_w2:
                    response['annex_w2_file'] = annex_w2[0].annexure_file_w2
                if len(str((annex_w2[0].annexure_data2).encode("utf-8"))) > 1:
                    response['annex_w2'] = json.loads(annex_w2[0].annexure_data2)
                    response['annex_w2_last_prom'] = annex_w2[0].last_prom_w2
                    response['annex_w2_total'] = annex_w2[0].total_w2
                    total_w += annex_w2[0].total_w2
                    if(annex_w2[0].total_w2 > 6.0):
                        response['annex_w2_system'] = 6.0
                        system_total += 6.0
                    else:
                        response['annex_w2_system'] = annex_w2[0].total_w2
                        system_total += annex_w2[0].total_w2

            response['annex_w_total'] = total_w
            credit_total += total_w

            response['annex_x_total'] = 0.0
            response['annex_x_system'] = 0.0
            annex_x = Acad_Annex_X.objects.filter(app_id=app_id)
            if annex_x.count() > 0:
                if annex_x[0].annexure_file:
                    response['annex_x_file'] = annex_x[0].annexure_file
                if len(str((annex_x[0].annexure_data).encode("utf-8"))) > 1:
                    response['annex_x'] = json.loads(annex_x[0].annexure_data)
                    response['annex_x_last_prom'] = annex_x[0].last_prom
                    total = float(annex_x[0].total)
                    response['annex_x_total'] = total
                    credit_total += total
                    if(total > 4.0):
                        response['annex_x_system'] = 4.0
                        system_total += 4.0
                    else:
                        response['annex_x_system'] = total
                        system_total += total

            response['annex_y_credit'] = 0.0
            response['annex_y_system'] = 0.0
            annex_y = Acad_Annex_Y.objects.filter(app_id=app_id)
            if annex_y.count() > 0:
                if annex_y[0].annexure_file:
                    response['annex_y_file'] = annex_y[0].annexure_file
                response['annex_y_credit'] = annex_y[0].credit_score
                if annex_y[0].ieee:
                    response['annex_y_ieee'] = 'IEEE'
                    response['annex_y_area'] = True
                if annex_y[0].fna:
                    response['annex_y_fna'] = 'FNA'
                    response['annex_y_area'] = True
                if annex_y[0].fnae:
                    response['annex_y_fnae'] = 'FNAE'
                    response['annex_y_area'] = True
                if annex_y[0].fnasc:
                    response['annex_y_fnasc'] = 'FNASC'
                    response['annex_y_area'] = True
                credit_total += annex_y[0].credit_score
                if(annex_y[0].credit_score > 10.0):
                    response['annex_y_system'] = 10.0
                    system_total += 10.0
                else:
                    response['annex_y_system'] = annex_y[0].credit_score
                    system_total += annex_y[0].credit_score

            response['annex_z_total'] = 0.0
            response['annex_z_system'] = 0.0
            annex_z = Acad_Annex_Z.objects.filter(app_id=app_id)
            if annex_z.count() > 0:
                if annex_z[0].annexure_file:
                    response['annex_z_file'] = annex_z[0].annexure_file
                if len(str((annex_z[0].annexure_data).encode("utf-8"))) > 1:
                    response['annex_z'] = json.loads(annex_z[0].annexure_data)
                    response['annex_z_last_prom'] = annex_z[0].last_prom
                    response['annex_z_percentage'] = annex_z[0].percentage
                    total = float(annex_z[0].total)
                    response['annex_z_total'] = total
                    credit_total += total
                    if annex_z[0].percentage >= 85:
                        if(total > 20.0):
                            response['annex_z_system'] = 20.0
                            system_total += 20.0
                        else:
                            response['annex_z_system'] = total
                            system_total += total
                    elif annex_z[0].percentage < 85 and annex_z[0].percentage >= 75:
                        if(total > 10.0):
                            response['annex_z_system'] = 10.0
                            system_total += 10.0
                    else:
                        response['annex_z_system'] = total
                        system_total += total

            annex_a = Acad_Annex_A.objects.filter(app_id=app_id)
            if annex_a.count() > 0:
                if annex_a[0].annexure_file:
                    response['annex_a_file'] = annex_a[0].annexure_file
                if len(str((annex_a[0].annexure_data).encode("utf-8"))) > 1:
                    response['annex_a'] = json.loads(annex_a[0].annexure_data)
            facuser = FacUser.objects.get(app_id=app_id)
            # response['app']=app_id

            response['fac']=facuser
            college = Constants.objects.filter(key='college')
            if college.count() > 0:
                response['college'] = college[0].value

            scrutinized_values = ScrutinizedValues.objects.filter(app_id=app_id)
            if scrutinized_values.count() > 0:
                response['Sc_annex_e1']=scrutinized_values[0].annex_e1
                response['Sc_annex_e2']=scrutinized_values[0].annex_e2
                response['Sc_annex_f']=scrutinized_values[0].annex_f
                response['Sc_annex_g']=scrutinized_values[0].annex_g
                response['Sc_annex_h']=scrutinized_values[0].annex_h
                response['Sc_annex_i']=scrutinized_values[0].annex_i
                response['Sc_annex_j']=scrutinized_values[0].annex_j
                response['Sc_annex_k']=scrutinized_values[0].annex_k
                response['Sc_annex_l']=scrutinized_values[0].annex_l
                response['Sc_annex_m']=scrutinized_values[0].annex_m
                response['Sc_annex_n']=scrutinized_values[0].annex_n
                response['Sc_annex_o']=scrutinized_values[0].annex_o
                response['Sc_annex_p']=scrutinized_values[0].annex_p
                response['Sc_annex_q']=scrutinized_values[0].annex_q
                response['Sc_annex_r']=scrutinized_values[0].annex_r
                response['Sc_annex_s']=scrutinized_values[0].annex_s
                response['Sc_annex_t']=scrutinized_values[0].annex_t
                response['Sc_annex_u']=scrutinized_values[0].annex_u
                response['Sc_annex_v']=scrutinized_values[0].annex_v
                response['Sc_annex_w']=scrutinized_values[0].annex_w
                response['Sc_annex_w2']=scrutinized_values[0].annex_w2
                response['Sc_annex_x']=scrutinized_values[0].annex_x
                response['Sc_annex_y']=scrutinized_values[0].annex_y
                response['Sc_annex_z']=scrutinized_values[0].annex_z
                response['application_status'] = scrutinized_values[0].application_status
                response['eligible_for'] = scrutinized_values[0].eligible_for
                response['remarks'] = scrutinized_values[0].remarks
                response['review1_total'] = scrutinized_values[0].scrutiny_total
            response['total_credit'] = credit_total
            response['total_system_credit'] = system_total
            response['app_id'] = app_id

            responses.append(response)
    	return render(request,'recruit/appSumPdf.djt',{'responses':responses})



@login_required(login_url='/faculty_login/')
@user_passes_test(checkuserifscrutinyuser,login_url="/faculty_login/")
def fac_admin(request):
    response={}
    if checkuserifinternaluser(request.user):
        fac=FacUser.objects.filter(app_id__submitted=True, app_id__is_nitw=True)
    else:
        fac=FacUser.objects.filter(app_id__submitted=True, app_id__paymentUploaded=True, app_id__is_nitw=False)

    if checkuserifmasteruser(request.user):
        final_list = []
        for users in fac:
            if ScrutinizedValues2.objects.filter(app_id=users.app_id).count() >0:
                obj = ScrutinizedValues2.objects.get(app_id=users.app_id)
                status = obj.application_status
                if status == 0:
                    users.scrutiny_status2 = 'Not reviewed'
                elif status == 1:
                    users.scrutiny_status2 = 'Under reviewed'
                elif status == 2:
                    users.scrutiny_status2 = 'Rejected'
                else:
                    users.scrutiny_status2 = 'Approved'
            else:
                users.scrutiny_status2 = 'Not reviewed'

            if ScrutinizedValues.objects.filter(app_id=users.app_id).count() >0:
                obj = ScrutinizedValues.objects.get(app_id=users.app_id)
                status = obj.application_status
                if status == 0:
                    users.scrutiny_status = 'Not reviewed'
                elif status == 1:
                    users.scrutiny_status = 'Under reviewed'
                elif status == 2:
                    users.scrutiny_status = 'Rejected'
                else:
                    users.scrutiny_status = 'Approved'
 
            final_list.append(users)
        response['status2Column'] = True
        if checkuserifinternaluser(request.user):
            response['internalmasteruser'] = True
        response['masteruser'] = True
        response['userlist'] = final_list
        return render(request,'recruit/admin.djt',response)

    if(not checkuserifA3user(request.user)):
        scrutiny_user = ScrutinyUser.objects.get(user = request.user)
        fac = fac.filter(app_id__post_in = scrutiny_user.dept)

    college = Constants.objects.filter(key='college')
    if college.count() > 0:
        response['college'] = college[0].value

    if not checkuserifA1user(request.user):
        response['status2Column'] = True
    
    final_list = []
    for users in fac:
        if ScrutinizedValues2.objects.filter(app_id=users.app_id).count() >0:
            obj = ScrutinizedValues2.objects.get(app_id=users.app_id)
            status = obj.application_status
            if status == 0:
                users.scrutiny_status2 = 'Not reviewed'
            elif status == 1:
                users.scrutiny_status2 = 'Under reviewed'
            elif status == 2:
                users.scrutiny_status2 = 'Rejected'
            else:
                users.scrutiny_status2 = 'Approved'
        else:
            users.scrutiny_status2 = 'Not reviewed'

        if ScrutinizedValues.objects.filter(app_id=users.app_id).count() >0:
            obj = ScrutinizedValues.objects.get(app_id=users.app_id)
            status = obj.application_status
            if status == 0:
                users.scrutiny_status = 'Not reviewed' 
            elif status == 1:
                users.scrutiny_status = 'Under reviewed'
            elif status == 2:
                users.scrutiny_status = 'Rejected'
            else:
                users.scrutiny_status = 'Approved'

            if obj.payment_accepted == 2 or checkuserifinternaluser(request.user):
                if checkuserifA1user(request.user):
                    final_list.append(users)
                elif  status == 2 or status == 3:
                    final_list.append(users)
        else:
            users.scrutiny_status = 'Not reviewed'
            if checkuserifinternaluser(request.user):
                final_list.append(users)
    response['nitw_users']=fac
    response['userlist'] = final_list
    return render(request,'recruit/admin.djt',response)

def copypasteh(request):
    #annex_h = Acad_Annex_H.objects.all()
    annex_h = Acad_Annex_H.objects.filter(app_id__app_id__in=[170410335])
    for a in annex_h:
        print(a)
        if a.annexure_data:
            h_data = json.loads(a.annexure_data)
            for item in h_data:
                obj = Scrutiny_h(app_id=a.app_id,single_annex_h=item)
                obj.save()
    return HttpResponse("HEYh")


def copypastei(request):
    #annex_i = Acad_Annex_I.objects.all()
    annex_i = Acad_Annex_I.objects.filter(app_id__app_id__in=[170410335])
    for a in annex_i:
        print(a)
        if a.annexure_data:
            i_data = json.loads(a.annexure_data)
            for item in i_data:
                obj = Scrutiny_i(app_id=a.app_id,single_annex_i=item)
                obj.save()
    return HttpResponse("HEYi")


def save_h(request,appID,number):
    postdata = []
    app_id = Appdata.objects.get(app_id=appID)
    if request.method == "POST":
        for x in xrange(1,int(number)+1):
            string = "scrutiny_h_"+ str(x)
            postdata.append(request.POST[string])
        obj = Scrutiny_h.objects.filter(app_id=app_id)
        if obj.count() > 0:
            for index,x in enumerate(obj):
                x.points = postdata[index]
                x.save()
        total = 0
        for index,c in enumerate(postdata):
            total += float(postdata[index])
        print(total)
        val = ScrutinizedValues.objects.get(app_id=app_id)
        val.annex_h = total
        val.save()
    return HttpResponseRedirect('/viewscrutiny/'+appID)

def save_i(request,appID,number):
    postdata = []
    app_id = Appdata.objects.get(app_id=appID)
    if request.method == "POST":
        for x in xrange(1,int(number)+1):
            string = "scrutiny_i_"+ str(x)
            postdata.append(request.POST[string])
        obj = Scrutiny_i.objects.filter(app_id=app_id)
        if obj.count() > 0:
            for index,x in enumerate(obj):
                x.points = postdata[index]
                x.save()
        total = 0
        for index,c in enumerate(postdata):
            total += float(postdata[index])
        print(total)
        val = ScrutinizedValues.objects.get(app_id=app_id)
        val.annex_i = min(total,10)
        val.save()
    return HttpResponseRedirect('/viewscrutiny/'+appID)

def save_h2(request,appID,number):
    postdata = []
    app_id = Appdata.objects.get(app_id=appID)
    if request.method == "POST":
        for x in xrange(1,int(number)+1):
            string = "scrutiny_h2_"+ str(x)
            postdata.append(request.POST[string])
        obj = Scrutiny_h.objects.filter(app_id=app_id)
        if obj.count() > 0:
            for index,x in enumerate(obj):
                x.points2 = postdata[index]
                x.save()
        total = 0
        for index,c in enumerate(postdata):
            total += float(postdata[index])
        val = ScrutinizedValues2.objects.get(app_id=app_id)
        val.annex_h = total
        val.save()
    return HttpResponseRedirect('/viewscrutiny/'+appID)

def save_i2(request,appID,number):
    postdata = []
    app_id = Appdata.objects.get(app_id=appID)
    if request.method == "POST":
        for x in xrange(1,int(number)+1):
            string = "scrutiny_i2_"+ str(x)
            postdata.append(request.POST[string])
        obj = Scrutiny_i.objects.filter(app_id=app_id)
        if obj.count() > 0:
            for index,x in enumerate(obj):
                x.points2 = postdata[index]
                x.save()
        total = 0
        for index,c in enumerate(postdata):
            total += float(postdata[index])
        val = ScrutinizedValues2.objects.get(app_id=app_id)
        val.annex_i = min(total,10)
        val.save()
    return HttpResponseRedirect('/viewscrutiny/'+appID)

        
@login_required(login_url='/faculty_login/')
@user_passes_test(checkuserifscrutinyuser,login_url="/faculty_login/")
def appSum(request,appID):
    response={}
    app_id = Appdata.objects.get(app_id=appID)
    response['specialization'] = app_id.specialize

    if request.method == "POST" :
        if checkuserifA1user(request.user):
            if ScrutinizedValues.objects.filter(app_id=app_id).count() >0:
                obj = ScrutinizedValues.objects.get(app_id=app_id)
            else:
                obj = ScrutinizedValues()
                obj.app_id = app_id
        else:
            if ScrutinizedValues2.objects.filter(app_id=app_id).count() >0:
                obj = ScrutinizedValues2.objects.get(app_id=app_id)
            else:
                obj = ScrutinizedValues2()
                obj.app_id = app_id
        obj.annex_e1 = request.POST['form_annex_e1']
        obj.annex_e2 = request.POST['form_annex_e2']
        obj.annex_f = request.POST['form_annex_f']
        obj.annex_g = request.POST['form_annex_g']
        obj.annex_h = request.POST['form_annex_h']
        obj.annex_i = min(10,float(request.POST['form_annex_i']))
        obj.annex_j = request.POST['form_annex_j']
        obj.annex_k = request.POST['form_annex_k']
        obj.annex_l = request.POST['form_annex_l']
        obj.annex_m = request.POST['form_annex_m']
        obj.annex_n = request.POST['form_annex_n']
        obj.annex_o = request.POST['form_annex_o']
        obj.annex_p = request.POST['form_annex_p']
        obj.annex_q = request.POST['form_annex_q']
        obj.annex_r = request.POST['form_annex_r']
        obj.annex_s = request.POST['form_annex_s']
        obj.annex_t = request.POST['form_annex_t']
        obj.annex_u = request.POST['form_annex_u']
        obj.annex_v = request.POST['form_annex_v']
        obj.annex_w = request.POST['form_annex_w']
        obj.annex_w2 = request.POST['form_annex_w2']
        obj.annex_x = request.POST['form_annex_x']
        obj.annex_y = request.POST['form_annex_y']
        obj.annex_z = request.POST['form_annex_z']
        obj.remarks = request.POST['remarks']
        obj.scrutiny_total = request.POST['scrutiny_total']
        prevStatus = obj.application_status
        obj.application_status = request.POST['appln_status']
        # if app_id.post_for.split(' ', 1)[0] == "Assistant":
        #     if obj.application_status == '3':
        #         obj.eligible_for = request.POST['eligibility']
        #     else:
        #         obj.eligible_for = 0

        if prevStatus == 0:
            prev_status = 'Not reviewed'
        elif prevStatus == 1:
            prev_status = 'Under reviewed'
        elif prevStatus == 2:
            prev_status = 'Rejected'
        else:
            prev_status = 'Approved'
        timestamp =  datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if obj.application_status == '2':
            obj.log += timestamp + " : " + request.user.username + " : " + prev_status+" to rejected .\n"
        elif obj.application_status == '3':
            obj.log += timestamp + " : " + request.user.username + " : " + prev_status +" to approve .\n"
        else:
            obj.log += timestamp + " : " + request.user.username + " : " + prev_status +" to modified .\n"
        obj.save()
        
    else:
        scrutinized_values = ScrutinizedValues.objects.filter(app_id=app_id)
        if scrutinized_values.count() == 0:
            obj = ScrutinizedValues()
            obj.app_id = Appdata.objects.get(app_id = appID)
            obj.save()

    credit_total = 0.0
    system_total = 0.0
    annex_e1 = Acad_Annex_E12.objects.filter(app_id=app_id)
    response['annex_e1_total'] = 0.0
    if annex_e1.count() > 0:
        if annex_e1[0].annexure_file_e1:
            response['annex_e1_file'] = annex_e1[0].annexure_file_e1
        if len(str((annex_e1[0].annexure_data_e1).encode("utf-8"))) > 1:
            response['annex_e1'] = json.loads(annex_e1[0].annexure_data_e1)
            total_e1 = float(annex_e1[0].total_e1)
            response['annex_e1_total'] = total_e1
            credit_total += total_e1
            system_total += total_e1

    response['annex_e2_total'] = 0.0
    annex_e2 = Acad_Annex_E12.objects.filter(app_id=app_id)
    if annex_e2.count() > 0:
        if annex_e2[0].annexure_file_e2:
            response['annex_e2_file'] = annex_e1[0].annexure_file_e2
        if len(str((annex_e2[0].annexure_data_e2).encode("utf-8"))) > 1:
            response['annex_e2'] = json.loads(annex_e2[0].annexure_data_e2)
            # total_patent=0
            # pat_credit=0
            # for item in response['annex_e2']:
            #     total_patent+=1
            #     pat_credit+=float(item['credit'])
            # response['total_patent']=total_patent
            # response['pat_credit']=pat_credit
            total_e2 = float(annex_e2[0].total_e2)
            response['annex_e2_total'] = total_e2
            credit_total += total_e2
            system_total += total_e2

    annex_f = Acad_Annex_F.objects.filter(app_id=app_id)
    if annex_f.count() > 0:
        if annex_f[0].annexure_file:
            response['annex_f_file'] = annex_f[0].annexure_file
        if annex_f[0].annexure_data:
            response['annex_f'] = json.loads(annex_f[0].annexure_data)
            response['annex_f_credit'] = annex_f[0].credit_score
            credit_total += annex_f[0].credit_score
            
            if(annex_f[0].credit_score > 10.0):
                response['annex_f_system'] = 10.0
                system_total += 10.0
            else:
                response['annex_f_system'] = annex_f[0].credit_score
                system_total += annex_f[0].credit_score

    annex_g = Acad_Annex_G.objects.filter(app_id=app_id)
    if annex_g.count() > 0:
        if annex_g[0].annexure_file:
            response['annex_g_file'] = annex_g[0].annexure_file
        if annex_g[0].annexure_data:
            response['annex_g'] = json.loads(annex_g[0].annexure_data)
            sole=0
            sole_credit=0
            superv=0
            sup_credit=0
            co=0
            co_credit=0
            total = 0.0
            for item in response['annex_g']:
                total += float(item['credit'])
                if item['co_sup'] == 0:
                    sole+=1
                    sole_credit+=float(item['credit'])
                elif item['role_main'][0]=='M' or item['role_main'][0]=='m':
                    superv+=1
                    sup_credit+=float(item['credit'])
                else:
                    co+=1
                    co_credit+=float(item['credit'])
            response['sole']=sole
            response['sole_credit']=sole_credit
            response['superv']=superv
            response['sup_credit']=sup_credit
            response['co']=co
            response['co_credit']=co_credit
            response['annex_g_total'] = total
            credit_total += total
            system_total += total

    # titles = []
    # scrutiny_h_indi = Scrutiny_h.objects.filter(app_id=app_id)
    # if scrutiny_h_indi.count() > 0:
    #     for i in scrutiny_h_indi:
    #         titles.append(i.single_annex_h)
    annex_h = Acad_Annex_H.objects.filter(app_id=app_id)
    if annex_h.count() > 0:
        if annex_h[0].annexure_file:
            response['annex_h_file'] = annex_h[0].annexure_file

        if annex_h[0].annexure_data:
            scrutiny_h_indi = Scrutiny_h.objects.filter(app_id=app_id)
            data = json.loads(annex_h[0].annexure_data)
            for index,h in enumerate(data):
                data[index]['scrutinized_values'] = scrutiny_h_indi[index].points
                data[index]['scrutinized_values2'] = scrutiny_h_indi[index].points2
            response['annex_h'] = data
            response['number_of_h'] = len(data)
            response['annex_h_last_prom'] = annex_h[0].last_prom
        total = float(annex_h[0].total)
        response['annex_h_total'] = total
        credit_total += total
        system_total += total


    annex_i = Acad_Annex_I.objects.filter(app_id=app_id)
    if annex_i.count() > 0:
        if annex_i[0].annexure_file:
            response['annex_i_file'] = annex_i[0].annexure_file
        if annex_i[0].annexure_data:
            scrutiny_i_indi = Scrutiny_i.objects.filter(app_id=app_id)
            data = json.loads(annex_i[0].annexure_data)
            for index,h in enumerate(data):
                data[index]['scrutinized_values'] = scrutiny_i_indi[index].points
                data[index]['scrutinized_values2'] = scrutiny_i_indi[index].points2
            response['annex_i'] = data
            response['number_of_i'] = len(data)
        total = float(annex_i[0].total)
        response['annex_i_total'] = total
        credit_total += total
        if(total > 10.0):
            response['annex_i_system'] = 10.0
            system_total += 10.0
        else:
            response['annex_i_system'] = total
            system_total += total

    annex_j = Acad_Annex_J.objects.filter(app_id=app_id)
    if annex_j.count() > 0:
        if annex_j[0].annexure_file:
            response['annex_j_file'] = annex_j[0].annexure_file
        if annex_j[0].annexure_data:
            response['annex_j'] = json.loads(annex_j[0].annexure_data)
            response['annex_j_credit'] = annex_j[0].credit_score
            response['annex_j_last_prom'] = annex_j[0].last_prom
            credit_total += annex_j[0].credit_score
            if(annex_j[0].credit_score > 16.0):
                response['annex_j_system'] = 16.0
                system_total += 16.0
            else:
                response['annex_j_system'] = annex_j[0].credit_score
                system_total += annex_j[0].credit_score

    annex_k = Acad_Annex_K.objects.filter(app_id=app_id)
    if annex_k.count() > 0:
        if annex_k[0].annexure_file:
            response['annex_k_file'] = annex_k[0].annexure_file
        if annex_k[0].annexure_data:
            response['annex_k'] = json.loads(annex_k[0].annexure_data)
            response['annex_k_credit'] = annex_k[0].credit_score
            response['annex_k_last_prom'] = annex_k[0].last_prom
            credit_total += annex_k[0].credit_score
            if(annex_k[0].credit_score > 8.0):
                response['annex_k_system'] = 8.0
                system_total += 8.0
            else:
                response['annex_k_system'] = annex_k[0].credit_score
                system_total += annex_k[0].credit_score

    annex_l = Acad_Annex_L.objects.filter(app_id=app_id)
    if annex_l.count() > 0:
        if annex_l[0].annexure_file:
            response['annex_l_file'] = annex_l[0].annexure_file
        if annex_l[0].annexure_data:
            response['annex_l'] = json.loads(annex_l[0].annexure_data)
            response['annex_l_last_prom'] = annex_l[0].last_prom
            response['annex_l_credit'] = annex_l[0].credit_score
            credit_total += annex_l[0].credit_score
            if(annex_l[0].credit_score > 3.0):
                response['annex_l_system'] = 3.0
                system_total += 3.0
            else:
                response['annex_l_system'] = annex_l[0].credit_score
                system_total += annex_l[0].credit_score


    annex_m = Acad_Annex_M.objects.filter(app_id=app_id)
    if annex_m.count() > 0:
        if annex_m[0].annexure_file:
            response['annex_m_file'] = annex_m[0].annexure_file
        if annex_m[0].annexure_data:
            response['annex_m'] = json.loads(annex_m[0].annexure_data)
            response['annex_m_credit'] = annex_m[0].credit_score
            response['annex_m_last_prom'] = annex_m[0].last_prom
            credit_total += annex_m[0].credit_score
            if(annex_m[0].credit_score > 3.0):
                response['annex_m_system'] = 3.0
                system_total += 3.0
            else:
                response['annex_m_system'] = annex_m[0].credit_score
                system_total += annex_m[0].credit_score

    annex_n = Acad_Annex_N.objects.filter(app_id=app_id)
    if annex_n.count() > 0:
        if annex_n[0].annexure_file:
            response['annex_n_file'] = annex_n[0].annexure_file
        if annex_n[0].annexure_data:
            response['annex_n'] = json.loads(annex_n[0].annexure_data)
            response['annex_n_last_prom'] = annex_n[0].last_prom
            response['annex_n_credit'] = annex_n[0].total
            response['total_noN'] = annex_n[0].total_number
            credit_total += annex_n[0].total
            if(annex_n[0].total > 8.0):
                response['annex_n_system'] = 8.0
                system_total += 8.0
            else:
                response['annex_n_system'] = annex_n[0].total
                system_total += annex_n[0].total

    response['annex_o_credit'] = 0.0
    response['annex_o_system'] = 0.0
    annex_o = Acad_Annex_O.objects.filter(app_id=app_id)
    if annex_o.count() > 0:
        if annex_o[0].annexure_file:
            response['annex_o_file'] = annex_o[0].annexure_file
        if annex_o[0].annexure_data:
            response['annex_o'] = json.loads(annex_o[0].annexure_data)
            response['annex_o_last_prom'] = annex_o[0].last_prom
            response['prog_2_week_duration']=annex_o[0].prog_2_week_duration
            response['prog_1_week_duration']=annex_o[0].prog_1_week_duration
            response['annex_o_credit'] = annex_o[0].total
            response['annex_o_system'] = annex_o[0].total
            credit_total += annex_o[0].total
            system_total += annex_o[0].total

    response['annex_p_credit'] = 0.0
    response['annex_p_system'] = 0.0
    annex_p = Acad_Annex_P.objects.filter(app_id=app_id)
    if annex_p.count() > 0:
        if annex_p[0].annexure_file:
            response['annex_p_file'] = annex_p[0].annexure_file
        if annex_p[0].annexure_data:
            response['annex_p'] = json.loads(annex_p[0].annexure_data)
            response['annex_p_last_prom'] = annex_p[0].last_prom
            response['annex_p_credit'] = annex_p[0].total
            response['total_noP'] = annex_p[0].total_number
            credit_total += annex_p[0].total
            if(annex_p[0].total > 6.0):
                response['annex_p_system'] = 6.0
                system_total += 6.0
            else:
                response['annex_p_system'] = annex_p[0].total
                system_total += annex_p[0].total

    response['annex_q_credit'] = 0.0
    response['annex_q_system'] = 0.0
    annex_q = Acad_Annex_Q.objects.filter(app_id=app_id)
    if annex_q.count() > 0:
        if annex_q[0].annexure_file:
            response['annex_q_file'] = annex_q[0].annexure_file
        if annex_q[0].annexure_data:
            response['annex_q'] = json.loads(annex_q[0].annexure_data)
            response['annex_q_last_prom'] = annex_q[0].last_prom
            response['annex_q_exp_phd'] = annex_q[0].total_exp_after_phd
            response['annex_q_exp_cur'] = annex_q[0].total_exp_cur
            response['annex_q_tot_exp'] = annex_q[0].total_exp
            response['annex_q_credit'] = annex_q[0].credit_score
            response['total_yearsQ']=annex_q[0].total_years
            response['total_monthsQ']=annex_q[0].total_months
            credit_total += annex_q[0].credit_score
            if(annex_q[0].credit_score > 10.0):
                response['annex_q_system'] = 10.0
                system_total += 10.0
            else:
                response['annex_q_system'] = annex_q[0].credit_score
                system_total += annex_q[0].credit_score

    response['annex_r_credit'] = 0.0
    response['annex_r_system'] = 0.0
    annex_r = Acad_Annex_R.objects.filter(app_id=app_id)
    if annex_r.count() > 0:
        if annex_r[0].annexure_file:
            response['annex_r_file'] = annex_r[0].annexure_file
        if annex_r[0].annexure_data:
            response['annex_r'] = json.loads(annex_r[0].annexure_data)
            response['annex_r_last_prom'] = annex_r[0].last_prom
            response['annex_r_credit']=annex_r[0].total
            response['total_numberR']=annex_r[0].total_number
            response['annex_r_system'] = annex_r[0].total
            credit_total += annex_r[0].total
            system_total += annex_r[0].total

    response['annex_s_credit'] = 0.0
    response['annex_s_system'] = 0.0
    annex_s = Acad_Annex_S.objects.filter(app_id=app_id)
    if annex_s.count() > 0:
        if annex_s[0].annexure_file:
            response['annex_s_file'] = annex_s[0].annexure_file
        if annex_s[0].annexure_data:
            response['annex_s'] = json.loads(annex_s[0].annexure_data)
            response['annex_s_last_prom'] = annex_s[0].last_prom
            response['annex_s_extra_load'] = annex_s[0].extra_load
            response['annex_s_credit'] = annex_s[0].credit_score
            credit_total += annex_s[0].credit_score
            if(annex_s[0].credit_score > 15.0):
                response['annex_s_system'] = 15.0
                system_total += 15.0
            else:
                response['annex_s_system'] = annex_s[0].credit_score
                system_total += annex_s[0].credit_score

    response['annex_t_total'] = 0.0
    response['annex_t_system'] = 0.0
    annex_t = Acad_Annex_T.objects.filter(app_id=app_id)
    if annex_t.count() > 0:
        if annex_t[0].annexure_file:
            response['annex_t_file'] = annex_t[0].annexure_file
        if annex_t[0].annexure_data:
            response['annex_t'] = json.loads(annex_t[0].annexure_data)
            response['annex_t_last_prom'] = annex_t[0].last_prom
        total = float(annex_t[0].total)
        response['annex_t_total'] = total
        credit_total += total
        if(total > 10.0):
            response['annex_t_system'] = 10.0
            system_total += 10.0
        else:
            response['annex_t_system'] = total
            system_total += total

    response['annex_u_total'] = 0.0
    response['annex_u_system'] = 0.0
    annex_u = Acad_Annex_U.objects.filter(app_id=app_id)
    if annex_u.count() > 0:
        if annex_u[0].annexure_file:
            response['annex_u_file'] = annex_u[0].annexure_file
        if annex_u[0].annexure_data:
            response['annex_u'] = json.loads(annex_u[0].annexure_data)
            response['annex_u_last_prom'] = annex_u[0].last_prom
        total = float(annex_u[0].total)
        response['annex_u_total'] = total
        credit_total += total
        if(total > 4.0):
            response['annex_u_system'] = 4.0
            system_total += 4.0
        else:
            response['annex_u_system'] = total
            system_total += total

    response['annex_v_total'] = 0.0
    response['annex_v_system'] = 0.0
    annex_v = Acad_Annex_V.objects.filter(app_id=app_id)
    if annex_v.count() > 0:
        if annex_v[0].annexure_file:
            response['annex_v_file'] = annex_v[0].annexure_file
        if annex_v[0].annexure_data:
            response['annex_v'] = json.loads(annex_v[0].annexure_data)
            response['annex_v_last_prom'] = annex_v[0].last_prom
        total = float(annex_v[0].total)
        response['annex_v_total'] = total
        credit_total += total
        if(total > 18.0):
            response['annex_v_system'] = 18.0
            system_total += 18.0
        else:
            response['annex_v_system'] = total
            system_total += total
    
    response['annex_w1_total'] = 0.0
    response['annex_w1_system'] = 0.0
    total_w = 0.0
    annex_w1 = Acad_Annex_W1_W2.objects.filter(app_id=app_id)
    if annex_w1.count() > 0:
        if annex_w1[0].annexure_file_w1:
            response['annex_w1_file'] = annex_w1[0].annexure_file_w1
        if len(str((annex_w1[0].annexure_data1).encode("utf-8"))) > 1:
            response['annex_w1'] = json.loads(annex_w1[0].annexure_data1)
            response['annex_w1_last_prom'] = annex_w1[0].last_prom_w1
            response['annex_w1_total'] = annex_w1[0].total_w1
            total_w += annex_w1[0].total_w1
            if(total_w > 6.0):
                response['annex_w1_system'] = 6.0
                system_total += 6.0
            else:
                response['annex_w1_system'] = total_w
                system_total += total_w


    response['annex_w2_total'] = 0.0
    response['annex_w2_system'] = 0.0
    annex_w2 = Acad_Annex_W1_W2.objects.filter(app_id=app_id)
    if annex_w2.count() > 0:
        if annex_w2[0].annexure_file_w2:
            response['annex_w2_file'] = annex_w2[0].annexure_file_w2
        if len(str((annex_w2[0].annexure_data2).encode("utf-8"))) > 1:
            response['annex_w2'] = json.loads(annex_w2[0].annexure_data2)
            response['annex_w2_last_prom'] = annex_w2[0].last_prom_w2
            response['annex_w2_total'] = annex_w2[0].total_w2
            total_w += annex_w2[0].total_w2
            if(annex_w2[0].total_w2 > 6.0):
                response['annex_w2_system'] = 6.0
                system_total += 6.0
            else:
                response['annex_w2_system'] = annex_w2[0].total_w2
                system_total += annex_w2[0].total_w2

    response['annex_w_total'] = total_w
    credit_total += total_w
    
    response['annex_x_total'] = 0.0
    response['annex_x_system'] = 0.0
    annex_x = Acad_Annex_X.objects.filter(app_id=app_id)
    if annex_x.count() > 0:
        if annex_x[0].annexure_file:
            response['annex_x_file'] = annex_x[0].annexure_file
        if len(str((annex_x[0].annexure_data).encode("utf-8"))) > 1:
            response['annex_x'] = json.loads(annex_x[0].annexure_data)
            response['annex_x_last_prom'] = annex_x[0].last_prom
            total = float(annex_x[0].total)
            response['annex_x_total'] = total
            credit_total += total
            if(total > 4.0):
                response['annex_x_system'] = 4.0
                system_total += 4.0
            else:
                response['annex_x_system'] = total
                system_total += total

    response['annex_y_credit'] = 0.0
    response['annex_y_system'] = 0.0
    annex_y = Acad_Annex_Y.objects.filter(app_id=app_id)
    if annex_y.count() > 0:
        if annex_y[0].annexure_file:
            response['annex_y_file'] = annex_y[0].annexure_file
        response['annex_y_credit'] = annex_y[0].credit_score
        if annex_y[0].ieee:
            response['annex_y_ieee'] = 'IEEE'
            response['annex_y_area'] = True
        if annex_y[0].fna:
            response['annex_y_fna'] = 'FNA'
            response['annex_y_area'] = True
        if annex_y[0].fnae:
            response['annex_y_fnae'] = 'FNAE'
            response['annex_y_area'] = True
        if annex_y[0].fnasc:
            response['annex_y_fnasc'] = 'FNASC'
            response['annex_y_area'] = True
        credit_total += annex_y[0].credit_score
        if(annex_y[0].credit_score > 10.0):
            response['annex_y_system'] = 10.0
            system_total += 10.0
        else:
            response['annex_y_system'] = annex_y[0].credit_score
            system_total += annex_y[0].credit_score

    response['annex_z_total'] = 0.0
    response['annex_z_system'] = 0.0
    annex_z = Acad_Annex_Z.objects.filter(app_id=app_id)
    if annex_z.count() > 0:
        if annex_z[0].annexure_file:
            response['annex_z_file'] = annex_z[0].annexure_file
        if len(str((annex_z[0].annexure_data).encode("utf-8"))) > 1:
            response['annex_z'] = json.loads(annex_z[0].annexure_data)
            response['annex_z_last_prom'] = annex_z[0].last_prom
            response['annex_z_percentage'] = annex_z[0].percentage
            total = float(annex_z[0].total)
            response['annex_z_total'] = total
            credit_total += total
            if annex_z[0].percentage >= 85:
                if(total > 20.0):
                    response['annex_z_system'] = 20.0
                    system_total += 20.0
                else:
                    response['annex_z_system'] = total
                    system_total += total
            elif annex_z[0].percentage < 85 and annex_z[0].percentage >= 75:
                if(total > 10.0):
                    response['annex_z_system'] = 10.0
                    system_total += 10.0
            else:
                response['annex_z_system'] = total
                system_total += total

    annex_a = Acad_Annex_A.objects.filter(app_id=app_id)
    if annex_a.count() > 0:
        if annex_a[0].annexure_file:
            response['annex_a_file'] = annex_a[0].annexure_file
        if len(str((annex_a[0].annexure_data).encode("utf-8"))) > 1:
            response['annex_a'] = json.loads(annex_a[0].annexure_data)
    facuser = FacUser.objects.get(app_id=app_id)
    # response['app']=app_id
    
    response['fac']=facuser
    college = Constants.objects.filter(key='college')
    if college.count() > 0:
        response['college'] = college[0].value

    scrutinized_values = ScrutinizedValues.objects.filter(app_id=app_id)
    if scrutinized_values.count() > 0:
        response['Sc_annex_e1']=scrutinized_values[0].annex_e1
        response['Sc_annex_e2']=scrutinized_values[0].annex_e2
        response['Sc_annex_f']=scrutinized_values[0].annex_f
        response['Sc_annex_g']=scrutinized_values[0].annex_g
        response['Sc_annex_h']=scrutinized_values[0].annex_h
        response['Sc_annex_i']=scrutinized_values[0].annex_i
        response['Sc_annex_j']=scrutinized_values[0].annex_j
        response['Sc_annex_k']=scrutinized_values[0].annex_k
        response['Sc_annex_l']=scrutinized_values[0].annex_l
        response['Sc_annex_m']=scrutinized_values[0].annex_m
        response['Sc_annex_n']=scrutinized_values[0].annex_n
        response['Sc_annex_o']=scrutinized_values[0].annex_o
        response['Sc_annex_p']=scrutinized_values[0].annex_p
        response['Sc_annex_q']=scrutinized_values[0].annex_q
        response['Sc_annex_r']=scrutinized_values[0].annex_r
        response['Sc_annex_s']=scrutinized_values[0].annex_s
        response['Sc_annex_t']=scrutinized_values[0].annex_t
        response['Sc_annex_u']=scrutinized_values[0].annex_u
        response['Sc_annex_v']=scrutinized_values[0].annex_v
        response['Sc_annex_w']=scrutinized_values[0].annex_w
        response['Sc_annex_w2']=scrutinized_values[0].annex_w2
        response['Sc_annex_x']=scrutinized_values[0].annex_x
        response['Sc_annex_y']=scrutinized_values[0].annex_y
        response['Sc_annex_z']=scrutinized_values[0].annex_z
        response['application_status'] = scrutinized_values[0].application_status
        response['eligible_for'] = scrutinized_values[0].eligible_for
        response['remarks'] = scrutinized_values[0].remarks
        response['review1_total'] = scrutinized_values[0].scrutiny_total
    response['total_credit'] = credit_total
    response['total_system_credit'] = system_total
    response['app_id'] = appID

    if not checkuserifA1user(request.user):
        response['A2user'] = True
        scrutinized_values2 = ScrutinizedValues2.objects.filter(app_id=app_id)
        if scrutinized_values2.count() == 0:
            obj = ScrutinizedValues2()
            obj.app_id = Appdata.objects.get(app_id = appID)
            obj.save()
        scrutinized_values2 = ScrutinizedValues2.objects.filter(app_id=app_id)
        response['Sc_annex_e1_2']=scrutinized_values2[0].annex_e1
        response['Sc_annex_e2_2']=scrutinized_values2[0].annex_e2
        response['Sc_annex_f_2']=scrutinized_values2[0].annex_f
        response['Sc_annex_g_2']=scrutinized_values2[0].annex_g
        response['Sc_annex_h_2']=scrutinized_values2[0].annex_h
        response['Sc_annex_i_2']=scrutinized_values2[0].annex_i
        response['Sc_annex_j_2']=scrutinized_values2[0].annex_j
        response['Sc_annex_k_2']=scrutinized_values2[0].annex_k
        response['Sc_annex_l_2']=scrutinized_values2[0].annex_l
        response['Sc_annex_m_2']=scrutinized_values2[0].annex_m
        response['Sc_annex_n_2']=scrutinized_values2[0].annex_n
        response['Sc_annex_o_2']=scrutinized_values2[0].annex_o
        response['Sc_annex_p_2']=scrutinized_values2[0].annex_p
        response['Sc_annex_q_2']=scrutinized_values2[0].annex_q
        response['Sc_annex_r_2']=scrutinized_values2[0].annex_r
        response['Sc_annex_s_2']=scrutinized_values2[0].annex_s
        response['Sc_annex_t_2']=scrutinized_values2[0].annex_t
        response['Sc_annex_u_2']=scrutinized_values2[0].annex_u
        response['Sc_annex_v_2']=scrutinized_values2[0].annex_v
        response['Sc_annex_w_2']=scrutinized_values2[0].annex_w
        response['Sc_annex_w2_2']=scrutinized_values2[0].annex_w2
        response['Sc_annex_x_2']=scrutinized_values2[0].annex_x
        response['Sc_annex_y_2']=scrutinized_values2[0].annex_y
        response['Sc_annex_z_2']=scrutinized_values2[0].annex_z
        response['application_status_2'] = scrutinized_values2[0].application_status
        response['eligible_for_2'] = scrutinized_values2[0].eligible_for
        response['remarks_A2'] = scrutinized_values2[0].remarks
        return render(request,'recruit/appSumA2.djt',response)

    # if app_id.post_for.split(' ', 1)[0] == "Assistant":
    #     response['assistant'] = True
    return render(request,'recruit/appSum.djt',response)

@login_required(login_url='/faculty_login/')
@user_passes_test(checkuserifscrutinyuser,login_url="/faculty_login/")
def options3(request, appID):
    response = {}
    app_id = Appdata.objects.get(app_id=appID)
    response['app_id'] = appID
    return render(request, 'recruit/3options.djt',response)

@login_required(login_url='/faculty_login/')
@user_passes_test(checkuserifscrutinyuser,login_url="/faculty_login/")
def viewedu(request, appID):
    response = {}
    app_id = Appdata.objects.get(app_id=appID)
    response['app_id'] = appID
    if Experience.objects.filter(app_id=app_id).exists():
        exp = Experience.objects.get(app_id=app_id)
        response['Experience'] = exp
        response['teachingData'] = json.loads(exp.teaching_data)
        response['researchData'] = json.loads(exp.research_data)
        response['industryData'] = json.loads(exp.industrial_data)

    if Qualification.objects.filter(app_id=app_id,degreeType='UG').exists():
        response['Bqual'] = Qualification.objects.get(app_id=app_id,degreeType='UG')
    if Qualification.objects.filter(app_id=app_id,degreeType='PG').exists():
        response['Mqual'] = Qualification.objects.get(app_id=app_id,degreeType='PG')
    if Qualification.objects.filter(app_id=app_id,degreeType='PHD').exists():
        response['Phdqual'] = Qualification.objects.get(app_id=app_id,degreeType='PHD')
    if Qualification.objects.filter(app_id=app_id,degreeType='other').exists():
        response['Oqual'] = Qualification.objects.get(app_id=app_id,degreeType='other')
    annex_a = Acad_Annex_A.objects.filter(app_id=app_id)

    if ScrutinizedValues.objects.filter(app_id=app_id).count() > 0:
        Scobj = ScrutinizedValues.objects.get(app_id=app_id)
        response['remarks'] = Scobj.remarks
    if not checkuserifA1user(request.user):
        response['A2user'] = True
        scrutinized_values2 = ScrutinizedValues2.objects.filter(app_id=app_id)
        if scrutinized_values2.count() > 0:
            response['remarks_A2'] = scrutinized_values2[0].remarks


    if annex_a.count() > 0:
        if annex_a[0].annexure_file:
            response['annex_a_file'] = annex_a[0].annexure_file
        if len(str((annex_a[0].annexure_data).encode("utf-8"))) > 2:
            response['annex_a'] = json.loads(annex_a[0].annexure_data)

    if Paper.objects.filter(app_id = appID).count() >0:
        paper = Paper.objects.get(app_id=app_id).paper1
        response['paper'] = paper
    return render(request,'recruit/viewedu.djt', response)

@login_required(login_url='/faculty_login/')
@user_passes_test(checkuserifscrutinyuser,login_url="/faculty_login/")
def rejectcandidate(request, appID):
    timestamp =  datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    app_id = Appdata.objects.get(app_id=appID)
    if checkuserifA1user(request.user):
        obj = ScrutinizedValues.objects.filter(app_id=app_id)
        if obj.count() > 0:
            obj = obj[0]
        else:
            obj = ScrutinizedValues()
            obj.app_id = app_id
    else:
        obj = ScrutinizedValues2.objects.filter(app_id=app_id)
        if obj.count() > 0:
            obj = obj[0]
        else:
            obj = ScrutinizedValues2()
            obj.app_id = app_id
    prevStatus = obj.application_status
    if prevStatus == 0:
        prev_status = 'Not reviewed'
    elif prevStatus == 1:
        prev_status = 'Under reviewed'
    elif prevStatus == 2:
        prev_status = 'Rejected'
    else:
        prev_status = 'Approved'
    timestamp =  datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    obj.log += timestamp + " : " + request.user.username + " : " + prev_status+" to rejected .\n"
    obj.application_status = 2
    obj.save()

    return redirect('/faculty_admin/')

@login_required(login_url='/faculty_login/')
@user_passes_test(checkuserifscrutinyuser,login_url="/faculty_login/")
def submitRemark(request, appID):
    if request.method == 'POST':
        remarks = request.POST['remarks']
        app_id = Appdata.objects.get(app_id=appID)
        if checkuserifA1user(request.user):
            obj = ScrutinizedValues.objects.filter(app_id=app_id)
            if obj.count() > 0:
                obj = obj[0]
            else:
                obj = ScrutinizedValues()
                obj.app_id = app_id
        else:
            obj = ScrutinizedValues2.objects.filter(app_id=app_id)
            if obj.count() > 0:
                obj = obj[0]
            else:
                obj = ScrutinizedValues2()
                obj.app_id = app_id     
        obj.remarks = remarks
        obj.save()
    return redirect('/viewedu/'+appID)

@login_required(login_url='/faculty_login/')
@user_passes_test(checkuserifscrutinyuser,login_url="/faculty_login/")
def viewappl(request, appID):
    response = {}
    response['profile'] = UserProfile.objects.get(applicationID=appID)

    college = Constants.objects.filter(key='college')
    if college.count() > 0:
        response['college'] = college[0].value

    app_id = Appdata.objects.get(app_id=appID)


    response['specialization'] = app_id.specialize
    if FacUser.objects.filter(app_id=app_id).exists():
        facuser = FacUser.objects.get(app_id=app_id)
        print(facuser.pwd)
        response['generalData'] = facuser
    if Experience.objects.filter(app_id=app_id).exists():
        exp = Experience.objects.get(app_id=app_id)
        response['Experience'] = exp
        response['teachingData'] = json.loads(exp.teaching_data)
        response['researchData'] = json.loads(exp.research_data)
        response['industryData'] = json.loads(exp.industrial_data)

    if Qualification.objects.filter(app_id=app_id,degreeType='UG').exists():
        response['Bqual'] = Qualification.objects.get(app_id=app_id,degreeType='UG')
    if Qualification.objects.filter(app_id=app_id,degreeType='PG').exists():
        response['Mqual'] = Qualification.objects.get(app_id=app_id,degreeType='PG')
    if Qualification.objects.filter(app_id=app_id,degreeType='PHD').exists():
        response['Phdqual'] = Qualification.objects.get(app_id=app_id,degreeType='PHD')
    if Qualification.objects.filter(app_id=app_id,degreeType='other').exists():
        response['Oqual'] = Qualification.objects.get(app_id=app_id,degreeType='other')

    external_sponsored_rnd = External_Sponsored_RnD.objects.filter(app_id=app_id)
    consultancy_projects = Consultancy_Projects.objects.filter(app_id=app_id)
    phd_completed = PhD_Completed.objects.filter(app_id=app_id)
    journal_papers = Journal_Papers.objects.filter(app_id = app_id)
    conference_paper_sci = Conference_Paper_SCI.objects.filter(app_id = app_id)
    paper = Paper.objects.filter(app_id = app_id)
    if paper.count() > 0:
        response['paper1'] = paper[0].paper1
    acad_annex_a = Acad_Annex_A.objects.filter(app_id=app_id)
    acad_annex_b = Acad_Annex_B.objects.filter(app_id=app_id)
    acad_annex_c = Acad_Annex_C.objects.filter(app_id=app_id)
    acad_annex_d = Acad_Annex_D.objects.filter(app_id=app_id)
    acad_annex_e12 = Acad_Annex_E12.objects.filter(app_id=app_id)
    acad_annex_f = Acad_Annex_F.objects.filter(app_id=app_id)
    acad_annex_g = Acad_Annex_G.objects.filter(app_id=app_id)
    acad_annex_h = Acad_Annex_H.objects.filter(app_id=app_id)
    acad_annex_i = Acad_Annex_I.objects.filter(app_id=app_id)
    acad_annex_j = Acad_Annex_J.objects.filter(app_id=app_id)
    acad_annex_k = Acad_Annex_K.objects.filter(app_id=app_id)
    acad_annex_l = Acad_Annex_L.objects.filter(app_id=app_id)
    acad_annex_m = Acad_Annex_M.objects.filter(app_id=app_id)
    acad_annex_n = Acad_Annex_N.objects.filter(app_id=app_id)
    acad_annex_o = Acad_Annex_O.objects.filter(app_id=app_id)
    acad_annex_p = Acad_Annex_P.objects.filter(app_id=app_id)
    acad_annex_q = Acad_Annex_Q.objects.filter(app_id=app_id)
    acad_annex_r = Acad_Annex_R.objects.filter(app_id=app_id)
    acad_annex_s = Acad_Annex_S.objects.filter(app_id=app_id)
    acad_annex_t = Acad_Annex_T.objects.filter(app_id=app_id)
    acad_annex_u = Acad_Annex_U.objects.filter(app_id=app_id)
    acad_annex_v = Acad_Annex_V.objects.filter(app_id=app_id)
    acad_annex_w1_w2 = Acad_Annex_W1_W2.objects.filter(app_id=app_id)
    acad_annex_x = Acad_Annex_X.objects.filter(app_id=app_id)
    acad_annex_y = Acad_Annex_Y.objects.filter(app_id=app_id)
    acad_annex_z = Acad_Annex_Z.objects.filter(app_id=app_id)

    if external_sponsored_rnd.count() > 0:
        response['external_sponsored_rnd'] = external_sponsored_rnd[0]
        if external_sponsored_rnd[0].projects_not_pi:
            response['projects_not_pi'] = json.loads(external_sponsored_rnd[0].projects_not_pi)
        if external_sponsored_rnd[0].patents_not_pi:
            response['patents_not_pi'] = json.loads(external_sponsored_rnd[0].patents_not_pi)

    if consultancy_projects.count() > 0:
        response['consultancy_projects'] = consultancy_projects[0]

    if phd_completed.count() > 0:
        response['phd_completed'] = phd_completed[0]
        if phd_completed[0].phds:
            response['phds'] = json.loads(phd_completed[0].phds)
        response['phds'] = json.loads(phd_completed[0].phds)

    if journal_papers.count() > 0:
        response['journal_papers'] = journal_papers[0]
        if journal_papers[0].papers:
            response['papers'] = json.loads(journal_papers[0].papers)
        response['papers'] = json.loads(journal_papers[0].papers)

    if conference_paper_sci.count() > 0:
        response['conference_paper_sci'] = conference_paper_sci[0]
        if conference_paper_sci[0].papers:
            response['papers1'] = json.loads(conference_paper_sci[0].papers)
        response['papers1'] = json.loads(conference_paper_sci[0].papers)


    if acad_annex_a.count() > 0:
        response['acad_annex_a'] = acad_annex_a[0]
        response['acad_annex_a_file'] = acad_annex_a[0].annexure_file
        if len(str((acad_annex_a[0].annexure_data).encode("utf-8"))) > 2:
            response['annex_a'] = json.loads(acad_annex_a[0].annexure_data)

    if acad_annex_b.count() > 0:
        response['acad_annex_b'] = acad_annex_b[0]
    if acad_annex_c.count() > 0:
        response['acad_annex_c'] = acad_annex_c[0]

    if acad_annex_d.count() > 0:
        response['acad_annex_d'] = acad_annex_d[0]

    if acad_annex_e12.count() > 0:
        response['acad_annex_e12'] = acad_annex_e12[0]
        response['total_e'] = float(acad_annex_e12[0].total_e1 + acad_annex_e12[0].total_e2)

    if acad_annex_f.count() > 0:
        response['acad_annex_f'] = acad_annex_f[0]

    if acad_annex_g.count() > 0:
        response['acad_annex_g'] = acad_annex_g[0]

    if acad_annex_h.count() > 0:
        response['acad_annex_h'] = acad_annex_h[0]

    if acad_annex_i.count() > 0:
        response['acad_annex_i'] = acad_annex_i[0]

    if acad_annex_j.count() > 0:
        response['acad_annex_j'] = acad_annex_j[0]

    if acad_annex_k.count() > 0:
        response['acad_annex_k'] = acad_annex_k[0]

    if acad_annex_l.count() > 0:
        response['acad_annex_l'] = acad_annex_l[0]

    if acad_annex_m.count() > 0:
        response['acad_annex_m'] = acad_annex_m[0]

    if acad_annex_n.count() > 0:
        response['acad_annex_n'] = acad_annex_n[0]

    if acad_annex_o.count() > 0:
        response['acad_annex_o'] = acad_annex_o[0]

    if acad_annex_p.count() > 0:
        response['acad_annex_p'] = acad_annex_p[0]

    if acad_annex_q.count() > 0:
        response['acad_annex_q'] = acad_annex_q[0]  

    if acad_annex_r.count() > 0:
        response['acad_annex_r'] = acad_annex_r[0]

    if acad_annex_s.count() > 0:
        response['acad_annex_s'] = acad_annex_s[0]

    if acad_annex_t.count() > 0:
        response['acad_annex_t'] = acad_annex_t[0]

    if acad_annex_u.count() > 0:
        response['acad_annex_u'] = acad_annex_u[0]

    if acad_annex_v.count() > 0:
        response['acad_annex_v'] = acad_annex_v[0]

    if acad_annex_w1_w2.count() > 0:
        response['acad_annex_w1_w2'] = acad_annex_w1_w2[0]
        response['total_w'] = float(acad_annex_w1_w2[0].total_w1 + acad_annex_w1_w2[0].total_w2)

    if acad_annex_x.count() > 0:
        response['acad_annex_x'] = acad_annex_x[0]

    if acad_annex_y.count() > 0:
        response['acad_annex_y'] = acad_annex_y[0]

    if acad_annex_z.count() > 0:
        response['acad_annex_z'] = acad_annex_z[0]

    if SubjectTaught.objects.filter(app_id=app_id,level='UG',courseType='core').exists() :
        obj1 = SubjectTaught.objects.get(app_id=app_id,level='UG',courseType='core')
        response['coreUGobj'] = json.loads(obj1.data)
    if SubjectTaught.objects.filter(app_id=app_id,level='UG',courseType='elective').exists() :
        obj2 = SubjectTaught.objects.get(app_id=app_id,level='UG',courseType='elective')
        response['electiveUGobj'] = json.loads(obj2.data)
    if SubjectTaught.objects.filter(app_id=app_id,level='PG',courseType='core').exists() :
        obj3 = SubjectTaught.objects.get(app_id=app_id,level='PG',courseType='core')
        response['corePGobj'] = json.loads(obj3.data)
    if SubjectTaught.objects.filter(app_id=app_id,level='PG',courseType='elective').exists() :
        obj4 = SubjectTaught.objects.get(app_id=app_id,level='PG',courseType='elective')
        response['electivePGobj'] = json.loads(obj4.data)
    if Referral.objects.filter(app_id=app_id).exists() :
        obj5 = Referral.objects.get(app_id=app_id)
        response['refobjs'] = json.loads(obj5.ref_data)

    if PaymentDetails.objects.filter(appID=app_id).count() >0:
        paymentObj = PaymentDetails.objects.get(appID=app_id)
        response['paymentDetails'] = paymentObj
    
    return render(request, 'recruit/main_application.djt', response)

@login_required(login_url='/faculty_login/')
@user_passes_test(checkuserifscrutinyuser,login_url="/faculty_login/")
def viewannex(request, appID):
    response = {}
    response['profile'] = UserProfile.objects.get(applicationID=appID)
    app_id = Appdata.objects.get(app_id=appID)
    response['specialization'] = app_id.specialize
    college = Constants.objects.filter(key='college')
    if college.count() > 0:
        response['college'] = college[0].value

    annex_e1 = Acad_Annex_E12.objects.filter(app_id=app_id)
    if annex_e1.count() > 0:
        if annex_e1[0].annexure_file_e1:
            response['annex_e1_file'] = annex_e1[0].annexure_file_e1
        if len(str((annex_e1[0].annexure_data_e1).encode("utf-8"))) > 1:
            response['annex_e1'] = json.loads(annex_e1[0].annexure_data_e1)

    annex_e2 = Acad_Annex_E12.objects.filter(app_id=app_id)
    if annex_e2.count() > 0:
        if annex_e2[0].annexure_file_e2:
            response['annex_e2_file'] = annex_e2[0].annexure_file_e2   
        if len(str((annex_e2[0].annexure_data_e2).encode("utf-8"))) > 1:
            response['annex_e2'] = json.loads(annex_e2[0].annexure_data_e2)
            

    annex_f = Acad_Annex_F.objects.filter(app_id=app_id)
    if annex_f.count() > 0:
        if annex_f[0].annexure_file:
            response['annex_f_file'] = annex_f[0].annexure_file
        if annex_f[0].annexure_data:
            response['annex_f'] = json.loads(annex_f[0].annexure_data)
            response['annex_f_credit'] = annex_f[0].credit_score


    annex_g = Acad_Annex_G.objects.filter(app_id=app_id)
    if annex_g.count() > 0:
        if annex_g[0].annexure_file:
            response['annex_g_file'] = annex_g[0].annexure_file
        if annex_g[0].annexure_data:
            response['annex_g'] = json.loads(annex_g[0].annexure_data)
            

    annex_h = Acad_Annex_H.objects.filter(app_id=app_id)
    if annex_h.count() > 0:
        if annex_h[0].annexure_file:
            response['annex_h_file'] = annex_h[0].annexure_file
        if annex_h[0].annexure_data:
            response['annex_h'] = json.loads(annex_h[0].annexure_data)
            response['annex_h_last_prom'] = annex_h[0].last_prom
            response['annex_h_file'] = annex_h[0].annexure_file

    annex_i = Acad_Annex_I.objects.filter(app_id=app_id)
    if annex_i.count() > 0:
        if annex_i[0].annexure_file:
            response['annex_i_file'] = annex_i[0].annexure_file
        if annex_i[0].annexure_data:
            response['annex_i'] = json.loads(annex_i[0].annexure_data)
            

    annex_j = Acad_Annex_J.objects.filter(app_id=app_id)
    if annex_j.count() > 0:
        if annex_j[0].annexure_file:
            response['annex_j_file'] = annex_j[0].annexure_file
        if annex_j[0].annexure_data:
            response['annex_j'] = json.loads(annex_j[0].annexure_data)
            response['annex_j_credit'] = annex_j[0].credit_score
            response['annex_j_last_prom'] = annex_j[0].last_prom
            

    annex_k = Acad_Annex_K.objects.filter(app_id=app_id)
    if annex_k.count() > 0:
        if annex_k[0].annexure_file:
            response['annex_k_file'] = annex_k[0].annexure_file
        if annex_k[0].annexure_data:
            response['annex_k'] = json.loads(annex_k[0].annexure_data)
            response['annex_k_credit'] = annex_k[0].credit_score
            response['annex_k_last_prom'] = annex_k[0].last_prom
            

    annex_l = Acad_Annex_L.objects.filter(app_id=app_id)
    if annex_l.count() > 0:
        if annex_l[0].annexure_file:
            response['annex_l_file'] = annex_l[0].annexure_file
        if annex_l[0].annexure_data:
            response['annex_l'] = json.loads(annex_l[0].annexure_data)
            response['annex_l_last_prom'] = annex_l[0].last_prom
            response['annex_l_credit'] = annex_l[0].credit_score
            

    annex_m = Acad_Annex_M.objects.filter(app_id=app_id)
    if annex_m.count() > 0:
        if annex_m[0].annexure_file:
            response['annex_m_file'] = annex_m[0].annexure_file
        if annex_m[0].annexure_data:
            response['annex_m'] = json.loads(annex_m[0].annexure_data)
            response['annex_m_credit'] = annex_m[0].credit_score
            response['annex_m_last_prom'] = annex_m[0].last_prom
            

    annex_n = Acad_Annex_N.objects.filter(app_id=app_id)
    if annex_n.count() > 0:
        if annex_n[0].annexure_file:
            response['annex_n_file'] = annex_n[0].annexure_file
        if annex_n[0].annexure_data:
            response['annex_n'] = json.loads(annex_n[0].annexure_data)
            response['annex_n_last_prom'] = annex_n[0].last_prom
            

    annex_o = Acad_Annex_O.objects.filter(app_id=app_id)
    if annex_o.count() > 0:
        if annex_o[0].annexure_file:
            response['annex_o_file'] = annex_o[0].annexure_file
        if annex_o[0].annexure_data:
            response['annex_o'] = json.loads(annex_o[0].annexure_data)
            response['annex_o_last_prom'] = annex_o[0].last_prom
            

    annex_p = Acad_Annex_P.objects.filter(app_id=app_id)
    if annex_p.count() > 0:
        if annex_p[0].annexure_file:
            response['annex_p_file'] = annex_p[0].annexure_file
        if annex_p[0].annexure_data:
            response['annex_p'] = json.loads(annex_p[0].annexure_data)
            response['annex_p_last_prom'] = annex_p[0].last_prom
            

    annex_q = Acad_Annex_Q.objects.filter(app_id=app_id)
    if annex_q.count() > 0:
        if annex_q[0].annexure_file:
            response['annex_q_file'] = annex_q[0].annexure_file
        if annex_q[0].annexure_data:
            response['annex_q'] = json.loads(annex_q[0].annexure_data)
            response['annex_q_last_prom'] = annex_q[0].last_prom
            response['annex_q_exp_phd'] = annex_q[0].total_exp_after_phd
            response['annex_q_exp_cur'] = annex_q[0].total_exp_cur
            response['annex_q_tot_exp'] = annex_q[0].total_exp
            response['annex_q_credit'] = annex_q[0].credit_score
            

    annex_r = Acad_Annex_R.objects.filter(app_id=app_id)
    if annex_r.count() > 0:
        if annex_r[0].annexure_file:
            response['annex_r_file'] = annex_r[0].annexure_file
        if annex_r[0].annexure_data:
            response['annex_r'] = json.loads(annex_r[0].annexure_data)
            response['annex_r_last_prom'] = annex_r[0].last_prom
            

    annex_s = Acad_Annex_S.objects.filter(app_id=app_id)
    if annex_s.count() > 0:
        if annex_s[0].annexure_file:
            response['annex_s_file'] = annex_s[0].annexure_file
        if annex_s[0].annexure_data:
            response['annex_s'] = json.loads(annex_s[0].annexure_data)
            response['annex_s_last_prom'] = annex_s[0].last_prom
            response['annex_s_extra_load'] = annex_s[0].extra_load
            response['annex_s_credit'] = annex_s[0].credit_score
            

    annex_t = Acad_Annex_T.objects.filter(app_id=app_id)
    if annex_t.count() > 0:
        if annex_t[0].annexure_file:
            response['annex_t_file'] = annex_t[0].annexure_file
        if annex_t[0].annexure_data:
            response['annex_t'] = json.loads(annex_t[0].annexure_data)
            response['annex_t_last_prom'] = annex_t[0].last_prom
            

    annex_u = Acad_Annex_U.objects.filter(app_id=app_id)
    if annex_u.count() > 0:
        if annex_u[0].annexure_file:
            response['annex_u_file'] = annex_u[0].annexure_file
        if annex_u[0].annexure_data:
            response['annex_u'] = json.loads(annex_u[0].annexure_data)
            response['annex_u_last_prom'] = annex_u[0].last_prom
            

    annex_v = Acad_Annex_V.objects.filter(app_id=app_id)
    if annex_v.count() > 0:
        if annex_v[0].annexure_file:
            response['annex_v_file'] = annex_v[0].annexure_file
        if annex_v[0].annexure_data:
            response['annex_v'] = json.loads(annex_v[0].annexure_data)
            response['annex_v_last_prom'] = annex_v[0].last_prom
            
    
    annex_w1 = Acad_Annex_W1_W2.objects.filter(app_id=app_id)
    if annex_w1.count() > 0:
        if annex_w1[0].annexure_file_w1:
            response['annex_w1_file'] = annex_w1[0].annexure_file_w1
        if len(str((annex_w1[0].annexure_data1).encode("utf-8"))) > 1:
            response['annex_w1'] = json.loads(annex_w1[0].annexure_data1)
            response['annex_w1_last_prom'] = annex_w1[0].last_prom_w1
            

    annex_w2 = Acad_Annex_W1_W2.objects.filter(app_id=app_id)
    if annex_w2.count() > 0:
        if annex_w2[0].annexure_file_w1:
            response['annex_w2_file'] = annex_w2[0].annexure_file_w2
        if len(str((annex_w2[0].annexure_data2).encode("utf-8"))) > 1:
            response['annex_w2'] = json.loads(annex_w2[0].annexure_data2)
            response['annex_w2_last_prom'] = annex_w2[0].last_prom_w2
            

    annex_x = Acad_Annex_X.objects.filter(app_id=app_id)
    if annex_x.count() > 0:
        if annex_x[0].annexure_file:
            response['annex_x_file'] = annex_x[0].annexure_file
        if len(str((annex_x[0].annexure_data).encode("utf-8"))) > 1:
            response['annex_x'] = json.loads(annex_x[0].annexure_data)
            response['annex_x_last_prom'] = annex_x[0].last_prom
            

    annex_y = Acad_Annex_Y.objects.filter(app_id=app_id)
    if annex_y.count() > 0:
        if annex_y[0].annexure_file:
            response['annex_y_file'] = annex_y[0].annexure_file
        response['annex_y_credit'] = annex_y[0].credit_score
        response['annex_y_ieee'] = annex_y[0].ieee 
        response['annex_y_fna'] = annex_y[0].fna 
        response['annex_y_fnae'] = annex_y[0].fnae 
        response['annex_y_fnasc'] = annex_y[0].fnasc 
        

    annex_z = Acad_Annex_Z.objects.filter(app_id=app_id)
    if annex_z.count() > 0:
        if annex_z[0].annexure_file:
            response['annex_z_file'] = annex_z[0].annexure_file
        if len(str((annex_z[0].annexure_data).encode("utf-8"))) > 1:
            response['annex_z'] = json.loads(annex_z[0].annexure_data)
            response['annex_z_last_prom'] = annex_z[0].last_prom
            

    annex_a = Acad_Annex_A.objects.filter(app_id=app_id)
    if annex_a.count() > 0: 
        if annex_a[0].annexure_file:
            response['annex_a_file'] = annex_a[0].annexure_file
        if len(str((annex_a[0].annexure_data).encode("utf-8"))) > 1:
            response['annex_a'] = json.loads(annex_a[0].annexure_data)


    return render(request, 'recruit/print_annexures_admin.djt', response)

@login_required(login_url='/payment_login/')
@user_passes_test(checkuserifpaymentuser,login_url="/payment_login/")
def paymentVerify(request, deptID = 1):
    response = {}
    try:
        deptObj = Department.objects.get(deptID = deptID)
    except ObjectDoesNotExist:
        return HttpResponseRedirect('/payment/1/')
    fac=FacUser.objects.filter(app_id__submitted=True,app_id__paymentUploaded=True, app_id__post_in = deptObj.name)
    
    college = Constants.objects.filter(key='college')
    if college.count() > 0:
        response['college'] = college[0].value

    for users in fac:
        if ScrutinizedValues.objects.filter(app_id=users.app_id).count() >0:
            obj = ScrutinizedValues.objects.get(app_id=users.app_id)
            status = obj.payment_accepted
            if status == 0:
                users.payment_status = 'Not Verified'
            elif status == 1:
                users.payment_status = 'Rejected'
            else:
                users.payment_status = 'Verified'
        else:
            users.payment_status = 'Not verified'
        if PaymentDetails.objects.filter(appID=users.app_id).count() >0:
            obj = PaymentDetails.objects.get(appID=users.app_id)
            users.bankName = obj.bankName
            users.TransID = obj.transID
            users.accountNum = obj.accountNum
            users.payDate = obj.payDate
            users.payType = obj.payType
            users.amount = obj.amount
            users.receipt = obj.receipt    
    response['nitw_users']=fac
    response['dept'] = deptObj
    return render(request, 'recruit/payment_verify.djt',response)

@login_required(login_url='/payment_login/')
@user_passes_test(checkuserifpaymentuser,login_url="/payment_login/")
def acceptpayment(request, deptID, appID):
    if ScrutinizedValues.objects.filter(app_id=appID).count() >0:
        obj = ScrutinizedValues.objects.get(app_id=appID)
    else:
        obj = ScrutinizedValues()
        obj.app_id = Appdata.objects.get(app_id = appID)
    obj.payment_accepted = 2
    obj.save()
    return redirect('/payment/' + deptID + '/')

@login_required(login_url='/payment_login/')
@user_passes_test(checkuserifpaymentuser,login_url="/payment_login/")
def rejectpayment(request, deptID, appID):
    if ScrutinizedValues.objects.filter(app_id=appID).count() >0:
        obj = ScrutinizedValues.objects.get(app_id=appID)
    else:
        obj = ScrutinizedValues()
        obj.app_id = Appdata.objects.get(app_id = appID)
    obj.payment_accepted = 1
    obj.save()
    return redirect('/payment/'+ deptID + '/')



def paymentLogin(request):
    if request.user.is_authenticated():
        if checkuserifpaymentuser(request.user):
            return HttpResponseRedirect('/payment/1/')
        else:
            logout(request)
            return HttpResponseRedirect('/payment_login/')
    else:
        response={}
        if request.method == 'POST':
            username=request.POST['username']
            password=request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/payment/1/')
                else:
                    response['message']='User is not active yet'
            else:
                response['message']='User is invalid'
        return render(request, 'recruit/payment_login.djt',response)

def paymentlogout(request):
    logout(request)
    return HttpResponseRedirect('/payment_login/')

def fac_login(request):
    if request.user.is_authenticated():
        if checkuserifscrutinyuser(request.user):
            return HttpResponseRedirect('/faculty_admin/')
        else:
            logout(request)
            return HttpResponseRedirect('/faculty_login/')
    else:
        response={}
        if request.method == 'POST':
            username=request.POST['username']
            password=request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/faculty_admin/')
                else:
                    response['message']='User is not active yet'
            else:
                response['message']='User is invalid'
        return render(request, 'recruit/faculty_login.djt',response)

def fac_logout(request):
    logout(request)
    return HttpResponseRedirect('/faculty_login/')

    
@login_required(login_url='/faculty_login/')
@user_passes_test(checkuserifmasteruser,login_url="/faculty_login/")
def statistics(request):
    response={}
    submitted_outside = ScrutinizedValues.objects.filter(payment_accepted = 2, app_id__submitted=True, app_id__paymentUploaded=True, app_id__is_nitw=False).count()
    response['submitted_outside'] = submitted_outside
    
    sc_accepted = ScrutinizedValues.objects.filter(payment_accepted = 2, application_status = 3, app_id__is_nitw=False).count()
    response['total_accepted_r1'] = sc_accepted
    sc_rejected = ScrutinizedValues.objects.filter(payment_accepted = 2, application_status = 2, app_id__is_nitw=False).count()
    response['total_rejected_r1'] = sc_rejected
    sc_modified = ScrutinizedValues.objects.filter(payment_accepted = 2, application_status = 1, app_id__is_nitw=False).count()
    response['total_modified_r1'] = sc_modified
    sc_unreviewed = submitted_outside - sc_accepted - sc_modified - sc_rejected
    response['total_unreviewed_r1'] = sc_unreviewed

    sc2_accepted = ScrutinizedValues2.objects.filter(application_status = 3, app_id__is_nitw=False).count()
    response['total_accepted_r2'] = sc2_accepted
    sc2_rejected = ScrutinizedValues2.objects.filter(application_status = 2, app_id__is_nitw=False).count()
    response['total_rejected_r2'] = sc2_rejected
    sc2_modified = ScrutinizedValues2.objects.filter(application_status = 1, app_id__is_nitw=False).count()
    response['total_modified_r2'] = sc2_modified
    sc2_unreviewed = submitted_outside - sc2_accepted - sc2_modified - sc2_rejected
    response['total_unreviewed_r2'] = sc2_unreviewed

    submitted_nitw = FacUser.objects.filter(app_id__submitted=True, app_id__is_nitw=True).count()
    response['submitted_nitw'] = submitted_nitw
    sc_accepted = ScrutinizedValues.objects.filter(application_status = 3, app_id__is_nitw=True).count()
    response['total_accepted_r1_nitw'] = sc_accepted
    sc_rejected = ScrutinizedValues.objects.filter(application_status = 2, app_id__is_nitw=True).count()
    response['total_rejected_r1_nitw'] = sc_rejected
    sc_modified = ScrutinizedValues.objects.filter(application_status = 1, app_id__is_nitw=True).count()
    response['total_modified_r1_nitw'] = sc_modified
    sc_unreviewed = submitted_nitw - sc_accepted - sc_modified - sc_rejected
    response['total_unreviewed_r1_nitw'] = sc_unreviewed

    sc2_accepted = ScrutinizedValues2.objects.filter(application_status = 3, app_id__is_nitw=True).count()
    response['total_accepted_r2_nitw'] = sc2_accepted
    sc2_rejected = ScrutinizedValues2.objects.filter(application_status = 2, app_id__is_nitw=True).count()
    response['total_rejected_r2_nitw'] = sc2_rejected
    sc2_modified = ScrutinizedValues2.objects.filter(application_status = 1, app_id__is_nitw=True).count()
    response['total_modified_r2_nitw'] = sc2_modified
    sc2_unreviewed = submitted_nitw - sc2_accepted - sc2_modified - sc2_rejected
    response['total_unreviewed_r2_nitw'] = sc2_unreviewed

    maxValue_nitw = ScrutinizedValues.objects.filter(app_id__is_nitw=True).aggregate(Max('scrutiny_total'))
    maxValue = ScrutinizedValues.objects.filter(app_id__is_nitw=False).aggregate(Max('scrutiny_total'))
    minValue_nitw = ScrutinizedValues.objects.filter(app_id__is_nitw=True).aggregate(Min('scrutiny_total'))
    minValue = ScrutinizedValues.objects.filter(app_id__is_nitw=False).aggregate(Min('scrutiny_total'))
    response['maxValue_nitw'] = maxValue_nitw['scrutiny_total__max']
    response['maxValue'] = maxValue['scrutiny_total__max']
    response['minValue_nitw'] = minValue_nitw['scrutiny_total__min']
    response['minValue'] = minValue['scrutiny_total__min']
    deptcount = Department.objects.all().count()
    final_list = []
    for i in range(1, deptcount + 1):
        # print i
        deptObj = Department.objects.get(deptID = i)
        # response['dept_'+str(i)] = deptObj.name
        deptObj.submitted_outside= ScrutinizedValues.objects.filter(payment_accepted = 2, app_id__submitted=True,app_id__paymentUploaded=True, app_id__is_nitw=False, app_id__post_in = deptObj.name).count()
        # response['submitted_outside'+'_dept_'+str(i)] = submitted_outside
        
        deptObj.sc_accepted = ScrutinizedValues.objects.filter(payment_accepted = 2, application_status = 3, app_id__post_in = deptObj.name, app_id__is_nitw=False).count()
        # response['total_accepted_r1'+'_dept_'+str(i)] = sc_accepted
        deptObj.sc_rejected = ScrutinizedValues.objects.filter(payment_accepted = 2, application_status = 2, app_id__post_in = deptObj.name, app_id__is_nitw=False).count()
        # response['total_rejected_r1'+'_dept_'+str(i)] = sc_rejected

        deptObj.sc_modified = ScrutinizedValues.objects.filter(payment_accepted = 2, application_status = 1, app_id__post_in = deptObj.name, app_id__is_nitw=False).count()
        # response['total_modified_r1'+'_dept_'+str(i)] = sc_modified
        deptObj.sc_unreviewed = deptObj.submitted_outside - deptObj.sc_accepted - deptObj.sc_modified - deptObj.sc_rejected
        # response['total_unreviewed_r1'+'_dept_'+str(i)] = sc_unreviewed



        deptObj.sc2_accepted = ScrutinizedValues2.objects.filter(application_status = 3, app_id__post_in = deptObj.name, app_id__is_nitw=False).count()
        # response['total_accepted_r2'+'_dept_'+str(i)] = sc2_accepted
        deptObj.sc2_rejected = ScrutinizedValues2.objects.filter(application_status = 2, app_id__post_in = deptObj.name, app_id__is_nitw=False).count()
        # response['total_rejected_r2'+'_dept_'+str(i)] = sc2_rejected

        deptObj.sc2_modified = ScrutinizedValues2.objects.filter(application_status = 1, app_id__post_in = deptObj.name, app_id__is_nitw=False).count()
        # response['total_modified_r2'+'_dept_'+str(i)] = sc2_modified
        deptObj.sc2_unreviewed = deptObj.submitted_outside - deptObj.sc2_accepted - deptObj.sc2_modified - deptObj.sc2_rejected
        # response['total_unreviewed_r2'+'_dept_'+str(i)] = sc2_unreviewed

        
        deptObj.submitted_nitw = FacUser.objects.filter(app_id__submitted=True, app_id__is_nitw=True, app_id__post_in = deptObj.name).count()
        # response['submitted_nitw'+'_dept_'+str(i)] = submitted_nitw
        
        deptObj.sc_accepted_nitw = ScrutinizedValues.objects.filter(application_status = 3, app_id__is_nitw=True, app_id__post_in = deptObj.name).count()
        # response['total_accepted_r1_nitw'+'_dept_'+str(i)] = sc_accepted
        deptObj.sc_rejected_nitw = ScrutinizedValues.objects.filter(application_status = 2, app_id__is_nitw=True, app_id__post_in = deptObj.name).count()
        # response['total_rejected_r1_nitw'+'_dept_'+str(i)] = sc_rejected

        deptObj.sc_modified_nitw = ScrutinizedValues.objects.filter(application_status = 1, app_id__post_in = deptObj.name, app_id__is_nitw=True).count()
        # response['total_modified_r1_nitw'+'_dept_'+str(i)] = sc_modified

        deptObj.sc_unreviewed_nitw = deptObj.submitted_nitw - deptObj.sc_accepted_nitw - deptObj.sc_modified_nitw - deptObj.sc_rejected_nitw
        # response['total_unreviewed_r1_nitw'+'_dept_'+str(i)] = sc_unreviewed

        deptObj.sc2_accepted_nitw = ScrutinizedValues2.objects.filter(application_status = 3, app_id__is_nitw=True, app_id__post_in = deptObj.name).count()
        # response['total_accepted_r2_nitw'+'_dept_'+str(i)] = sc2_accepted
        deptObj.sc2_rejected_nitw = ScrutinizedValues2.objects.filter(application_status = 2, app_id__is_nitw=True, app_id__post_in = deptObj.name).count()
        # response['total_rejected_r2_nitw'+'_dept_'+str(i)] = sc2_rejected

        deptObj.sc2_modified_nitw = ScrutinizedValues2.objects.filter(application_status = 1, app_id__post_in = deptObj.name, app_id__is_nitw=True).count()
        # response['total_modified_r2_nitw'+'_dept_'+str(i)] = sc2_modified
        deptObj.sc2_unreviewed_nitw = deptObj.submitted_nitw - deptObj.sc2_accepted_nitw - deptObj.sc2_modified_nitw - deptObj.sc2_rejected_nitw
        # response['total_unreviewed_r2_nitw'+'_dept_'+str(i)] = sc2_unreviewed

        deptObj.maxValue_nitw = ScrutinizedValues.objects.filter(app_id__is_nitw=True, app_id__post_in = deptObj.name).aggregate(Max('scrutiny_total'))['scrutiny_total__max']
        deptObj.maxValue = ScrutinizedValues.objects.filter(app_id__is_nitw=False, app_id__post_in = deptObj.name).aggregate(Max('scrutiny_total'))['scrutiny_total__max']
        deptObj.minValue_nitw = ScrutinizedValues.objects.filter(app_id__is_nitw=True, app_id__post_in = deptObj.name).aggregate(Min('scrutiny_total'))['scrutiny_total__min']
        deptObj.minValue = ScrutinizedValues.objects.filter(app_id__is_nitw=False, app_id__post_in = deptObj.name).aggregate(Min('scrutiny_total'))['scrutiny_total__min']
        # response['maxValue_nitw'+'_dept_'+str(i)] = maxValue_nitw['scrutiny_total__max']
        # response['maxValue'+'_dept_'+str(i)] = maxValue['scrutiny_total__max']
        # response['minValue_nitw'+'_dept_'+str(i)] = minValue_nitw['scrutiny_total__min']
        # response['minValue'+'_dept_'+str(i)] = minValue['scrutiny_total__min']
        final_list.append(deptObj)
    response['departments'] = final_list
    return render(request, 'recruit/stats.djt',response)



@login_required(login_url='/faculty_login/')
@user_passes_test(checkuserifmasteruser,login_url="/faculty_login/")
def log1(request):
    response={}
    fac=FacUser.objects.all()
    final_list_1 = []
    for users in fac:
        if ScrutinizedValues.objects.filter(app_id=users.app_id).count() >0:
            obj = ScrutinizedValues.objects.get(app_id=users.app_id)
            final_list_1.append(obj)
    response['userlist1'] = final_list_1
    college = Constants.objects.filter(key='college')
    if college.count() > 0:
        response['college'] = college[0].value
    return render(request,'recruit/log.djt',response)

@login_required(login_url='/faculty_login/')
@user_passes_test(checkuserifmasteruser,login_url="/faculty_login/")
def log2(request):
    response={}
    fac=FacUser.objects.all()
    final_list_1 = []
    for users in fac:
        if ScrutinizedValues2.objects.filter(app_id=users.app_id).count() >0:
            obj = ScrutinizedValues2.objects.get(app_id=users.app_id)
            final_list_1.append(obj)
    response['userlist1'] = final_list_1
    college = Constants.objects.filter(key='college')
    if college.count() > 0:
        response['college'] = college[0].value
    return render(request,'recruit/log1.djt',response)

def getStatus(status):
    if status == 0:
        return "Not Verified"
    elif status == 1:
        return "Under Review"
    elif status == 2:
        return "Rejected"
    else:
        return "Accepted"

@login_required(login_url='/faculty_login/')
@user_passes_test(checkuserifmasteruser,login_url="/faculty_login/")
def export_ext(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=UserExternalData.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    depts = Department.objects.all()
    for dept in depts :
        ws = wb.add_sheet(dept.name.split(" ")[0])
    #ws = wb.add_sheet("ExternalApplications")

    	row_num = 0

    	columns = [
        	(u"Application ID",6000),
        	(u"Full name", 6000),
		(u"Age",6000),
        	(u"category",6000),
        	(u"PWD",6000),
        	(u"Department",6000),
        	(u"post applied",20000),
	
        	(u"annex_e1",6000),
        	(u"annex_e2",6000),
        	(u"annex_f",6000),
        	(u"annex_g",6000),
        	(u"annex_h",6000),
        	(u"annex_i",6000),
        	(u"annex_j",6000),
        	(u"annex_k",6000),
        	(u"annex_l",6000),
        	(u"annex_m",6000),
        	(u"annex_n",6000),
        	(u"annex_o",6000),
        	(u"annex_p",6000),
        	(u"annex_q",6000),
        	(u"annex_r",6000),
        	(u"annex_s",6000),
        	(u"annex_t",6000),
        	(u"annex_u",6000),
        	(u"annex_v",6000),
        	(u"annex_w",6000),
        	(u"annex_w2",6000),
        	(u"annex_x",6000),
        	(u"annex_y",6000),
        	(u"annex_z",6000),
        	(u"scrutiny_total",6000),
	
	        (u"status",6000),
	        (u"remarks", 20000),
	]

    	font_style = xlwt.XFStyle()
    	font_style.font.bold = True

    	for col_num in xrange(len(columns)):
        	ws.write(row_num, col_num, columns[col_num][0], font_style)
        	ws.col(col_num).width = columns[col_num][1]

    	font_style = xlwt.XFStyle()
    	font_style.alignment.wrap = 1

    	Outside_applications = ScrutinizedValues.objects.filter(payment_accepted = 2, app_id__submitted=True, app_id__paymentUploaded=True, app_id__is_nitw=False,app_id__post_in=dept.name)

    	for obj in Outside_applications:
	
		if FacUser.objects.filter(app_id = obj.app_id).count()==0:
			print "missing Facuser : "+str(obj.app_id)
			continue
        	row_num += 1
        	Facobj = FacUser.objects.get(app_id = obj.app_id)
        	status = getStatus(obj.application_status)

        	dataRow = [obj.app_id.app_id, Facobj.full_name, Facobj.age, Facobj.category, Facobj.pwd, obj.app_id.post_in, obj.app_id.post_for,
        	obj.annex_e1,
        	obj.annex_e2,
        	obj.annex_f,
        	obj.annex_g,
        	obj.annex_h,
        	obj.annex_i,
        	obj.annex_j,
        	obj.annex_k,
        	obj.annex_l,
        	obj.annex_m ,
        	obj.annex_n,
        	obj.annex_o,
        	obj.annex_p ,
        	obj.annex_q ,
        	obj.annex_r,
        	obj.annex_s ,
        	obj.annex_t ,
        	obj.annex_u ,
        	obj.annex_v ,
        	obj.annex_w ,
        	obj.annex_w2 ,
        	obj.annex_x ,
        	obj.annex_y ,
        	obj.annex_z ,
        	obj.scrutiny_total ,
        	status ,
        	obj.remarks
        	]

        	for col_num in xrange(len(dataRow)) :
            		ws.write(row_num, col_num, dataRow[col_num], font_style)

    wb.save(response)
    return response

@login_required(login_url='/faculty_login/')
@user_passes_test(checkuserifmasteruser,login_url="/faculty_login/")
def export_int(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=UserInternalData.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    depts = Department.objects.all()
    for dept in depts :
	ws = wb.add_sheet(dept.name.split(" ")[0])	
    #ws = wb.add_sheet("InternalApplications")

    	row_num = 0

    	columns = [
        	(u"Application ID",6000),
        	(u"Full name", 6000),
		(u"Age",6000),
        	(u"category",6000),
        	(u"PWD",6000),
        	(u"Department",6000),
        	(u"post applied",20000),
	
        	(u"annex_e1",6000),
        	(u"annex_e2",6000),
        	(u"annex_f",6000),
        	(u"annex_g",6000),
        	(u"annex_h",6000),
        	(u"annex_i",6000),
        	(u"annex_j",6000),
        	(u"annex_k",6000),
        	(u"annex_l",6000),
        	(u"annex_m",6000),
        	(u"annex_n",6000),
        	(u"annex_o",6000),
        	(u"annex_p",6000),
        	(u"annex_q",6000),
        	(u"annex_r",6000),
        	(u"annex_s",6000),
        	(u"annex_t",6000),
        	(u"annex_u",6000),
        	(u"annex_v",6000),
        	(u"annex_w",6000),
        	(u"annex_w2",6000),
        	(u"annex_x",6000),
        	(u"annex_y",6000),
        	(u"annex_z",6000),
        	(u"scrutiny_total",6000),
        	(u"status",6000),
        	(u"remarks", 20000),
    	]		

    	font_style = xlwt.XFStyle()
    	font_style.font.bold = True
	
	for col_num in xrange(len(columns)):
        	ws.write(row_num, col_num, columns[col_num][0], font_style)
        	ws.col(col_num).width = columns[col_num][1]

    	font_style = xlwt.XFStyle()
    	font_style.alignment.wrap = 1

    	Internal_applications = ScrutinizedValues.objects.filter(app_id__submitted=True, app_id__is_nitw=True,app_id__post_in = dept.name)

    	for obj in Internal_applications:

        	row_num += 1
        	Facobj = FacUser.objects.get(app_id = obj.app_id)
        	status = getStatus(obj.application_status)
        	dataRow = [obj.app_id.app_id, Facobj.full_name, Facobj.age, Facobj.category, Facobj.pwd, obj.app_id.post_in, obj.app_id.post_for,
        	obj.annex_e1,
        	obj.annex_e2,
        	obj.annex_f,
        	obj.annex_g,
        	obj.annex_h,
        	obj.annex_i,
        	obj.annex_j,
        	obj.annex_k,
        	obj.annex_l,
        	obj.annex_m ,
        	obj.annex_n,
        	obj.annex_o,
        	obj.annex_p ,
        	obj.annex_q ,
        	obj.annex_r,
        	obj.annex_s ,
        	obj.annex_t ,
        	obj.annex_u ,
        	obj.annex_v ,
        	obj.annex_w ,
        	obj.annex_w2 ,
        	obj.annex_x ,
        	obj.annex_y ,
        	obj.annex_z ,
        	obj.scrutiny_total ,
        	status,
        	obj.remarks
        	]
        	# dataRow = ["hceck", "ma"]
        	for col_num in xrange(len(dataRow)) :
        	    ws.write(row_num, col_num, dataRow[col_num], font_style)
	
    wb.save(response)
    return response
