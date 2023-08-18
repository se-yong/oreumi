from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('create', views.article_create, name='article_create'),
]
