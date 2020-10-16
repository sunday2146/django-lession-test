# coding:utf-8

from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from .forms import Auth, AuthModelForm
from .models import Auth as AuthModel


class Regist(View):
    TEMPLATE = 'regist.html'

    def get(self, request):

        user = AuthModel.objects.filter(pk=1).first()

        if user:
            form = AuthModelForm(instance=user)
        else:
            form = AuthModelForm()

        return render(request, self.TEMPLATE, {'form': form})

    def post(self, request):
        # username = request.POST.get('username')
        # password = request.POST.get('password')

        form = AuthModelForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            form.save()
        else:
            return render(request, self.TEMPLATE, {'form': form})

        return redirect(reverse('regist'))

