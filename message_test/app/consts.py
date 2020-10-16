# coding:utf-8

from enum import Enum


class MessageType(Enum):
    info = 'info'
    warning = 'warning'
    error = 'error'
    danger = 'danger'

MessageType.info.label = '信息'
MessageType.warning.label = '警告'
MessageType.error.label = '错误'
MessageType.danger.label = '危险'

MessageType.info.color = 'green'
MessageType.warning.color = 'orange'
MessageType.error.color = 'gray'
MessageType.danger.color = 'red'

SensitiveWord = ['天气', '坏人', '不开心']
SensitiveWordInit = ['专业', '生活']
