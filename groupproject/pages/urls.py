from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from groupproject import settings
from pages import views

app_name = 'pages'

urlpatterns = [
    path('', views.index, name='home'),
    path('terms_of_service', views.staticpage, name='terms_of_service'),
    path('contact', views.get_FAQ_question, name='contact'),

]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)