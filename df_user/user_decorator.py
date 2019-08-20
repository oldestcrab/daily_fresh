from django.shortcuts import reverse
from django.http import HttpResponseRedirect

# 如果未登陆则跳转到登录页面
def login(func):
    def login_fun(request, *args, **kwargs):
        if 'user_id' in request.session:
            return func(request, *args, **kwargs)
        else:
            red = HttpResponseRedirect(reverse('df_user:login'))
            red.set_cookie('url', request.get_full_path())
            # 登录之后跳转回之前的页面
            return red

    return login_fun