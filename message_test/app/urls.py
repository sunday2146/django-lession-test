# coding:utf-8

from django.urls import path
from .views import (LessionThree, LessionFourPageOne,
                    LessionFourPageTwo, LessionFive, Register,
                    LoginView)


urlpatterns = [
    path('three/<str:message_type>', LessionThree.as_view(), name='three'),
    path('fourPageOne/<str:message_type>', LessionFourPageOne.as_view()),
    path('fourPageTwo', LessionFourPageTwo.as_view(), name='fourpagetwo'),
    path('five', LessionFive.as_view(), name='five'),
    path('register', Register.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login')
]
