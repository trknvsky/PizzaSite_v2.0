from rest_framework import status, serializers, viewsets
from dishes.models import Dish, Ingredient, InstanceDish
from order.models import Order


class IngregientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name']


class DishSerializer(serializers.ModelSerializer):
    ingredients = IngregientSerializer(many=True)

    class Meta:
        model = Dish
        fields = ['name', 'ingredients', 'dish_img', 'price']


class InstanceDishSerializer(serializers.ModelSerializer):

    name = serializers.CharField(required=False)

    class Meta:
        model = InstanceDish
        fields = ['name', 'price', 'count', 'dish']

    def create(self, validated_data):
        dish_id = self.initial_data.get('dish')
        dish = Dish.objects.get(id=dish_id)
        count = self.initial_data.get('count')
        order, created = Order.objects.get_or_create()
        order.dishes.add(InstanceDish.objects.create(
            **validated_data,
            name=dish.name,
            price=dish.price)
            )
        order.calculate_price()
        return validated_data

    def to_representation(self, instance):
        ret = super(InstanceDishSerializer, self).to_representation(instance)
        dish = Dish.objects.get(id=ret['dish'])
        ret['name'] = dish.name
        ret['price'] = dish.price
        ret['full_price'] = dish.price * ret['count']
        return ret
