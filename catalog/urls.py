

from django.views.decorators.cache import cache_page
from django.urls import path
from .views import HomeView, ContactsView, ProductDetailView, ProductDeleteView, ProductUpdateView, ProductCreateView, \
    ProductListView


app_name = 'catalog'

urlpatterns = {
    path('', HomeView.as_view(), name='home'),
    path('contacts/<int:pk>/contacts/', ContactsView.as_view(), name='contacts'),
    path('categories/<slug:slug>/products/', cache_page(60 * 15)(ProductListView.as_view()), name='categories_list'),
    path('products/<int:pk>/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),


}
