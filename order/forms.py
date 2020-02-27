from django import forms
from django.forms import ModelForm
from order.models import Order
from dishes.models import *


class DishForm(forms.Form):
    dish_id = forms.IntegerField()
    count = forms.IntegerField()


class ChangeInstanceForm(ModelForm):
    class Meta:
        model = InstanceDish
        fields = ['count']


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['phone_number', 'first_name', 'adress']


class DrinkForm(forms.Form):
    drink_id = forms.IntegerField()
    count = forms.IntegerField()
