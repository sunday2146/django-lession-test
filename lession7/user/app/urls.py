# coding:utf-8

from django.urls import path
from .views import Regist, Login, LogoutUser, A, B


urlpatterns = [
    path('regist', Regist.as_view(), name='regist'),
    path('login', Login.as_view(), name='login'),
    path('logout', LogoutUser.as_view(), name='logout'),
    path('a', A.as_view(), name='a_page'),
    path('b', B.as_view(), name='b_page')
]
