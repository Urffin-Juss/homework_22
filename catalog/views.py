from gc import get_objects

from django.shortcuts import render
from catalog.models import Product

def home(request):
    return render(request, 'catalog/home.html')

def contacts(request):
    return render(request, 'catalog/contacts.html')

def product_details(request, product_id):
    product = get_objects_or_404(Product, id=product_id)
    context = {
        'product': product
        'title': f'{product.name} - Детали'

        }
    return render(request, 'catalog/product_detail.html', context)


