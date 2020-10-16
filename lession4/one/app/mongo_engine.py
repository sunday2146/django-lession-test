#coding:utf-8

from mongoengine import connect, Document, StringField, IntField, ReferenceField

db = connect('test_mongo', host='localhost', port=27017)


class Users(Document):
    name = StringField(required=True, max_length=200)
    age = IntField(required=True)


class Paper(Document):
    title = StringField(required=True, max_length=200)
    user = ReferenceField(Users)

