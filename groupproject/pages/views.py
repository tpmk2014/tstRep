from django.contrib.auth import get_user_model
from django.shortcuts import render
from users.models import Trainer


def index(request):
  User = get_user_model()
  users = User.objects.all()
  trainers = Trainer.objects.all()
  context = {'users': users, 'trainers': trainers}
  return render(request, 'pages/index.html', context)


def staticpage(request):
  context = {}
  if request.path == '/terms_of_service':
    staticpage_template = 'pages/terms_of_service.html'
  elif request.path == '/about_us':
    staticpage_template = 'pages/about_us.html'
  elif request.path == '/contact':
    staticpage_template = 'pages/contact.html'
  elif request.path == '/pricing':
    staticpage_template = 'pages/pricing.html'

  return render(request, staticpage_template, context)
