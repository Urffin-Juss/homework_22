from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product
from .form import ProductForm


class HomeView(ListView):

    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

class ProductDetailView(DetailView):

    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'product_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = f"{self.object.name} - Детали"
        return context

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('products:poduct_list')

class ProductListView(ListView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('products:product_list')

class ProductDeleteView(DeleteView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_confir_delet.html'
    success_url = reverse_lazy('products:product_list')
