from django.views.generic.base import View
from django.shortcuts import render, redirect, render_to_response
from django.http import JsonResponse
from dishes.models import Dish
from order.models import Order
from decimal import Decimal

class OrderApiView(View):

    def get(self, request):
        orders = Order.objects.all().order_by('date_create')
        serialized_orders = []
        for order in orders:
            serialized_orders.append(order.get_serialize_data())
        return JsonResponse({'orders_list': serialized_orders})


class PizzaToOrderApiView(View):

    def post(self, request, *args, **kwargs):
        orders = Order.objects.all()
        dish_id = request.POST.get('dish')
        dish = Dish.objects.get(id=dish_id)
        count = request.POST.get('count')
        instance = Dish.create_order(dish, count)
        order, created = Order.objects.get_or_create()
        order.dishes.add(instance)
        order.calculate_price()
        full_price = instance.price * Decimal(instance.count)
        serialized_dishes = {
            'pizza_name': instance.name,
            'pizza_count': instance.count,
            'pizza_price': full_price
        }
        return JsonResponse({'orders list': serialized_dishes})