# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# from turtle import Turtle
# from types import CoroutineType

from django.contrib.auth import models as auth_models
from django.db import models
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils.translation import gettext_lazy as _

from apps.account import managers
from apps.generics import models as generic_models
# from apps.generics import tasks



class User(auth_models.AbstractBaseUser):
    """Custom user model that supports using email instead of username"""

    firstname = models.CharField(max_length=64)

    lastname = models.CharField(max_length=64)

    email = models.EmailField(max_length=64, unique=True)

    qualification = models.CharField(max_length=128,null=True,blank=True)

    emp_id = models.CharField(max_length=128,unique=True)

    address1 = models.TextField(blank=True, null=True)

    address2 = models.TextField(blank=True, null=True)

    phone_number = models.CharField(max_length=100, blank=True, null=True)

    roles = models.ForeignKey('RoleMaster', blank=True, null=True, on_delete=models.CASCADE)

    image = models.CharField(max_length=255, null=True,blank=True)

    is_active = models.BooleanField(default=True)

    is_staff = models.BooleanField(default=False)

    last_login = models.DateTimeField(null=True)

    login_count = models.PositiveIntegerField(null=True)

    is_email_verified = models.BooleanField(default=False)

    is_phone_verified = models.BooleanField(default=False)

    city = models.CharField(max_length=100, blank=True, null=True)

    state = models.CharField(max_length=200, blank=True, null=True)

    country = models.CharField(max_length=200, blank=True, null=True)

    pincode = models.IntegerField(null =True,blank=True)
    
    updated_at = models.DateTimeField(auto_now=True)

    objects = managers.UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        db_table = 'hrms_auth_user'
    
    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self


class OTPAuth(models.Model):
    "Model for handling user authentication via OTP"
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=12)
    expired_by = models.DateTimeField(null=True,blank=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True)
    updated_on = models.DateTimeField(auto_now=True,null=True)

    class Meta:
        db_table = 'hrms_otp_auth'



class RoleMaster(models.Model):
    "Model for handling user role"
    
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = 'hrms_role_master'

# class TempOTP(models.Model):
#     """
#     Model for handling user authentication via OTP
#     """
    
#     phone = models.CharField(max_length=20,null=True,blank=True)
#     email = models.EmailField(null=True,blank=True,max_length=200)
#     otp = models.CharField(max_length=12)
#     expired_by = models.DateTimeField(null=True,blank=True)
#     created_on = models.DateTimeField(auto_now_add=True,null=True)
#     updated_on = models.DateTimeField(auto_now=True,null=True)

#     class Meta:
#         db_table = 'hrms_temp_otp'

