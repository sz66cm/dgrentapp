# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.db.models.fields import AutoField, CharField, IntegerField,\
    BooleanField, DecimalField, TimeField
import django.utils.timezone as timezone

# Table Building
class Building(models.Model):
    '建筑模块 - 大厦,楼宇等'
    id = AutoField(primary_key=True)
    name = CharField(max_length=150)
    total_storey = IntegerField()
    address = CharField(max_length=300)
    postcode = IntegerField()

# Table Flatlet    
class Flatlet(models.Model):
    '套房模块 - 单间,两房一厅'
    id = AutoField(primary_key=True)
    building_id = IntegerField()
    room_id = CharField(max_length=60)
    cost_type_id = IntegerField()
    is_idle = BooleanField(default=True)
    
#Table ResourceMeters
class ResourceMeters(models.Model):
    '资源模块 - 水电煤网络等资源'
    id = AutoField(primary_key=True)
    flatlet_id = IntegerField()
    res_name = CharField(max_length=30)
    unit = CharField(max_length=30)
    meters = DecimalField(max_digits=8, decimal_places=2)
    data_time = TimeField(default=timezone.now)
    
    
    
        

    
