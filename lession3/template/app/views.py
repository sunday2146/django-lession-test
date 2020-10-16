#coding:utf-8

import datetime

from django.shortcuts import render
from django.views.generic import View


class Index(View):
    TEMPLATE = 'index.html'

    def get(self, request, name):

        data = {}
        data['name'] = name
        data['array'] = range(10)
        data['count'] = 20
        data['time'] = datetime.datetime.now()
        data['cut_str'] = 'hello-boy!'
        data['first_big'] = '你好 django! haha'
        data['result'] = False
        data['dic_list'] = [{'name': 'dewei', 'age': 30},{'name': 'xiaoming', 'age': 18}]
        data['float_num'] = 3.1415926
        data['html_str'] = '<div style="background-color:red;width:50px;height:50px"></div>'
        data['a_str'] = '请看 www.baidu.com'
        data['feature'] = data['time'] + datetime.timedelta(days=5)
        #return render(request, self.TEMPLATE, data)
        return ''


class Jinja(View):
    TEMPLATE = 'jinja2.html'

    def get(self, request):
        data = {'name': 'dewei', 'count': 10}
        return render(request, self.TEMPLATE, data)
