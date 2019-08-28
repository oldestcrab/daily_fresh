from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator
from datetime import datetime

from .models import TypeInfo, GoodsInfo
from df_user.models import GoodsBrowser
from df_cart.models import CartInfo

# Create your views here.
def index(request):
    typelist = TypeInfo.objects.all()
    # 按照上传顺序
    type0 = typelist[0].goodsinfo_set.order_by('-id')[0:4]
    # 按照点击量
    type01 = typelist[0].goodsinfo_set.order_by('-gclick')[0:4]
    type1 = typelist[1].goodsinfo_set.order_by('-id')[0:4]
    type11 = typelist[1].goodsinfo_set.order_by('-gclick')[0:4]
    type2 = typelist[2].goodsinfo_set.order_by('-id')[0:4]
    type21 = typelist[2].goodsinfo_set.order_by('-gclick')[0:4]
    type3 = typelist[3].goodsinfo_set.order_by('-id')[0:4]
    type31 = typelist[3].goodsinfo_set.order_by('-gclick')[0:4]
    type4 = typelist[4].goodsinfo_set.order_by('-id')[0:4]
    type41 = typelist[4].goodsinfo_set.order_by('-gclick')[0:4]
    type5 = typelist[5].goodsinfo_set.order_by('-id')[0:4]
    type51 = typelist[5].goodsinfo_set.order_by('-gclick')[0:4]

    context = {
        'title': '主页',
        'guest_cart': 1,
        'cart_num': cart_count(request),
        'type0': type0, 'type01': type01,
        'type1': type1, 'type11': type11,
        'type2': type2, 'type21': type21,
        'type3': type3, 'type31': type31,
        'type4': type4, 'type41': type41,
        'type5': type5, 'type51': type51,
    }
    return render(request, 'df_goods/index.html', context=context)

def detail(request, goods_id):
    goods = GoodsInfo.objects.filter(id=int(goods_id)).first()
    # 点击量+1
    goods.gclick = goods.gclick + 1
    goods.save()

    # 上新
    news = goods.gtype.goodsinfo_set.order_by('-id')[0:2]
    context = {
        'title': '商品详情',
        'guest_cart': 1,
        'cart_num': cart_count(request),
        'goods': goods,
        'id': goods_id,
        'news': news,
    }
    resposne = render(request, 'df_goods/detail.html', context=context)

    # 更新用户浏览记录，保持在5条
    if 'user_id' in request.session:
        user_id = request.session.get('user_id')
        try:
            browsed_good = GoodsBrowser.objects.get(user_id=int(user_id), good_id=int(goods_id))
        except:
            browsed_good = None
        if browsed_good:
            browsed_good.browser_time = datetime.now()
            browsed_good.save()
        else:
            GoodsBrowser.objects.create(user_id=int(user_id), good_id=int(goods_id))
            browsed_goods = GoodsBrowser.objects.filter(user_id=int(user_id))
            if browsed_goods.count() > 5:
                ordered_goods = browsed_goods.order_by('-browser_time')
                for _ in ordered_goods[5:]:
                    _.delete()

    return resposne

def goods_list(request, type_id, page_id, sort_id):
    typeinfo = TypeInfo.objects.get(id=int(type_id))
    # 上新
    news = typeinfo.goodsinfo_set.order_by('-id')[0:2]
    cart_num, guest_cart = 0, 0
    goods_list =[]

    user_id = request.session.get('user_id')
    if user_id:
        guest_cart = 1

    # 默认最新
    if sort_id == '1':
        goods_list = typeinfo.goodsinfo_set.order_by('-id')
    # 按照价格
    if sort_id == '2':
        goods_list = typeinfo.goodsinfo_set.order_by('-gprice')
    # 按照人气
    if sort_id == '3':
        goods_list = typeinfo.goodsinfo_set.order_by('-gprice')

    # 分页
    paginator = Paginator(goods_list, 4)
    # 返回page对象，包含商品信息
    page = paginator.page(int(page_id))
    context = {
        'title': '商品列表',
        'cart_num': cart_count(request),
        'guest_cart': guest_cart,
        'news': news,
        'sort_id': sort_id,
        'typeinfo': typeinfo,
        'page': page,
        'paginator': paginator,
    }
    return render(request, 'df_goods/list.html', context=context)

def cart_count(request):
    if 'user_id' in request.session:
        user_id = int(request.session.get('user_id'))
        return CartInfo.objects.filter(user_id=user_id).count()
    return cart_count