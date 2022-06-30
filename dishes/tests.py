from django.test import TestCase
from dishes.models import Dish


class UrlsTest(TestCase):
    def test_drinks_page(self):
        response = self.client.get("/drinks/")
        self.assertEqual(response.status_code, 200)

    def test_home_page(self):
        response = self.client.get("/home/")
        self.assertEqual(response.status_code, 200)


class DishListViewTest(TestCase):
    def setUp(self):
        pass

    @classmethod
    def setUpTestData(cls):
        dish_count = 15
        for dish in range(dish_count):
            Dish.objects.create(name="PizzaTest", price=140, dish_img=" ")

    def test_view_uses_correct_template(self):
        response = self.client.get('/dishes/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dish_list.html')

    def test_pagination_is_twelve(self):
        response = self.client.get('/dishes/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] is True)
        self.assertTrue(len(response.context['dish_list']) == 12)

    def test_lists_all_dishes(self):
        response = self.client.get('/dishes/?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] is True)
        self.assertTrue(len(response.context['dish_list']) == 3)
