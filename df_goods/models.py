from django.db import models

from tinymce.models import HTMLField

# Create your models here.
class TypeInfo(models.Model):
    ttitle = models.CharField(max_length=20, verbose_name = '分类')
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.ttitle

    class Meta:
        verbose_name = '商品类型'
        verbose_name_plural = verbose_name

class GoodsInfo(models.Model):
    is_delete = models.BooleanField(default=False)
    gtitle = models.CharField(max_length=20, unique=True, verbose_name='商品名称')
    gprice = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='商品价格')
    gjianjie = models.CharField(max_length=200, verbose_name='简介')
    gunit = models.CharField(max_length=20, default='500g', verbose_name='单位重量')
    gclick = models.IntegerField(default=0, null=False, verbose_name='点击量')
    gcontent = HTMLField(max_length=200, verbose_name='详情')
    gkucun = models.IntegerField(default=0, verbose_name='库存')
    gpic = models.ImageField(upload_to='df_goods/image/%Y/%m', null=True, blank=True, verbose_name='商品图片')
    gtype = models.ForeignKey(TypeInfo, verbose_name='分类', on_delete=models.CASCADE)
    class Meta():
        verbose_name = '商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.gtitle