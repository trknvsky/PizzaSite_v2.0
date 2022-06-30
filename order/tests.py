from django.test import TestCase
from order.models import Order
from order.forms import OrderForm


class UrlsTest(TestCase):

    def test_order_page(self):
        response = self.client.get("/order/")
        self.assertEqual(response.status_code, 200)

    def test_order_sucess_page(self):
        response = self.client.get("/order_sucess/")
        self.assertEqual(response.status_code, 200)


class OrderFormTest(TestCase):

    def setUp(self):
        Order.objects.create(
            full_price="500",
            date_create="15.12.2019",
        )

    def test_order_form_true(self):
        form_data = {
            'phone_number': '+380931444144',
            'first_name': 'Cat',
            'adress': "davida oistrakha, 32"
        }
        form = OrderForm(data=form_data)
        self.assertTrue(form.is_valid())
        response = self.client.post("/makeorder/1/", form_data)
        self.assertEqual(response.status_code, 302)

    def test_order_form_false(self):
        form_data = {
            'phone_number': '000000000000',
            'first_name': 'Cat',
            'adress': "davida oistrakha, 32"
        }
        form = OrderForm(data=form_data)
        self.assertFalse(form.is_valid())
