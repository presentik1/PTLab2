from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest
from .models import Product, Purchase

# Главная страница с товарами
def index(request):
    products = Product.objects.all().order_by('id')  # Сортировка по ID
    context = {'products': products}
    return render(request, 'shop/index.html', context)

# Страница покупки товара
def purchase(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    error_message = None
    
    if request.method == 'POST':
        # Получаем количество товара, которое хочет купить пользователь
        quantity = int(request.POST.get('quantity'))
        
        # Проверяем, достаточно ли товара
        if quantity > product.quantity:
            error_message = f"Недостаточно товара в наличии. Доступно {product.quantity} единиц."
        
        if not error_message:
            # Создаём покупку
            purchase = Purchase(
                product=product,
                person=request.POST.get('person'),
                address=request.POST.get('address'),
                quantity=quantity,  # Сохраняем количество, которое покупатель хочет купить
            )
            
            # Обновляем количество товара
            product.quantity -= quantity
            product.save()
            
            # Сохраняем покупку
            purchase.save()
            
            # Возвращаем ответ с кнопкой для возврата на главную
            return render(request, 'shop/thank_you.html', {
                'person': purchase.person,
                'quantity': purchase.quantity
            })
    
    return render(request, 'shop/purchase_form.html', {'product': product, 'error_message': error_message})
