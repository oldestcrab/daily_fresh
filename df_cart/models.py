from django.db import models

# Create your models here.
class CartInfo(models.Model):
    user = models.ForeignKey("df_user.UserInfo", verbose_name="用户", on_delete=models.CASCADE)
    goods = models.ForeignKey("df_goods.GoodsInfo", verbose_name="商品", on_delete=models.CASCADE)
    count = models.IntegerField(default=0)

    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.uname + '的购物车'