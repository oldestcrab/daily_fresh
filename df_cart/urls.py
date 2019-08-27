from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^add(?P<goods_id>\d+)_(?P<count>\d+)/$", views.add, name="add"),

]
