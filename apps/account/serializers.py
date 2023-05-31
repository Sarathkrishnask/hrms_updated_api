from django.contrib.auth import get_user_model
from rest_framework import serializers
from apps import account
from apps.account.models import *

User = get_user_model()


"""
Maintain roles using serializers
"""
class RoleMasterSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = RoleMaster
        fields = '__all__'


class setPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def update(self, instance,data):
        instance.set_password(data.get('password'))
        instance.save()
        instance.refresh_from_db()
        return instance
    
# class EmployeeSerializer(serializers.ModelSerializer):

#     class Meta(object):
#         model = User
#         extra_kwargs = {'password': {'write_only': True, 'required': True}}
        
#     def __init__(self, *args, **kwargs):
#         super(EmployeeSerializer, self).__init__(*args, **kwargs)
#         self.Meta.exclude = ['updated_at','is_staff']


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        
    def __init__(self, *args, **kwargs):
        super(EmployeeSerializer, self).__init__(*args, **kwargs)
        self.Meta.exclude = ['updated_at','is_staff']
