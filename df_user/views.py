from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
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
        'user_name':user_name,
    }
    # 转到登录页面
    return render(request, 'df_user/login.html', context=context)

def register_exist(request):
    # 判断数据库中是否已存在该用户名
    user_name = request.GET.get('user_name')
    count = UserInfo.objects.filter(uname=user_name).count()
    return JsonResponse({'count':count})

def login(request):
    user_name = request.COOKIES.get('user_name', '')
    context = {
        'title':'用户登录',
        'user_name': user_name,
        'error_name': 0,
        'error_pwd':0,
    }
    return render(request, 'df_user/login.html', context=context)

def login_handle(request):
    # 获取登录信息
    post = request.POST
    user_name = post.get('user_name','')
    pwd = post.get('pwd')
    jizhu = post.get('jizhu', 0)
    # print(user_name, pwd, jizhu)
    # 从数据库获取用户信息
    users = UserInfo.objects.filter(uname=user_name)
    # 判断用户名是否正确
    if len(users) == 1:
        # 加密密码
        sha1 = hashlib.sha1()
        sha1.update(pwd.encode('utf-8'))
        encrypted_pwd = sha1.hexdigest()
        # 判断密码是否相同
        if encrypted_pwd == users[0].upwd:
            url = request.COOKIES.get('url', '/')
            # 跳转到登录之前的链接或者首页
            red = HttpResponseRedirect(url)
            # 判断是否要记住用户名
            if jizhu:
                red.set_cookie('user_name', user_name)
            else:
                red.set_cookie('user_name', '', max_age=-1)
            request.session['user_id'] = users[0].id
            request.session['user_name'] = user_name
            return red

        # 密码错误
        else:
            context = {
            'title':'用户登录',
            'user_name':user_name,
            'pwd':pwd,
            'error_name':0,
            'error_pwd':1,
            }
            return render(request, 'df_user/login.html', context=context)

    # 用户名错误
    else:
        context = {
        'title':'用户登录',
        'user_name':user_name,
        'pwd':pwd,
        'error_name':1,
        'error_pwd':0,
        }
        return render(request, 'df_user/login.html', context=context)

def logout(request):
    request.session.flush()
    return redirect('df_user:login')

def info(request):

    return render(request, 'df_user/user_center_info.html')