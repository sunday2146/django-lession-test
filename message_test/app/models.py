# coding:utf-8

import time

from django.contrib.auth.models import User
from django.db import models
from .consts import MessageType


class Message(models.Model):
    user = models.ForeignKey(
        User, null=True,
        default='',
        on_delete=models.SET_NULL,
        related_name='message'
    )
    content = models.TextField()
    message_type = models.CharField(max_length=10, db_index=True)
    created_time = models.IntegerField(default=0)

    def __str__(self):
        return 'type:{},content:{}'.format(self.message_type, self.content)

    @property
    def message_typ(self):
        try:
            return MessageType[self.message_type]
        except:
            return MessageType.info

    def times(self):
        _time = time.localtime(self.created_time)
        return time.strftime('%Y-%m-%d %H:%M:%s', _time)
