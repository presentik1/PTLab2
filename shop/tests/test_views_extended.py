from django.test import TestCase, Client
from shop.models import Product, Purchase

class ExtendedPurchaseViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.product = Product.objects.create(name="pen", price=50, quantity=10)

    def test_valid_purchase(self):
        response = self.client.post(f'/buy/{self.product.id}/', {
            'quantity': 2,
            'person': 'Alice',
            'address': 'Wonderland'
        })
        self.assertEqual(response.status_code, 200)
        purchase = Purchase.objects.get(product=self.product)
        self.assertEqual(purchase.quantity, 2)
        self.assertEqual(self.product.quantity, 8)

    def test_invalid_quantity(self):
        response = self.client.post(f'/buy/{self.product.id}/', {
            'quantity': 20,  # Превышение количества
            'person': 'Bob',
            'address': 'Nowhere'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Недостаточно товара в наличии")

class ExtendedIndexViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        Product.objects.create(name="book", price=740, quantity=10)

    def test_index_page_content(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "book")
        self.assertContains(response, "740")
        self.assertContains(response, "10")  # Проверка количества товара
