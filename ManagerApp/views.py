#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from UserApp.models import UserType

def show_add_user_type_page(request):
    return render_to_response(
                              'AddUserType.html',
                              context_instance=RequestContext(request))

def show_add_user_page(request):
    ctx = {}
    user_type_list = UserType.objects.all();
    ctx['type_list'] = user_type_list
    return render_to_response(
                              'AddUser.html',
                              ctx,
                              RequestContext(request))
    