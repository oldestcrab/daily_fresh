from django.db import models

# Create your models here.
class OrderInfo(models.Model):
    oid = models.CharField(max_length=20, primary_key=True, verbose_name='大订单号')
    user = models.ForeignKey("df_user.UserInfo", verbose_name='订单用户', on_delete=models.CASCADE)
    odate = models.DateField(auto_now=True, verbose_name='订单创建时间')
    ototal = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='订单总价')
    oaddress = models.CharField(max_length=150, verbose_name='订单地址')
    ois_pay = models.BooleanField(default=False, verbose_name='是否支付')

    class Meta:
        verbose_name = '订单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{user}在{date}订单'.format(user=self.user.uname, date=self.odate)

class OrderDetailInfo(models.Model):
    goods = models.ForeignKey("df_goods.GoodsInfo", verbose_name='商品', on_delete=models.CASCADE)
    order = models.ForeignKey("OrderInfo", verbose_name='订单', on_delete=models.CASCADE)
    count = models.IntegerField(verbose_name='商品数量')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='商品价格')

    class Meta:
        verbose_name = '订单详情'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{goods}(数量为{count})'.format(goods=self.goods.gtitle, count=self.count)