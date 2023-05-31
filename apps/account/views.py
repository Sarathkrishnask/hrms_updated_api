"""
import django functions
"""
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.hashers import make_password,check_password
from rest_framework.response import Response

"""
import apps,models,serializers
"""
from apps.account import models as account_models
from apps.account.models import OTPAuth as otp_auth
# from apps.account.models import User
from apps.account.serializers import *
from apps.admin import models as admin_models
from hrms import settings


"""
import restframeworks functions
"""
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status

"""
import utils functions
"""
from utils import json,validators
from utils import functions
from utils import permissions as cust_perms

"""
other imports
"""
from apps.account.helpers import *
import random
import json as j
import logging
# from appsacmec_admin import models as admin_models
logger = logging.getLogger(__name__)
User = get_user_model()


# class UserRegister(APIView):
#     """
#     Registeration of user
#     """

#     permission_classes=[permissions.AllowAny,]

#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args, **kwargs):
#         return super(UserRegister, self).dispatch(request, *args, **kwargs)

#     @csrf_exempt
#     def post(self, request):
#         print("data_in")
#         datas = j.loads(request.body.decode('utf-8'))
#         print(datas)
#         try:
#             params = self.request.query_params
#             if params.get('login_type') == "0":
#                 """
#                 mobile registeration
#                 """
#                 if validators.user_phone_register_validators(datas)==False:
#                     print("user_phone_register_validators")
#                     return json.Response({"data":[]},"Required Field is missing",400,False)
                
#                 if datas["firstname"]=="" or datas["lastname"]=="" or datas["phone"]=="" or datas["email"]=="" or datas["role"]=="" or datas["password"] == "" or datas["confirm_password"]=="":
#                     print("empty_Str")
#                     return json.Response({"data":[]},"Field is empty",400,False)

#                 if datas["country_code"]=="": 
#                     print("countrycode")
#                     return json.Response({"data":[]},"countrycode is empty",400,False)
                
#                 if datas["country_code"]=="+91":
#                     print("91")
#                     if datas['personal_id'] !='':
#                         print("personal_id")
#                         pan=functions.verify_personalid(datas['personal_id'])
#                         if pan==False:
#                             print("pan_false")
#                             return json.Response({"data":[]},"pancard not verified",400, False)
#                         if pan==True:
#                             print("pan_true")
                
#                 Users_data = models.User.objects
#                 User_filter = Users_data.filter(phone_number=datas['phone'])
#                 User_email = Users_data.filter(email=datas['email'])

#                 if User_filter.exists():
#                     print("phn_exist")
#                     return json.Response({"data":[]},"Phone number already exists!",400,False)
                
#                 if  User_email.exists():
#                     print("email_exist")
#                     return json.Response({"data":[]},"Email already exists!",400,False)
                
#                 if datas["password"].lower() != datas["confirm_password"].lower():
#                     return json.Response({"data":[]}, "Password and confirm password are not same", 400, False)
                
#                 if not models.role_master.objects.filter(id=datas['role']).exists():
#                     return json.Response({"data":[]},"There is no role for this type",400,False)

#                 rolelist = models.role_master.objects.filter(id=datas['role']).first()

#                 if str(rolelist).lower() == "employee":
#                     if validators.user_email_register_validators(datas) == False:
#                         print("is_verify_missing")
#                         return json.Response({"data":[]},"Is_verified Field is missing",400,False)
#                     if datas["is_verified"]==False: 
#                         print("verify_otp")
#                         return json.Response({"data":[]},"OTP not verified. Please verify your otp",400,False)
#                     Users_data.create(firstname=datas["firstname"],lastname=datas["lastname"],phone_number=datas['phone'],email=datas['email'],is_active=True,is_email_verified=False,is_phone_verified=True,roles_id=datas["role"],password=make_password(datas["password"]),personalid=datas['personal_id'],country_code=datas['country_code'])
#                     user_datas = models.User.objects.get(phone_number=datas['phone'])
#                     user_Name_id = models.User.objects.filter(phone_number=datas['phone']).first()
#                     user_details = {}
#                     getjwt=functions.phoneauth(user_datas,user_Name_id.id)
#                     user_details['access_token'] = getjwt['access_token']
#                     user_details['refresh_token'] = getjwt['refresh_token']
#                     user_details['user_info'] = {"id":user_Name_id.id,
#                                                 "name":str(user_Name_id.firstname) + str(user_Name_id.lastname),
#                                                 "email":user_Name_id.email,
#                                                 "phone_number":user_Name_id.phone_number,
#                                                 "image":user_Name_id.image}
#                     return json.Response({"data":user_details},"User created successfully",201,True)
                
