from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('buy/<int:product_id>/', views.purchase, name='purchase'),  # Обработка покупки товара
]
