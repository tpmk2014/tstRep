from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def login_view(request):
  if request.method == 'POST':
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
      user = form.get_user()
      login(request, user)
      return redirect('users:dashboard')
  else:
    form = AuthenticationForm()
  context = {'form': form}
  return render(request, "users/login.html", context)


def registration_view(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('users:dashboard')
  else:
    form = UserCreationForm()
  context = {'form': form}
  return render(request, 'users/registration.html', context)


def logout_view(request):
  logout(request)
  return redirect('pages:home')


@login_required
def dashboard_view(request):
  dashboard_template = "users/dashboard.html"
  context = {}
  return render(request, dashboard_template, context)


def bmi_calculator_view(request):
  context = {}
  template = "users/bmi_calculator.html"
  return render(request, template, context)


def articles_view(request):
  context = {}
  template = "users/articles.html"
  return render(request, template, context)


def my_calories_view(request):
  context = {}
  template = "users/user_calories.html"
  return render(request, template, context)
