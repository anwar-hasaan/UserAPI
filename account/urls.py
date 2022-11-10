from django.urls import path
from .views import (UserRegistrationView, UserLoginView, 
                    UserProfileView, UserChangePasswordView,
                    SendPasswordResetEmailView, UserPasswordResetView, )

urlpatterns = [
    path('register', UserRegistrationView.as_view(), name='registration'),
    path('login', UserLoginView.as_view(), name='login'),
    path('profile', UserProfileView.as_view(), name='profile'),
    path('changepassword', UserChangePasswordView.as_view(), name='changepassword'), # when user logged in and eant to change pass
    path('send-password-reset-email', SendPasswordResetEmailView.as_view()), # when user forgot password
    path('reset-password/<uid>/<token>', UserPasswordResetView.as_view(), name='resetpassword'),
]