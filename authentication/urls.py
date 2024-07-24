from django.urls import path

from . import views
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.registration.views import LoginView, VerifyEmailView, ResendEmailVerificationView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='rest_register'),
    path('login/', LoginView.as_view(), name='rest_login'),
    path('verify-email/', VerifyEmailView.as_view(), name='rest_verify_email'),
    path('resend-email/', ResendEmailVerificationView.as_view(), name="rest_resend_email"),
    path('account-confirm-email/<str:key>/', views.email_confirm_redirect, name="account_confirm_email"),
    path('account-confirm-email-sent/', VerifyEmailView.as_view(), name="account_email_verification_sent"),
]
