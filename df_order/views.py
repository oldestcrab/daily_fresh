from django.shortcuts import render

from df_user import user_decorator
from df_user.models import UserInfo
from df_cart.models import CartInfo

@user_decorator.login
def order(request):
    user_id = request.session.get('user_id')
    user = UserInfo.objects.get(id=int(user_id))
    cart_ids = request.GET.getlist('cart_id')
    print(cart_ids)
    carts = []
    total_price = 0
    for goods_id in cart_ids:
        cart = CartInfo.objects.get(id=goods_id)
        carts.append(cart)
        total_price = total_price + float(cart.count) * float(cart.goods.gprice)
    total_price = float('%0.2f'%total_price)
    # 加上运费
    trans_cost = 10
    total_trans_price = total_price + 10
    context = {
        'title': '提交订单',
        'page_name': 1,
        'user': user,
        'carts': carts,
        'total_price': total_price,
        'trans_cost': trans_cost,
        'total_trans_price': total_trans_price,
    }
    return render(request, 'df_order/place_order.html', context=context)