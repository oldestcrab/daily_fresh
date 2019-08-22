from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<goods_id>\d+)/$', views.detail, name='detail'),
    url(r'^list_(?P<type_id>\d+)_(?P<page_id>\d+)_(?P<sort_id>\d+)/$', views.goods_list, name='goods_list'),
]