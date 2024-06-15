from django.test import TestCase
from django.urls import reverse

class FoodTableTests(TestCase):

    def test_food_table_view(self):
        response = self.client.get(reverse('food-table'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'food_table.html')
