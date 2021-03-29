from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect

def login_view(request):
  if request.metod == 'POST':
    pass
  else:
    form = AuthenticationForm()
  context = {'form': form}
  return render(request, "users/login", context)

def registration_view(request):
  if request.metod == 'POST':
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
