#-*- coding:utf-8 -*-
'''
Created on 2016年8月9日

@author: cm
'''
from django.core.context_processors import csrf
from django.shortcuts import render

from UserApp.models import UserType, User
'''
    添加用户:
'''
def add_user(request):
    ctx = {}
    ctx.update(csrf(request))
    result = '';
    if request.POST:
        name = request.POST['name']
        type_id = int(request.POST['type_id'])
        head_pic = request.POST['head_pic']
        phone = request.POST['phone']
        if len(name)==0 or phone==0:
            ctx['result'] = '请完整名字与电话'
            return render(request,
                  "AddUser.html",
                  ctx)
        user = User(
                    user_name=name,
                    head_pic=head_pic,
                    phone=phone,
                    type_id=type_id,
                    is_left=False)
        try:
            user.save()
#             print str(user)
        except Exception, e:
            result = '过程出现异常'
            print "Exception : ", Exception, " e :", e
        else:
            result = '添加成功'
    else:
        result = '请检查请求类型'
    ctx['result'] = result
    return render(request,
                  "AddUser.html",
                  ctx)
'''
    添加用户类型:
'''
def add_user_type(request):
    ctx = {}
    ctx.update(csrf(request))
    if request.POST:
        type_name = request.POST['type_name']
        description = request.POST['description']
        user_type = UserType(type_name=type_name, description=description)
        #检查是否为空
        if len(type_name)==0:
            ctx['result'] = '类型名字不能为空'
        else:    
            try:
                user_type.save()
            except:
                ctx['result'] = '添加失败'
            else:
                ctx['result'] = '成功'
    else:
        ctx['result'] = '不是POST类型'
    return render(request, "AddUserType.html", ctx)

