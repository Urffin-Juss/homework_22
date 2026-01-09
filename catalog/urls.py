from django.urls import path, include
from catalog.apps import CatalogConfig
from . import views


app_name = 'catalog'

urlpatterns = [
    path('',views.home,name='home'),
    path('contacts/',views.contacts,name='contacts'),
    path('products/<int:product_id>', views.product_detail, name='product_detail'),


]
