from django.shortcuts import render



def index(request):
  context = {}
  render(request, 'pages/index.html', context)
