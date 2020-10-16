#coding:utf-8

import json

from functools import wraps
from django.db import models
from django_redis import get_redis_connection


_cache = get_redis_connection('default')


def cache(func):
  @wraps(func)
  def wrapper(obj, *args):
    key = args[0]
    value = _cache.get(key)
    if value:
      return json.loads(value)
    rs = func(obj, *args)
    _cache.set(key, json.dumps(rs))
    return rs
  return wrapper
 


class Test(models.Model):
  name = models.IntegerField()
  

class User(models.Model):
  username = models.CharField(unique=True, max_length=50, blank=False)
  age = models.SmallIntegerField(default=0)
  phone = models.IntegerField(db_index=True, blank=True, default=0)
  email = models.EmailField(blank=True, default='')
  info = models.TextField()
  create_time = models.DateTimeField(auto_now_add=True)
  update_time = models.DateTimeField(auto_now=True)

  class Meta:
    index_together = ['username', 'phone']

  def __str__(self):
    return 'user:{}'.format(self.username)

  @classmethod
  @cache
  def get(cls, id):
    rs = cls.objects.get(id=id)
    return {
      'id': rs.id,
      'username': rs.username,
      'age': rs.age,
      'email': rs.email,
      'info': rs.info,
      'create_time': str(rs.create_time),
      'update_time': str(rs.update_time)
    }


class Userprofile(models.Model):
  user = models.OneToOneField(User, blank=True, null=True, on_delete=models.SET_NULL)
  birthday = models.CharField(max_length=100, blank=True, default='')

  def __str__(self):
    return 'user:{}, birthday:{}'.format(self.user.username, self.birthday)


class Diary(models.Model):
  user = models.ForeignKey(User, related_name='diary', on_delete=models.SET_NULL, blank=True, null=True)
  content = models.TextField()
  create_time = models.IntegerField()


class Group(models.Model):
  user = models.ManyToManyField(User, related_name='group')
  name = models.CharField(max_length=20)
  create_time = models.IntegerField()