#                 else:
#                     return json.Response({"data":[]},"Only user can be created",400,False)
            
#             if params.get('login_type') == "1":
#                 """
#                 User Email registeration
#                 """
#                 if validators.admin_email_register_validators(datas)==False:
#                     return json.Response({"data":[]},"Required field is missing",400,False)

#                 if datas["firstname"]=="" or datas["lastname"]=="" or datas["phone"]=="" or datas["email"]=="" or datas["role"]=="" or datas["password"] == "" or datas["confirm_password"]=="":
#                     return json.Response({"data":[]},"Field is empty",400,False)
                
#                 if datas["country_code"]=="": 
#                     return json.Response({"data":[]},"countrycode is empty",400,False)
#                 if datas["country_code"]=="+91":
#                     if datas['personal_id'] !='':
              
#                         pan=functions.verify_personalid(datas['personal_id'])
#                         if pan==False:
#                             return json.Response({"data":[]},"pancard not verified",400, False)

#                 Users_data = models.User.objects
#                 User_filter = Users_data.filter(phone_number=datas['phone'])
#                 User_email = Users_data.filter(email=datas['email'])

#                 if User_filter.exists():
#                     return json.Response({"data":[]},"Phone number already exists!",400,False)
                
#                 if  User_email.exists():
#                     return json.Response({"data":[]},"Email already exists!",400,False)
                
#                 if datas["password"].lower() != datas["confirm_password"].lower():
#                     return json.Response({"data":[]}, "Password and confirm password are not same", 400, False)

#                 if not models.role_master.objects.filter(id=datas['role']).exists():
#                     return json.Response({"data":[]},"There is no role for this type",400,False)

#                 rolelist = models.role_master.objects.filter(id=datas['role']).first()
    
#                 if str(rolelist).lower() == "employee":
#                     if validators.user_email_register_validators(datas) == False:
#                         return json.Response({"data":[]},"Is_verified Field is missing",400,False)
#                     if datas["is_verified"]==False:
#                         return json.Response({"data":[]},"OTP not verified. Please verify your otp",400,False)
#                     Users_data.create(firstname=datas["firstname"],lastname=datas["lastname"],phone_number=datas['phone'],email=datas['email'],is_active=True,is_email_verified=True,is_phone_verified=False,roles_id=datas["role"],password=make_password(datas["password"]),personalid=datas['personal_id'],country_code=datas['country_code'])
#                     user_datas = models.User.objects.get(email=datas['email'])
#                     user_Name_id = models.User.objects.filter(email=datas['email']).first()
#                     user_details = {}
#                     getjwt=functions.emailauth(user_datas,user_Name_id.id)
#                     user_details['access_token'] = getjwt['access_token']
#                     user_details['refresh_token'] = getjwt['refresh_token']
#                     user_details['user_info'] = {"id":user_Name_id.id,
#                                                 "name":str(user_Name_id.firstname) + str(user_Name_id.lastname),
#                                                 "email":user_Name_id.email,
#                                                 "phone_number":user_Name_id.phone_number,
#                                                 "image":user_Name_id.image}
#                     return json.Response({"data":user_details},"User created successfully",201,True)
                
#                 else:
#                     return json.Response({"data":[]},"Only user can be created",400,False)
                
#         except Exception as e:
#             return json.Response({"data":[]},f"{e}Internal Server Error", 400,False)
        

