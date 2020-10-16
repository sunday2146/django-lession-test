# coding:utf-8

from django.urls import path
from .views import Regist


urlpatterns = [
  path('regist', Regist.as_view(), name='regist')
]
