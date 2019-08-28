from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

from df_user import user_decorator
from .models import CartInfo

@user_decorator.login
def cart(request):
    user_id = request.session.get('user_id')
    carts = CartInfo.objects.filter(user_id=int(user_id))
    # print(cart)
    context = {
        'title': '购物车',
        'page_name': 1,
        'carts': carts,
    }
    if request.is_ajax():
        count = carts.count()
        return JsonResponse({'count': count})
    else:
        return render(request, 'df_cart/cart.html', context=context)

@user_decorator.login
def add(request, goods_id, count):
    user_id = request.session.get('user_id')
    cart = CartInfo.objects.filter(user_id=int(user_id), goods_id=int(goods_id)).first()
    # 如果已存在数据则count相加，否则创建
    # print(cart)
    if cart:
        # print(count)
        cart.count = cart.count + int(count)
    else:
        cart = CartInfo()
        cart.user_id = int(user_id)
        cart.goods_id = int(goods_id)
        cart.count = count
    cart.save()

    if request.is_ajax():
        count = CartInfo.objects.filter(user_id=int(user_id)).count()
        context = {
            'count':count,
        }
        return JsonResponse(context)
    else:
        return redirect('df_cart:cart')