from django.shortcuts import render, HttpResponse
from django.db import transaction
from django.http import JsonResponse

from datetime import datetime
from decimal import Decimal

from df_user import user_decorator
from df_user.models import UserInfo
from df_cart.models import CartInfo
from .models import OrderInfo, OrderDetailInfo

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

@user_decorator.login
def push(request):
    post = request.POST
    cart_ids = post.get('carts')
    total = post.get('total')
    user_id = request.session.get('user_id')
    tran_id = transaction.savepoint()
    data = {}
    try:
        user = UserInfo.objects.get(id=int(user_id))
        order = OrderInfo()
        now = datetime.now()
        order.user = int(user_id)
        order.odate = now
        order.ototal = Decimal(total)
        order.oid = ''
        order.oaddress = user.uaddress
        order.save()

        for cart_id in cart_ids.split(','):
            cart = CartInfo.objects.get(id=int(cart_id))
            order_detail = OrderDetailInfo()
            order_detail.order = order
            goods = cart.goods
            if cart.count <= goods.gkucun:
                goods.gkucun = goods.gkucun - cart.count
                goods.save()
                order_detail.goods = goods
                order_detail.count = cart.count
                order_detail.price = goods.gprice
                order_detail.save()
                cart.delete()
            else:
                return HttpResponse('库存不足')
                transaction.savepoint_rollback(tran_id)
        data['ok'] = 1
        transaction.savepoint_commit(tran_id)
    except Exception as e:
        print('订单提交失败')
        print(e.args)
        transaction.savepoint_rollback(tran_id)
    return JsonResponse(data)