from django.views.generic.base import View
from django.shortcuts import render, redirect, render_to_response
from django.http import JsonResponse
from dishes.models import Dish


class DishApiView(View):

    sorting_fields = ['name', 'price', '-price']

    def get(self, request):
        ordering = request.GET.get('ordering', 'name')
        if ordering not in self.sorting_fields:
            ordering = 'name'
        dishes = Dish.objects.all().order_by(ordering)
        serialized_dishes = []
        for dish in dishes:
            serialized_dishes.append(dish.get_serialize_data())
        return JsonResponse({'pizzas_list': serialized_dishes})

    def post(self, request, *args, **kwargs):
        price_lt = request.POST.get('pizzas to')
        price_gt = request.POST.get('pizzas from')
        dishes = Dish.objects.all().filter(price__lt=price_lt).filter(price__gt=price_gt)
        serialized_dishes = []
        for dish in dishes:
            serialized_dishes.append(dish.get_serialize_data())
        return JsonResponse({'pizzas_list': serialized_dishes})
