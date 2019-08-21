from django.contrib import admin

# Register your models here.
from .models import TypeInfo, GoodsInfo
# 注册模型类  普通方法
class TypeinfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'ttitle']
    list_per_page = 10
    search_fields = ['ttitle']
    list_display_links = ['ttitle']

class GoodsInfoAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['id', 'gtitle', 'gunit', 'gclick', 'gprice', 'gpic', 'gkucun', 'gjianjie']
    list_editable = ['gkucun']
    readonly_fields = ['gclick']
    search_fields = ['gtitle', 'gcontent', 'gjianjie']
    list_display_links = ['gtitle']

admin.site.register(TypeInfo, TypeinfoAdmin)
admin.site.register(GoodsInfo)