from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.item_list, name="item-list"),
    path("product/", views.product, name="product-page"),
    path("checkout/", views.checkout, name="checkout-page"),
]
