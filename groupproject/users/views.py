from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect


def login_view(request):
  if request.method == 'POST':
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
      return redirect('users:dashboard')
  else:
    form = AuthenticationForm()
  context = {'form': form}
  return render(request, "users/login.html", context)


def registration_view(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('users:dashboard')
  else:
    form = UserCreationForm()
  context = {'form': form}
  return render(request, 'users/registration.html', context)


def logout_view(request):
    logout(request)


def dashboard_view(request):
  dashboard_template = "users/dashboard.html"
  context = {}
  return render(request, dashboard_template, context)
