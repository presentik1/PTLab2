from django.test import TestCase
from shop.models import Product, Purchase

class ExtendedProductTestCase(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name="notebook", price=100, quantity=20)

    def test_quantity_update(self):
        self.product.quantity -= 5
        self.product.save()
        self.assertEqual(self.product.quantity, 15)

    def test_product_deletion(self):
        product_id = self.product.id
        self.product.delete()
        self.assertFalse(Product.objects.filter(id=product_id).exists())
