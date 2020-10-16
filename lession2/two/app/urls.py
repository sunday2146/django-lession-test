#coding:utf-8

from django.urls import path
from .views import Index

urlpatterns = [
    path('<str:name>/<int:age>', Index.as_view(), name='index')
]