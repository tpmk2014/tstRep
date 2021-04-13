from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from groupproject import settings
from pages import views

app_name = 'pages'

urlpatterns = [
    path('', views.index, name='home'),
    path('terms_of_service', views.staticpage, name='terms_of_service'),
    path('about_us', views.staticpage, name='about_us'),
    path('contact', views.contact_view, name='contact'),
    path('pricing', views.staticpage, name='pricing'),
    path('success', views.success_view, name='success'),
]
