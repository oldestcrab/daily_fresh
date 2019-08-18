from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from .models import UserInfo

import hashlib

# Create your views here.
def register(request):
    # 注册视图
    context = {
        'title':'注册',
    }
    return render(request, 'df_user/register.html', context=context)

def register_handle(request):
    # 处理注册信息
    # 获取注册信息
    post = request.POST
    user_name = post.get('user_name')
    pwd = post.get('pwd')
    cpwd = post.get('cpwd')
    uemail = post.get('email')

    # 两次输入的密码不一致回到注册页面
    if pwd != cpwd:
        return redirect('df_user:register')
    # 对密码进行sha1加密
    sha1 = hashlib.sha1()
    sha1.update(pwd.encode('utf-8'))
    encrypted_pwd = sha1.hexdigest()

    # 创建对象
    UserInfo.objects.create(
        uname = user_name,
        upwd = encrypted_pwd,
        uemail = uemail,
    )

    context = {
        'title':'用户登录',
    }
    # 转到登录页面
    return render(request, 'df_user/login.html', context=context)

def register_exist(request):
    # 判断数据库中是否已存在该用户名
    user_name = request.GET.get('user_name')
    count = UserInfo.objects.filter(uname=user_name).count()
    return JsonResponse({'count':count})

def login(request):
    context = {
        'title':'用户登录',
    }
    return render(request, 'df_user/login.html', context=context)

def login_handle(request):
    # 获取登录信息
    post = request.POST
    user_name = post.get('user_name')
    pwd = post.get('pwd')
    print(user_name, pwd)
    # 判断用户名是否正确
    uname = UserInfo.objects.filter(uname=user_name)
    # 加密密码
    sha1 = hashlib.sha1()
    sha1.update(pwd.encode('utf-8'))
    encrypted_pwd = sha1.hexdigest()
    context = {
        'title':'用户登录',
    }
    return render(request, 'df_user/login.html', context=context)