from django.shortcuts import render
from dishes.models import Dish, Drink, InstanceDish, Ingredient
from django.views.generic import TemplateView, ListView, View, FormView
from django.http import HttpResponse
from django import forms
from django.views.generic.edit import UpdateView, FormView
from dishes.forms import *
from django.core.paginator import Paginator
from rest_framework import routers, serializers, viewsets
from dishes.serializers import DishSerializer, IngregientSerializer, InstanceDishSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from project.celery import *
from .tasks import *
from django.core.paginator import Paginator
from django.shortcuts import render

class AboutView(TemplateView):
    template_name = 'order_sucess.html'


class DrinkListView(ListView):
    model = Drink
    template_name = 'drink_list.html'


class AddNewDrinkView(FormView):
    form_class = DrinkForm
    template_name = 'send.html'
    success_url = '/drinks'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class DrinkUpdateView(UpdateView):
    form_class = DrinkForm
    model = Drink
    template_name = 'send.html'
    success_url = '/drinks'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class DishListView(ListView):
    model = Dish
    template_name = 'dish_list.html'
    sorting_fields = ['name', 'price', '-price']
    paginate_by = 12

    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.GET.get('ordering', 'name')
        print(Dish.objects.all())
        if ordering not in self.sorting_fields:
            ordering = 'name'
        queryset = Dish.objects.all().order_by(ordering)
        return queryset

    # @method_decorator(cache_page(60))
    # def dispatch(self, request, *args, **kwargs):
    #     return super(DishListView, self).dispatch(request, *args, **kwargs)
    
    # def listing(request):
    #     dish_list = Dish.objects.all().order_by('name')
    #     paginator = Paginator(dish_list, 12) # Show 25 contacts per page

    #     page = request.GET.get('page')
    #     dishes = paginator.get_page(page)
    #     return render(request, 'dish_list.html', {'dishes': dishes})


class DishView(ListView):
    model = Dish
    template_name = 'dishes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dish_count'] = Dish.objects.count()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = Dish.objects.values_list('name', flat=True).order_by('price')
        return queryset


class AddNewDishView(FormView):
    form_class = DishForm
    template_name = 'send.html'
    success_url = '/dishes'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class DishUpdateView(UpdateView):
    form_class = DishForm
    model = Dish
    template_name = 'send.html'
    success_url = '/dishes'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ChangePriceDishView(FormView):
    form_class = ChangePriceForm
    template_name = 'change_price_form.html'
    success_url = '/dishes'

    def form_valid(self, form):
        price = form.cleaned_data.get('price')
        Dish.change_price(price)
        return super().form_valid(form)


class IngredientListView(ListView):
    model = Ingredient
    template_name = 'ingredients_list.html'


class AddNewIngredientView(FormView):
    form_class = IngredientForm
    template_name = 'send.html'
    success_url = '/ingredients'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class IngredientUpdateView(UpdateView):
    form_class = IngredientForm
    model = Ingredient
    template_name = 'send.html'
    success_url = '/ingredients'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngregientSerializer


class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all().order_by('name')
    serializer_class = DishSerializer


class InstanceDishViewSet(viewsets.ModelViewSet):
    queryset = InstanceDish.objects.all()
    serializer_class = InstanceDishSerializer
