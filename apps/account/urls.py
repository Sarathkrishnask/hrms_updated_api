from django.urls import path
from apps.account import views

app_name = 'account'

urlpatterns = [

    # path('registeruser/',views.UserRegister.as_view(),name='registeruser'),
    path('login/',views.loginApi.as_view(),name='email_login'),
    path('forget_account',views.ForgetAccount.as_view(),name='forget_account'),
    path('change_password',views.Changepassword.as_view(),name='change_password'),
    path('resend_otp',views.Resend_OTP.as_view(),name='resend_otp'),

]