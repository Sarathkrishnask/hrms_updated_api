from rest_framework import permissions
from django.contrib import auth

class ISSuperAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return str(request.user.roles) in ['SuperAdmin']

class ISEmployee(permissions.BasePermission):
    def has_permission(self, request, view):
        return str(request.user.roles) not in ["SuperAdmin"]
    
class ISSuperAdminOrEmployee(permissions.BasePermission):
    def has_permission(self, request, view):
        return str(request.user.roles) in ["SuperAdmin"] or str(request.user.roles) not in ["SuperAdmin"]

    
