from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from users import views

app_name = 'users'

urlpatterns = [
  path('login', views.login_view, name='login'),
  path('registration', views.registration_view, name='registration'),
  path('dashboard', views.dashboard_view, name='dashboard')
]