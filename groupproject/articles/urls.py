from django.urls import path
from django.conf.urls import include

from articles import views

app_name = "articles"
urlpatterns = [
    path('<str:article_section>/', views.article_view, name='article'),
]