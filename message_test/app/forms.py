# coding:utf-8

import jieba

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .consts import MessageType, SensitiveWordInit


MESSAGE_TYPE_CHOICES = tuple(
    [(message.value, message.value) for message in MessageType])


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if not username or not password:
            raise forms.ValidationError('用户名，密码不可为空')

        exists = User.objects.filter(username=username).exists()

        if not exists:
            raise forms.ValidationError('该用户不存在')

        user = authenticate(username=username, password=password)

        if not user:
            raise forms.ValidationError('密码错误')

        self.cleaned_data['user'] = user
        return self.cleaned_data


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    check_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):

        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        check_password = self.cleaned_data.get('check_password')

        if not username:
            raise forms.ValidationError('缺少用户名')

        if not password or not check_password:
            raise forms.ValidationError('缺少密码')

        if password != check_password:
            raise forms.ValidationError('两次密码不一致')
        exists = User.objects.filter(username=username).exists()

        if exists:
            raise forms.ValidationError('该用户已存在:{}'.format(username))
        user = User.objects.create_user(username=username, password=password)
        user.save()

        return self.cleaned_data



class MessageForm(forms.Form):
    content = forms.CharField(label='消息内容', max_length=100, required=True)
    message_type = forms.CharField(
        label='数据类型',
        max_length=10,
        widget=forms.Select(choices=MESSAGE_TYPE_CHOICES)
    )

    def clean_message_type(self):
        message_type = self.cleaned_data.get('message_type')

        if not message_type:
            raise forms.ValidationError('消息类型不能为空!')

        try:
            message_type_obj = MessageType[message_type]
        except:
            raise forms.ValidationError('无效的消息类型')

        return message_type_obj

    def clean_message(self):

        content = self.cleaned_data.get('content')

        if not content:
            raise forms.ValidationError('消息不能为空')

        cut_message = jieba.lcut(content)

        check = list(set(cut_message) & set(SensitiveWordInit))

        if check:
            raise forms.ValidationError('该消息涉及违禁词汇，已被屏蔽')

        return content
