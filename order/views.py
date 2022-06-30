from django.shortcuts import render
from order.models import *
from django.views.generic.edit import UpdateView, FormView
from django.views.generic import TemplateView, ListView, View, FormView
from order.forms import *
from dishes.models import *
from rest_framework import routers, serializers, viewsets
from order.serializers import OrderSerializer
from .tasks import *
from dishes.tasks import *


class AddDishView(FormView):
    template_name = "dish_list.html"
    form_class = DishForm
    success_url = '/dishes/'

    def form_valid(self, form):
        dish_id = form.cleaned_data.get('dish_id')
        # dish = Dish.objects.get(id=form.cleaned_data.get('dish_id'))
        count = form.cleaned_data.get("count")
        # instance = Dish.create_order(dish, count)
        # order, created = Order.objects.get_or_create()
        # order.dishes.add(instance)
        # order.calculate_price()
        order_add.delay(dish_id, count)
        parsing_pizzas.delay()
        return super().form_valid(form)


class AddDrinkView(FormView):
    template_name = 'drink_list.html'
    form_class = DrinkForm
    success_url = '/drinks/'

    def form_valid(self, form):
        drink = Drink.objects.get(id=form.cleaned_data.get('drink_id'))
        count = form.cleaned_data.get("count")
        instance = Drink.create_order(drink, count)
        order, created = Order.objects.get_or_create()
        order.drinks.add(instance)
        order.calculate_price()
        return super().form_valid(form)


class OrderView(ListView):
    model = Order
    template_name = 'order.html'


class InstanceUpdateView(UpdateView):
    form_class = ChangeInstanceForm
    model = InstanceDish
    template_name = 'send.html'
    success_url = '/order'

    def form_valid(self, form):
        instance = super().form_valid(form)
        order = Order.objects.get()
        order.calculate_price()
        return instance


class MakeOrderView(UpdateView):
    form_class = OrderForm
    model = Order
    template_name = "make_order.html"
    success_url = '/order_sucess/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
