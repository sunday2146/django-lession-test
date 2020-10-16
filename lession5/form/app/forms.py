# coding:utf-8


from django import forms
from django.forms import fields
from .models import Auth as AuthModel


class AuthModelForm(forms.ModelForm):

    class Meta:
        model = AuthModel

        fields = ['username', 'password']  # '__all__'
        exclude = []  # 输入不专程表单字段的model字段

        field_classes = {  # 定义字段的类型，一般会按照model的类型自动转换
            'username': forms.CharField,
            'password': forms.CharField
        }

        labels = {
            'username': '用户名',
            'password': '密码'
        }

        widgets = {
            'username': forms.TextInput(
                attrs={'placeholder': '请输入用户名'}
            ),
            'password': forms.PasswordInput(
                attrs={'placeholder': '请输入密码'},
                render_value=True
            )
        }

        error_messages = {
            'username': {'required': '用户名不可以为空'},
            'password': {'min_length': '最爱哦不能低于10个字符'}
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if len(username) > 10:
            raise forms.ValidationError('用户名最大不可超过10')

        return username



class Auth(forms.Form):
    username = fields.CharField(
        max_length=18,
        min_length=3,
        required=True,
        label="用户名",
        widget=forms.TextInput(attrs={'placeholder': '最大不可超过18字符'})
    )
    password = fields.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '请输入密码'}),
        label="密码",
        required=True,
        min_length=10,
        error_messages={'min_length': '最小不能低于10个字符'}
    )

    def clean(self):
        username = self.cleaned_data.get('username', '')
        password = self.cleaned_data.get('password', '')
        print('111')
        if not username:
            raise forms.ValidationError('用户名不可以为空！')

        if len(username) > 10:
            print('222')
            raise forms.ValidationError('用户名最大不能超过10')

        if not password:
            raise forms.ValidationError('密码不可以为空！')


    def clean_username(self):
        username = self.cleaned_data.get('username', '')

        if len(username) > 18:
            raise forms.ValidationError('用户名不能超过18')
        return username
