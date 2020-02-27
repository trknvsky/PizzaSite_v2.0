from django.db import models
from dishes.models import Dish, Drink, InstanceDish, InstanceDrink
from accounts.models import User
from phonenumber_field.modelfields import PhoneNumberField
from accounts.views_api import UserApiView
from accounts.models import User


class Order(models.Model):
    dishes = models.ManyToManyField(InstanceDish, blank=True, null=True)
    drinks = models.ManyToManyField(InstanceDrink, blank=True, null=True)
    date_create = models.DateTimeField(auto_now_add=True)
    full_price = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    user_profile = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    phone_number = PhoneNumberField(null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    adress = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return '{}'.format(self.id)

    def dishes_list(self):
        return ([dish.name for dish in self.dishes.all()])

    def calculate_price(self):
        self.full_price = 0
        for dish in self.dishes.all():
            self.full_price += dish.price * dish.count
            print(self.full_price, dish.price, dish.count)
        for drink in self.drinks.all():
            self.full_price += drink.price * drink.count
        self.save()

    def get_serialize_data(self):
        print(self.user_profile.id)
        return{
            'dishes': list(self.dishes.all().values_list('name', 'count', 'price')),
            'date': self.date_create,
            'full_price': self.full_price,
            'phone': str(self.phone_number),
            'first_name': self.first_name,
            'adress': self.adress
        }
