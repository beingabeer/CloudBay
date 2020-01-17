from django.contrib import admin

from .models import Item, OrderItem, Order


class ItemModelAdmin(admin.ModelAdmin):
    list_display = ["title", "price"]

    class Meta:
        model = Item


class OrderItemModelAdmin(admin.ModelAdmin):
    list_display = ["item"]

    class Meta:
        model = OrderItem


class OrderModelAdmin(admin.ModelAdmin):
    list_display = ["user", "start_date", "ordered_date"]

    class Meta:
        model = Order


admin.site.register(Item, ItemModelAdmin)
admin.site.register(OrderItem, OrderItemModelAdmin)
admin.site.register(Order, OrderModelAdmin)
