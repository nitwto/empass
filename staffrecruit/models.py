# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.validators import FileExtensionValidator
from staffregistration.models import *


# Create your models here.
class StaffApp(models.Model):
	app_id = models.CharField(max_length=20,primary_key=True)
	user = models.ForeignKey(User, default=None)
	post = models.ForeignKey(Post,default=None)
	submitted = models.BooleanField(default=False)
	paymentUploaded = models.BooleanField(default=False)
	internal_id = models.IntegerField(default=0)
	submitDate = models.DateTimeField(blank=True,default=datetime.datetime.now,auto_now=False, auto_now_add=False)

	def __unicode__(self):
		return str(self.app_id)

class Address(models.Model):
	addr1 = models.CharField(max_length=255)
	addr2 = models.CharField(max_length=255,blank=True)
	city = models.CharField(max_length=255)
	state = models.CharField(max_length=255)
	country = models.CharField(max_length=63)
	pin = models.CharField(max_length=31)

	def __unicode__(self):
		return str(self.state)+"_"+str(self.city)

class Education(models.Model):
	e_id=models.AutoField(primary_key=True)
	degree=models.CharField(max_length=255)
	university=models.CharField(max_length=255)
	yearofpassing=models.CharField(max_length=255)
	cgpa=models.CharField(max_length=255)
	classdiv=models.CharField(max_length=255)

	def __unicode__(self):
		return str(self.e_id)

class Experience(models.Model):
	e_id=models.AutoField(primary_key=True)
	org=models.CharField(max_length=255)
	designation=models.CharField(max_length=255)
	doj=models.CharField(max_length=255)
	dol=models.CharField(max_length=255)
	pay=models.CharField(max_length=255)
	service=models.CharField(max_length=255)

	def __unicode__(self):
		return str(self.e_id)

class Membership(models.Model):
	m_id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=255)

	def __unicode__(self):
		return str(self.m_id)

class Extracurr(models.Model):
	ex_id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=255)

	def __unicode__(self):
		return str(self.ex_id)

class Adminpos(models.Model):
	a_id=models.AutoField(primary_key=True)
	resp_held=models.CharField(max_length=255)
	duration=models.CharField(max_length=255)

	def __unicode__(self):
		return str(self.a_id)

class Language(models.Model):
	l_id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=255)
	read=models.BooleanField(default=False)
	write=models.BooleanField(default=False)
	speak=models.BooleanField(default=False)

	def __unicode__(self):
		return str(self.l_id)

class Reference(models.Model):
	r_id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=255)
	address=models.CharField(max_length=255)
	email=models.CharField(max_length=255)
	phone=models.CharField(max_length=255)
	mobile=models.CharField(max_length=255)

	def __unicode__(self):
		return str(self.r_id)

def get_proof_path(instance,filename):
	return 'staffusers/{0}/proof/{1}'.format(instance.appID,filename)

class Proof(models.Model):
	appID=models.CharField(max_length=255)
	prooffile=models.FileField(upload_to=get_proof_path,null=True)
	def __unicode__(self):
		return str(self.appID)


class StaffUser(models.Model):

	app_id = models.ForeignKey(StaffApp)
	full_name = models.CharField(max_length=255)
	gender = models.CharField(max_length=200)
	father_name = models.CharField(max_length=255)
	father_occ = models.CharField(max_length=255)
	mother_name = models.CharField(max_length=255)
	mother_occ = models.CharField(max_length=255,blank=True)
	nation = models.CharField(max_length=255)
	pob = models.CharField(max_length=255)
	dob = models.CharField(max_length=20,default="NA")
	age = models.IntegerField(default=0)
	maritalstatus=models.CharField(max_length=255)
	permanent_addr = models.ForeignKey(Address, related_name='permanent_addr')
	correspond_addr = models.ForeignKey(Address, related_name='correspond_addr')
	category = models.CharField(max_length=10,blank=True)
	obccreamy=models.CharField(max_length=255)
	pwd = models.CharField(max_length=10,default='no')
	educationdet=models.ManyToManyField(Education)
	exprdet=models.ManyToManyField(Experience)
	languages=models.ManyToManyField(Language)
	memberships=models.ManyToManyField(Membership)
	adminpos=models.ManyToManyField(Adminpos)
	extracurr=models.ManyToManyField(Extracurr)
	proof=models.ManyToManyField(Proof)
	refrences=models.ManyToManyField(Reference)

	def __unicode__(self):
		return str(self.full_name)+"_"+str(self.app_id.app_id)



