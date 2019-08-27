from django.shortcuts import render, HttpResponse

from df_user import user_decorator
from .models import CartInfo

@user_decorator.login
def add(request, goods_id, count):
    user_id = request.session.get('user_id')
    cart = CartInfo.objects.filter(user_id=int(user_id), goods_id=int(goods_id)).first()
    # 如果已存在数据则count相加，否则创建
    if cart:
        cart.count = cart.count + int(count)
    else:
        cart = CartInfo()
        cart.user_id = int(user_id)
        cart.goods_id = int(goods_id)
        cart.count = count
    cart.save()
    context = {
        'title': '购物车',
        'page_name': 1,
        'cart': cart,
    }
    return render(request, 'df_cart/add.html', context=context)