class loginApi(APIView):
    """
    login using Email
    """
    
    permission_classes=[permissions.AllowAny]

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(loginApi, self).dispatch(request, *args, **kwargs)

    @csrf_exempt
    def post(self,request):
        try:
            
            datas = j.loads(request.body.decode('utf-8'))
            if validators.Email_Login_Validators(datas) == False:
                return json.Response({"data":[]},"Required field is missing",400,False)
            print("Login successful")
            user_data = account_models.User.objects 
            print(user_data)
            if not user_data.filter(email=datas['email']).exists():
                return json.Response({"data":[]},"Please enter registered email",400, False)

            if not user_data.filter(email=datas['email'],roles_id=datas['role']).exists():
                return json.Response({"data":[]},"Please enter registered email Id",400, False)

            if len(datas['password']) == 0 or datas['password'] == '':
                return json.Response({"data":[]},"Please enter password",400, False)
            
            users = user_data.get(email=datas['email'])

            if check_password(datas['password'],users.password) == False:
                print("check_password")
                return json.Response({"data":[]},"Incorrect password",400, False)

            user_datas = account_models.User.objects.get(email=datas['email'])
            user_Name_id = account_models.User.objects.filter(email=datas['email']).first()
            
            user_details = {}
            if int(user_Name_id.roles_id) == 1:
                print("Login successful")
                getjwt=functions.emailauth(user_datas,user_Name_id.id)
                user_details['access_token'] = getjwt['access_token']
                user_details['refresh_token'] = getjwt['refresh_token']
                user_details['user_info'] = {"id":user_Name_id.id,
                                                    "name":str(user_Name_id.firstname)+' '+str(user_Name_id.lastname),
                                                    "email":user_Name_id.email,
                                                    "phone_number":user_Name_id.phone_number,
                                                    "image":user_Name_id.image,
                                                    "role_id":user_Name_id.roles_id}
            else:
                users.save()
                getjwt=functions.emailauth(user_datas,user_Name_id.id)
                user_details['access_token'] = getjwt['access_token']
                user_details['refresh_token'] = getjwt['refresh_token']
                user_details['user_info'] = {"id":user_Name_id.id,
                                                    "name":str(user_Name_id.firstname)+' '+str(user_Name_id.lastname),
                                                    "email":user_Name_id.email,
                                                    "phone_number":user_Name_id.phone_number,
                                                    "image":user_Name_id.image,
                                                    "role_id":user_Name_id.roles_id}
                                                    # "login_count":user_Name_id.login_count + 1}
            return json.Response({"data":user_details},"Logged In Successfully",200,True)

        except Exception as e:
            return json.Response({"data":[]},f"{e}Internal Server Error", 400,False)
        

class ForgetAccount(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self,request):
        try:
            data=request.data
            email=data['email']
            check_email=User.objects.filter(email=email).exists()
            if not check_email:
                res = {"status":False,'message':'Kindly Enter The Registered email','data':[]}
                return Response(res,status=status.HTTP_400_BAD_REQUEST)
            
            user=account_models.User.objects.filter(email=email).last()
            # generate OTP and save with USERTEMP
            otp_val=generate_otp()
            email_body = (f"Use This Otp for verification {otp_val}")
            email_subject="forget_password"
            mail=send_mail_toTemplate(email_subject,email_body,email,settings.EMAIL_HOST_USER)  
            
            save_temp=otp_auth.objects.create(otp=otp_val,user_id=user.id)
            
            res = {'status':True,'message':'OTP send successfully to given email','data':[]}
            return Response(res,status = status.HTTP_200_OK)
                       
        except Exception as e:
            logger.info(f"{e}: forget password")
            return json.Response({"data":[]},f"{e}Internal Server Error", 400,False)


class Changepassword(APIView):
    permission_classes=[permissions.AllowAny]

    def post(self,request):
        try:
            data=request.data                            
            password=data['password']
            cf_password=data['confirm_password']
            email=data['email']
            
            user = account_models.User.objects.filter(email=email).last()
            if not (password==cf_password):
                res = {'status':False,'message':'Password and Confirm Password are Mismatched','data':[]}
                return Response(res,status = status.HTTP_400_BAD_REQUEST)   
            user.password=make_password(password)
            user.save()
            res = {'status':True,'message':'Password changed successfully','data':[]}
            return Response(res,status = status.HTTP_200_OK)
        except Exception as e:
            logger.info(f"{e}: change password")
            res = {'status':False,'message':f'{e}Internal Server Error','data':[]}
            return Response(res,status=status.HTTP_400_BAD_REQUEST)
        
class Resend_OTP(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self,request):
        try:
            data = request.data
            user=account_models.User.objects.filter(email=data['email']).last()
            # generate OTP and save with USERTEMP
            otp_val=generate_otp()
            email_body = (f"Use This Otp for verification {otp_val}")
            email_subject="forget_password"
            mail=send_mail_toTemplate(email_subject,email_body,data['email'],settings.EMAIL_HOST_USER)  
            
            save_temp=otp_auth.objects.update(otp=otp_val,user_id=user.id)
            
            res = {'status':True,'message':'OTP send successfully to given email','data':[]}
            return Response(res,status = status.HTTP_200_OK)
        
        except Exception as e:
            logger.info(f"{e}: resent otp")
            res = {'status':False,'message':f'{e}Internal Server Error','data':[]}
            return Response(res,status=status.HTTP_400_BAD_REQUEST)
