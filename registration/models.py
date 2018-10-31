# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

def get_profilepic_path(instance,filename):
	return 'users/{0}/profilepic/{1}'.format(instance.applicationID,filename)

def get_pay_path(instance,filename):
	return 'users/{0}/payment/{1}'.format(instance.appID,filename)

class UserProfile(models.Model):
	user = models.ForeignKey(User)
	applicationID = models.CharField(max_length=20)
	contact = models.CharField(max_length=14)
	departmentApplied = models.CharField(max_length=50)
	postApplied = models.CharField(max_length=100)
	termsRead = models.BooleanField(default=False)
	profilePic = models.ImageField(upload_to=get_profilepic_path,null=True,blank=True)

	def __str__(self):
		return (self.applicationID+"-"+self.user.first_name+" "+self.user.last_name)

class Department(models.Model):
	name = models.CharField(max_length=100)
	deptID = models.IntegerField()
	appCount = models.IntegerField()

	def __str__(self) :
		return self.name

class Post(models.Model):
	name = models.CharField(max_length=50)
	postID = models.IntegerField()

	def __str__(self):
		return self.name

class PaymentDetails(models.Model) :
	appID = models.CharField(max_length=20)
	bankName = models.CharField(max_length=100,blank=True,null=True)
	transID = models.CharField(max_length=512, blank=True)
	accountNum = models.CharField(max_length=30)
	payDate = models.CharField(max_length=20,blank=True,null=True)
	payType = models.CharField(max_length=10,blank=True,null=True)
	amount = models.CharField(max_length=10,blank=True,null=True)
	receipt = models.FileField(upload_to=get_pay_path, validators=[FileExtensionValidator(["pdf"])], null=True, blank=True)

	def __str__(self):
		return self.appID
