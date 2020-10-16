# coding:utf-8

import jieba

from django import template
from app.consts import SensitiveWord


register = template.Library()


@register.filter(name='deep_check_message')
def deep_check(value):
    cut_message = jieba.lcut(value)

    new_message = []

    for m in cut_message:
        if m in SensitiveWord:
            new_message.append('*')
        else:
            new_message.append(m)

    if new_message:
        return ''.join(new_message)
    return value


@register.filter
def sample_check(value):
    cut_message = jieba.lcut(value)
    print(cut_message)
    print(SensitiveWord)

    check = list(set(cut_message) & set(SensitiveWord))

    if len(check) != 0:
        return '该消息涉及违禁词汇，已被屏蔽'
    return value


@register.filter
def add_message_year(value, year):
    return '{} {}'.format(value, year)
