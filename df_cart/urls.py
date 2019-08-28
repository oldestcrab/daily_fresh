from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^add(?P<goods_id>\d+)_(?P<count>\d+)/$", views.add, name="add"),
    url(r"^$", views.cart, name="cart"),
    url(r"^edit(?P<cart_id>\d+)_(?P<count>\d+)/$", views.edit, name="edit"),
    url(r"^delete(?P<cart_id>\d+)/$", views.delete, name="delete"),

]
