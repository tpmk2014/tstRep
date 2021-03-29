from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect

def login_view(request):
  pass


def registration_view(request):
 pass

def logout_view(request):
    logout(request)
