from django.shortcuts import render
from allauth.account.views import LoginView, SignupView



class LogIn(LoginView):
    template_name = 'authentication/login.html'



class SignUp(SignupView):
    template_name = 'authentication/signup.html'