from django.conf.urls import url, include
from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
	# main view
	path('', views.index, name='home'),
	path('o-nas', views.staticpage, name='about_us'),
	path('cennik', views.staticpage, name='pricing'),
	path('regulamin', views.staticpage, name='terms_of_service'),
	path('kontakt', views.staticpage, name='contact_us'),
	path('prywatnosc', views.staticpage, name='privacy'),
]
