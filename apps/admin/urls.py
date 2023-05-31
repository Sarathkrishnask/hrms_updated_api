from django.urls import path
from apps.admin import views

app_name = 'admin'

urlpatterns = [
    # path('userlist/',views.UserListApiView.as_view(),name='UserListApiView'),
    # path('userdetails/',views.UserDetailApiView.as_view(), name='userdetails'),
    path('manage_role/',views.RoleMaster.as_view(),name='RoleMaster'),
    path('manage_user/',views.RoleMaster.as_view(),name='RoleMaster'),
    path("add_emp/",views.ManageEmployee.as_view(),name="ManageEmployee")
]