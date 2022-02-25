from distutils.command.upload import upload
from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.

class Doctor(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE, related_name='Doctor')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to = 'asset/profile-pic', default= 'asset/profile-pic/default.png')
    qualification_higest = models.CharField(max_length=40 , blank=True)
    specilization = models.CharField(max_length=100 ,blank=True)
    about = models.CharField(max_length=500 ,blank=True)
    phone_no = models.IntegerField(default=0 ,blank=True)
    add_line_1 = models.CharField(max_length=50 , blank=True)
    add_city = models.CharField(max_length=50  , blank=True)
    add_state = models.CharField(max_length=20 , blank=True)
    add_Pincode = models.IntegerField(default=0 ,blank=True)
    def __str__(self):
        return str(self.user)


class Patient(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE, related_name='Patient')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to = 'asset/profile-pic' , default= 'asset/profile-pic/default.png')
    add_line_1 = models.CharField(max_length=50 , blank=True)
    add_city = models.CharField(max_length=50 , blank=True)
    add_state = models.CharField(max_length=20 , blank=True)
    phone_no = models.IntegerField(default=0 ,blank=True)
    add_Pincode = models.IntegerField(default=0 ,blank=True)
    def __str__(self):
        return str(self.user)