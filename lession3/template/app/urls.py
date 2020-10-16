#coding:utf-8

from django.urls import path
from .views import Index, Jinja

urlpatterns = [
    path('jinja2', Jinja.as_view(), name='jinja'),
    path('index/<str:name>', Index.as_view(), name='index')
]