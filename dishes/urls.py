from dishes.views import *
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'pizzas_list', DishViewSet)
router.register(r'ingredients_list', IngredientViewSet)
router.register(r'instance_list', InstanceDishViewSet)

urlpatterns = [
    path(r'', include(router.urls))
]
