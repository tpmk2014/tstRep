from django.contrib.auth import get_user_model
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect

from pages.forms import ContactForm
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

  return render(request, staticpage_template, context)


def success_view(request):
  context = {}
  template = "pages/success.html"
  return render(request, template, context)


def contact_view(request):
    if request.method == 'GET':
      form = ContactForm()
    else:
      form = ContactForm(request.POST)
      if form.is_valid():
        subject = form.cleaned_data['subject']
        from_email = form.cleaned_data['from_email']
        message = form.cleaned_data['message']
        try:
          send_mail(subject, message, from_email, ['informatykasan2018@gmail.com'])
        except BadHeaderError:
          return HttpResponse('Invalid header found.')
        return redirect('/success')
    context = {'form': form}
    return render(request, "pages/contact.html", context)


