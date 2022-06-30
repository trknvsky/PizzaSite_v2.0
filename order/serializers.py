from rest_framework import status, serializers, viewsets
from order.models import Order
from dishes.serializers import InstanceDishSerializer

class OrderSerializer(serializers.ModelSerializer):

    dishes = InstanceDishSerializer(many=True)
    
    class Meta:
        model = Order
        fields = ['dishes', 'date_create', 'full_price', 'phone_number', 'first_name', 'adress']
