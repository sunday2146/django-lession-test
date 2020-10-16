# coding:utf-8

import time

from django.views.generic import View
from django.shortcuts import render, redirect, reverse

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login
# from django.http import HttpResponse

from .models import Message
from .consts import MessageType
from .forms import MessageForm, RegisterForm, LoginForm


class Register(View):
    TEMPLATE = 'register.html'

    def get(self, request):
        data = {}
        return render(request, self.TEMPLATE, data)

    def post(self, request):
        data = {}
        form = RegisterForm(request.POST)
        data['error'] = form.non_field_errors

        if not form.is_valid():
            return render(request, self.TEMPLATE, data)

        return redirect(reverse('five'))


class LoginView(View):
    TEMPLATE = 'login.html'

    def get(self, request):

        if request.user.is_authenticated:
            return redirect(reverse('five'))

        data = {}
        next_return = request.GET.get('next', '')
        data['next'] = next_return
        return render(request, self.TEMPLATE, data)

    def post(self, request):
        data = {}
        form = LoginForm(request.POST)
        print('1')
        if not form.is_valid():
            print('test 1.1', form.non_field_errors)
            data['error'] = form.non_field_errors
            return render(request, self.TEMPLATE, data)
        print('2')
        user = form.cleaned_data.get('user')
        if user:
            login(request, user)
        print('3')
        next_return = request.POST.get('next_return')
        print('test1', next_return)
        if next_return:
            print('test2', 1)
            return redirect(next_return)
        print('test3', '2')
        return redirect(reverse('five'))




class LessionThree(View):

    TEMPLATE = 'three.html'

    def get(self, request, message_type):
        data = {}

        try:
            message_type_obj = MessageType[message_type]
        except Exception as e:
            data['error'] = '没有这个消息类型 {}'.format(e)
            return render(request, self.TEMPLATE, data)

        message = request.GET.get('message', '')

        if not message:
            data['error'] = '消息不可为空'
            return render(request, self.TEMPLATE, data)

        data['message'] = message
        data['message_type'] = message_type_obj

        return render(request, self.TEMPLATE, data)


class LessionFourPageOne(View):
    TEMPLATE = 'four_page_one.html'

    def get(self, request, message_type):

        data = {}

        try:
            message_type_obj = MessageType[message_type]
        except Exception as e:
            data['error'] = '没有这个消息类型 {}'.format(e)
            return render(request, self.TEMPLATE, data)

        message = request.GET.get('message', '')

        if not message:
            data['error'] = '消息不可为空'
            return render(request, self.TEMPLATE, data)

        Message.objects.create(
            content=message,
            message_type=message_type_obj.value,
            created_time=time.time()
        )

        return redirect(reverse('fourpagetwo'))


class LessionFourPageTwo(View):

    TEMPLATE = 'four_page_two.html'

    @method_decorator(permission_required('app.view_message'))
    def get(self, request):

        data = {}

        search = request.GET.get('search', '')

        if search:
            messages = Message.objects.filter(content__contains=search)
        else:
            messages = Message.objects.all()

        data['messages'] = messages

        return render(request, self.TEMPLATE, data)


class LessionFive(View):

    TEMPLATE = 'five.html'

    @method_decorator(login_required)
    def get(self, request):

        data = {}
        data['form'] = MessageForm()

        return render(request, self.TEMPLATE, data)

    def post(self, request):

        form = MessageForm(request.POST)

        if not form.is_valid():
            return render(request, self.TEMPLATE, {'form': form})

        content = form.cleaned_data.get('content')
        message_type = form.cleaned_data.get('message_type')

        Message.objects.create(
            content=content,
            message_type=message_type.value,
            created_time=time.time()
        )

        return redirect(reverse('fourpagetwo'))
