# coding:utf-8

from django.contrib import admin
from django.utils.html import format_html
from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'message_type', 'created_time', 'return_href']
    # readonly_fields = ('message_type', 'created_time')

    list_filter = ('message_type', )
    search_fields = ['content']
    ordering = ['-id']
    list_per_page = 5

    def save_model(self, request, obj, form, change):

        if change:
            obj.content = obj.content + ' update'
        else:
            obj.content = obj.content + ' create'

        super(MessageAdmin, self).save_model(request, obj, form, change)

    def return_href(self, obj):
        return format_html('<a href="{}">跳转', 'http://www.baidu.com')
