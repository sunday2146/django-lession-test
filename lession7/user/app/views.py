# coding:utf-8

from django.contrib.auth.models import User, Permission
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from django.http import Http404


class Regist(View):
    TEMPLATE = 'regist.html'

    def get(self, request):

        if request.user.is_authenticated:
            return redirect(reverse('login'))

        error = request.GET.get('error', '')

        return render(request, self.TEMPLATE, {'error': error})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        check_password = request.POST.get('check_password')

        if password != check_password:
            return redirect('/regist?error=密码不相同')

        exists = User.objects.filter(username=username).exists()
        if exists:
            return redirect('/regist?error=该用户已存在')

        user = User.objects.create_user(
            username=username,
            password=password
        )
        user.save()
        return redirect(reverse('login'))


class Login(View):
    TEMPLATE = 'login.html'

    def get(self, request):
        error = request.GET.get('error', '')

        return render(request, self.TEMPLATE, {'error': error})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        exists = User.objects.filter(username=username).exists()

        if not exists:
            return redirect('/login?error=没有该用户')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
        else:
            return redirect('/login?error=密码错误')

        return redirect('/login')


class LogoutUser(View):

    def get(self, request):

        logout(request)

        return redirect(reverse('login'))


class A(View):

    TEMPLATE = 'a.html'

    def get(self, request):

        if not request.user.is_authenticated:
            return redirect('/login')

        if not request.user.has_perm('app.look_a_page'):
            raise Http404()

        return render(request, self.TEMPLATE)

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required



class B(View):
    TEMPLATE = 'b.page.html'

    @method_decorator(login_required)
    @method_decorator(permission_required('app.look_b_page'))
    def get(self, request):

        b_permission = Permission.objects.filter(codename='look_b_page').first()

        users = User.objects.filter(Q(groups__permissions=b_permission)|Q(user_permissions=b_permission)).distinct()
        if request.user not in users:
            raise Http404()

        return render(request, self.TEMPLATE)
