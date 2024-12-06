from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default=0)  # Количество товара

    def __str__(self):
        return f"{self.name} ({self.quantity} шт.)"

# Модель покупки
class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    person = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=1)  # Поле для количества товара, которое покупатель хочет купить

    def __str__(self):
        return f"Покупка {self.product.name} ({self.person})"
