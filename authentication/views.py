from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

def email_confirm_redirect(request, key):
    return HttpResponseRedirect(f"{settings.BASE_EMAIL_VERIFY_URL}/{key}")

def password_reset_confirm_redirect(request, userId, token):
    return HttpResponseRedirect(f"{settings.BASE_PASSWORD_RESET_URL}{userId}/{token}/")