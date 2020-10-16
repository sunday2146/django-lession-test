# coding:utf-8

from django.db import models


class Apage(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        permissions = [
            ('look_a_page', 'can get this a page message')
        ]


class Bpage(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        permissions = [
            ('look_b_page', 'can get this a page message')
        ]
