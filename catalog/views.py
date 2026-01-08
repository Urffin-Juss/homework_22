from gc import get_objects

from django.shortcuts import render
from catalog.models import Product


def home(request):
    """Главная страница со списком товаров"""
    products = Product.objects.all()[:12]  # Ограничим 12 товарами
    for product in products:
        # Обрезаем описание для превью
        if product.description and len(product.description) > 100:
            product.description_preview = product.description[:100] + '...'
        else:
            product.description_preview = product.description or ''

    context = {
        'products': products,
        'title': 'Главная страница'
    }
    return render(request, 'catalog/home.html', context)

def contacts(request):
    return render(request, 'catalog/contacts.html')

def product_details(request, product_id):
    product = get_objects_or_404(Product, id=product_id)
    context = {
        'product': product
        'title': f'{product.name} - Детали'

        }
    return render(request, 'catalog/product_detail.html', context)


