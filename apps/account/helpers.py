import random
import string
from apps.account.models import *
from django.core.mail import EmailMessage

def generate_random_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(8))
    return password

def generate_empids():
    event = User.objects.filter().last()    
    num = 1  
    if event:
        num = int(event.id) + 1                     
    eventid = "HUB_" + str(num)
    if User.objects.filter(emp_id=eventid).count() == 0:
        return eventid
    
def send_mail_toTemplate(subject,mail_body,to_mail,from_mail):
    try:
        email = EmailMessage(
            subject=subject,body=mail_body,to=[to_mail],from_email=from_mail
        )
        email.send()
        return True
    except Exception as ex:
        raise ex
    
def generate_otp():
    # Define possible characters for OTP
    digits = "123456789"
    # Initialize OTP variable
    otp = ""
    # Loop to generate 6 random digits
    for i in range(4):
        otp += random.choice(digits)
    # Return the OTP
    return otp
        
    