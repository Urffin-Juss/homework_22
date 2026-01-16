from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import path
from .views import HomeView, ContactsView, ProductDetailView, ProductDeleteView, ProductUpdateView, ProductCreateView, \
    ProductListView

app_name = 'catalog'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('products/<int:product_id>/', ProductDetailView.as_view(), name='product_detail' ),
    path('products/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:product_id>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('products/<int:product_id>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail')
    path('products/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:product_id>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('products/<int:product_id>/update/', ProductUpdateView.as_view(), name='product_update'),



]
