from order.models import Order


def order(request):
    return {"order_list": Order.objects.all()}
