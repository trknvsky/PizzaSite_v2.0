from order.views import *
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'orders_list', OrderViewSet)

urlpatterns = [
    path(r'', include(router.urls))
]
