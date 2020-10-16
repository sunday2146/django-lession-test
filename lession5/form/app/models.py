# coding:utf-8

from django.db import models


class Auth(models.Model):
    username = models.CharField(max_length=18)
    password = models.CharField(max_length=18)

    def __str__(self):
        return 'username:{}'.format(self.username)
