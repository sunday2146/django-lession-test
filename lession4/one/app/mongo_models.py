#coding:utf-8

from django.conf import settings


conn = settings.MONGOCLIENT['test_mongo']



class User(object):

  db = conn['user']

  @classmethod
  def insert(cls, **params):
      return cls.db.insert(params)

  @classmethod
  def gets(cls, **params):
      return list(cls.db.find(params))

  @classmethod
  def get(cls, **params):
      return cls.db.find_one(params)

  @classmethod
  def update(cls, _id, **params):
      cls.db.update({'_id': _id}, {'$set': params})