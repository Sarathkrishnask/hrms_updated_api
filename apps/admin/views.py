

"""
import apps,models,serializers
"""
from apps.account import models as account_models
from apps.admin import serializers as admin_serializers
from apps.account.serializers import *
from apps.admin import models as admin_models

"""
import restframeworks functions
"""
from rest_framework.views import APIView
from rest_framework import generics,permissions
from django.contrib.auth.hashers import make_password,check_password
# Create your views here.


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



# class UserListApiView(generics.GenericAPIView):
#     """
#     List users in adminpanel
#     """
#     permission_classes=[permissions.IsAuthenticated,cust_perms.ISSuperAdmin]
#     queryset = account_models.User.objects.all()
#     serializer_class = admin_serializers.UserListSerializer

#     def get(self, request):
#         try:
#             queryset = self.filter_queryset(self.get_queryset())            
#             serializer = self.get_serializer(queryset, many=True)
#             data = json.Response(serializer.data,'Listed successfully',200,True)
#             return data
#         except Exception as e:
#             return json.Response({'data':[]},f'{e}Internal Server Error',400,False)
        


# class UserDetailApiView(APIView):
#     """
#     get particular user detail in adminpanel
#     """
#     permission_classes=[permissions.IsAuthenticated,cust_perms.ISSuperAdmin]

#     def get(self, request):
#         """
#         admin can access particualar user detail with id in params 
#         """

#         try:
#             id_=self.request.query_params.get('id')
#             if id_:
#                 queryset = account_models.User.objects.filter(id=id_)
#                 serializer = admin_serializers.UserDetailViewSerializers(queryset, many=True)  
#                 return json.Response({"data":serializer.data}," particular user detail accessed successfully",200,True)
#             elif id_ is None :
#                 return json.Response({"data":id_},"No user", 400, False)
#         except Exception as e:
#             return json.Response({"data":[]},f"{e}Internal Server Error", 400, False)
        
#     def put(self, request):
#         id_=request.query_params.get('id')
#         datas = j.loads(request.body.decode('utf-8'))
#         Users_data = account_models.User.objects
#         user_exists = Users_data.filter(id=id_).exists()
#         if user_exists:
#             print("Existing user")
#             Users_data.filter(id=id_).update(firstname=datas["firstname"],
#                             lastname=datas["lastname"],
#                             phone_number=datas['phone'],
#                             email=datas['email'],
#                             roles_id=datas["role"],
#                             city=datas["city"],
#                             state=datas["state"],
#                             country=datas["country"],
#                             address1=datas["address1"],
#                             address2=datas["address2"],
#                             image=datas["image"],
#                             pincode=datas["pincode"])
#             user_Name_id = account_models.User.objects.filter(email=datas['email']).first()
#             return json.Response({"data":user_Name_id.id},"User updated successfully",201,True)
#         return json.Response({"data":[]},"User not existed",400,False)
    
#     def delete(self,request):
#         id_=request.query_params.get('id')
#         datas = j.loads(request.body.decode('utf-8'))
#         Users_data = account_models.User.objects
        
#         try:
#             user_exists = Users_data.filter(id=id_).exists()
#             print(user_exists)
#             if user_exists:
#                 user_details=account_models.User.objects.get(id=id_)
#                 user_details.delete()
#                 # print(user_details,user_details.firstname,user_details.lastname,user_details.phone_number)
#             return json.Response({"data":user_details.firstname},"User deleted successfully",201,True)
                
#         except Exception as e:
#             return json.Response({"data":[]},f"{e}User not existed",400,False)
        
class RoleMaster(APIView):

    permission_classes=[permissions.IsAuthenticated,cust_perms.ISSuperAdmin]

    def post(self,request):
        datas = j.loads(request.body.decode('utf-8'))
        if not account_models.RoleMaster.objects.filter(name=datas['role']).exists():
            account_models.RoleMaster.objects.create(name=datas['role'])
            return json.Response([],"User created successfully",200,True)
        else:
            return json.Response([],"Role already exists",400,False)
    
    def get(self,request):
        role_id = request.query_params.get('id')
        if role_id:
            role = account_models.RoleMaster.objects.filter(id=role_id).last()
            print(role)
            role_data = RoleMasterSerilaizer(role)
            return json.Response(role_data.data,"",200,True)
        role = account_models.RoleMaster.objects.all()         
        role_data = RoleMasterSerilaizer(role,many=True)
        return json.Response(role_data,"",200,True)
    
    def put(self,request):  
        role = request.data 
        roleobj = account_models.RoleMaster.objects.filter(id=role['id']).last()
        roledata = RoleMasterSerilaizer(roleobj,data=role)
        if roledata.is_valid(raise_exception=True):    
            roledata.save()
            return json.Response([],"Role updated successfully",200,True)
        return json.Response([],"serializer is not valid",400,False)
    
    def delete(self,request):  
        account_models.RoleMaster.objects.filter(id=request.query_params.get('id')).delete()
        return json.Response([],"Role deleted successfully",200,True)

        
class ManageEmployee(APIView):

    permission_classes=[permissions.IsAuthenticated,cust_perms.ISSuperAdmin]

    def get(self,request):
        role_id = request.query_params.get('id')
        if role_id:
            role = account_models.User.objects.filter(id=role_id).last()
            print(role)
            role_data = EmployeeSerializer(role)
            return json.Response(role_data.data,"",200,True)
        role = account_models.User.objects.all()         
        role_data = EmployeeSerializer(role,many=True)
        return json.Response(role_data,"",200,True)
    
    def post(self,request):
        try:
            data = j.loads(request.body.decode('utf-8'))
            password = generate_random_password()
            data['password']=make_password(password)
            data['emp_id'] = generate_empids()
            user_data = EmployeeSerializer(data=data)
            if user_data.is_valid(raise_exception=True):
                print(data)    
                user_data.save()
            return json.Response([],"User created successfully",200,True)
        except Exception as e:
            return json.Response({"data":[e]},"Internal Server Error", 400,False)
        
    def put(self,request):
        try:
            data = request.data 
            print(data['id'])
            userobj = account_models.User.objects.filter(id=data['id']).last()
            print(userobj)
            user_data = EmployeeSerializer(userobj,data=data)
            if user_data.is_valid(raise_exception=True):    
                user_data.save()
            v=self.write(dict(error=str(e)))
            return json.Response([v],"User Updated successfully",200,True)
        except Exception as e:
            return json.Response({"data":[e]},"Internal Server Error", 400,False)

    def put(self, request):
        # id_=request.query_params.get('id')
        datas = j.loads(request.body.decode('utf-8'))
        Users_data = account_models.User.objects
        user_exists = Users_data.filter(id=datas["id"]).exists()
        print(user_exists)
        if user_exists:
            print("Existing user")
            Users_data.filter(id=datas["id"]).update(firstname=datas["firstname"],
                            lastname=datas["lastname"],
                            phone_number=datas['phone_number'],
                            email=datas['email'],
                            is_active=True,
                            is_email_verified=True,
                            is_phone_verified=False,
                            roles_id=datas["roles"],
                            city=datas["city"],
                            state=datas["state"],
                            country=datas["country"],
                            address1=datas["address1"],
                            address2=datas["address2"],
                            image=datas["image"],
                            pincode=datas["pincode"])
        

            user_Name_id = account_models.User.objects.filter(email=datas['email']).first()
            return json.Response({"data":user_Name_id.id},"User updated successfully",201,True)
        return json.Response({"data":[]},"User not existed",400,False)
        

