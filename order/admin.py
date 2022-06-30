from django.contrib import admin
from order.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'dishes_list', 'full_price', 'user_profile', 'date_create']


admin.site.register(Order, OrderAdmin)
