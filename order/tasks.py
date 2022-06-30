from celery.task import task
from .models import Order
from dishes.models import Dish

@task()
def order_add(dish_id, count):
    dish = Dish.objects.get(id=dish_id)
    instance = Dish.create_order(dish, count)
    order, created = Order.objects.get_or_create()
    order.dishes.add(instance)
    print(instance)
    order.calculate_price()
