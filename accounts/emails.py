from django.core.mail import send_mail
import random
from django.conf import settings
from accounts.models import User


def send_otp_via_email(email):
    subject = f'Your account verification email'
    otp = random.randint(1000, 9999)
    message = f'Your otp is {otp}'
    from_email = settings.EMAIL_HOST
    send_mail(subject, message, from_email, [email])
    user_obj = User.objects.get(email=email)
    user_obj.otp = otp
    user_obj.save()
    print("отправлено")