from django.db import models
from df_goods.models import GoodsInfo
from datetime import datetime
# Create your models here.
class UserInfo(models.Model):
    uname = models.CharField(max_length=20, unique=True)
    upwd = models.CharField(max_length=40, blank=False)
    uemail = models.EmailField(unique=True)
    uaddress = models.CharField(max_length=100, default='')
    uphone = models.CharField(max_length=11, default='')
    uyoubian = models.CharField(max_length=6, default='')
    ushou = models.CharField(max_length=20, default='')

    def _str__(self):
        return self.uname

class GoodsBrowser(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name='用户ID')
    good = models.ForeignKey(GoodsInfo, on_delete=models.CASCADE, verbose_name='商品ID')
    browser_time = models.DateTimeField(default=datetime.now, verbose_name='浏览时间')

    class Meta:
        verbose_name = '用户浏览记录'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{user}浏览记录{title}'.format(user=self.user.name, title=self.good.gtitle)