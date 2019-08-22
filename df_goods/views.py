from django.shortcuts import render, HttpResponse
from .models import TypeInfo, GoodsInfo

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

    cart_num = 0
    if 'user_id' in request.session:
        pass
        # cart_num = request.session.get('user_id')

    context = {
        'title': '主页',
        'guest_cart': 1,
        'cart_num': cart_num,
        'type0': type0, 'type01': type01,
        'type1': type1, 'type11': type11,
        'type2': type2, 'type21': type21,
        'type3': type3, 'type31': type31,
        'type4': type4, 'type41': type41,
        'type5': type5, 'type51': type51,
    }
    return render(request, 'df_goods/index.html', context=context)

def detail(request, goods_id):
    cart_num = 0
    goods = GoodsInfo.objects.filter(id=int(goods_id)).first()
    # 点击量+1
    goods.gclick = goods.gclick + 1
    goods.save()

    # 上新
    news = goods.gtype.goodsinfo_set.order_by('-id')[0:2]
    context = {
        'title': '商品详情',
        'guest_cart': 1,
        'cart_num': cart_num,
        'goods': goods,
        'id': goods_id,
        'news': news,
    }
    resposne = render(request, 'df_goods/detail.html', context=context)
    return resposne