# -*- coding:UTF-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.fields import AutoField, CharField, \
    DecimalField, TextField, BooleanField, TimeField, IntegerField

'''
    用户类型表:
    
'''
# Table UserType
class UserType(models.Model):
    id = AutoField(primary_key=True)
    type_name = CharField(max_length=30)
    description = CharField(max_length=300)
    
'''
    用户表:
    字段:
    id:
    type:用户类型{管理员,房东,租客}
    
'''
# Table User
class User(models.Model):
    '用户表 - 所有系统使用者'
    #字段-start
    id = AutoField(primary_key=True)
    type_id = IntegerField()
    user_name = CharField(max_length=15)
    head_pic = CharField(max_length=100)
    phone = CharField(max_length=50, unique=True)
    is_left = BooleanField()
    #字段-end

# Table CostType
class CostType(models.Model):
    id = AutoField(primary_key=True)
    type_name = CharField(max_length=30)
    unit = CharField(max_length=50)
    rate = DecimalField(max_digits=7, decimal_places=2)
    description = TextField()
    
#Table Cost
class Cost(models.Model):
    id = AutoField(primary_key=True)
    type_id = IntegerField()
    cost_num = DecimalField(max_digits=8, decimal_places=2)
    start = TimeField(auto_now_add=True)
    end = TimeField()
    
    
    
    
