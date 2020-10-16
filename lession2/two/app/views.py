#coding:utf-8

from django.views.generic import View
from django.http import HttpResponse


class Index(View):

    def get(self, request, name, age):

        print(dir(request))

        return HttpResponse('hello i am {0}, age is {1}'.format(name, age))

