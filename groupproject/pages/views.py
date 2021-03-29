from django.shortcuts import render



def index(request):
  context = {}
  return render(request, 'pages/index.html', context)


def staticpage(request):
  context = {}
  if request.path == '/terms_of_service':
    staticpage_template = 'pages/terms_of_service.html'
  if request.path == '/about_us':
    staticpage_template = 'pages/about_us.html'

  return render(request, staticpage_template, context)
