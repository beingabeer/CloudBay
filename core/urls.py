from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.HomeView.as_view(), name="item-list"),
    path("product/<slug>", views.ItemDetailView.as_view(), name="product-detail"),
    path("checkout/", views.checkout, name="checkout-page"),
    path("add-to-cart/<slug>/", views.add_to_cart, name="add-to-cart"),
]
