from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.HomeView.as_view(), name="item-list"),
    path("product/", views.products, name="product-page"),
    path("checkout/", views.checkout, name="checkout-page"),
]
