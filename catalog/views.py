

from django.contrib.auth.decorators import login_required, permission_required
from django.http import  HttpResponseForbidden
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product
from .form import ProductForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


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

class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'

    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'product_id'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = f"{self.object.name} - Детали"
        return context

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('products:product_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProductListView(ListView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'



class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('products:product_list')

    def test_func(self):
        product = self.get.object()
        return product.owner == self.request.user

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('products:product_list')

    def test_func(self):
        product = self.get.object()
        if product.owner == self.request.user:
            return True
        if self.request.user.groups.filter(name='Moderator').exists():
            return True
        return False

    def handle_no_permission(self):

        return HttpResponseForbidden("You don't have permission to delete this product.")


@login_required
@permission_required('product.can_unpublishing_product', raise_exception=True)
def unpublish_product(request, pk):
    product = get_objects_or_404(Product, pk=pk)
    product.is_published = False
    product.save()
    return redirect('products:product_list')

def product_list(request):
    products = Product.objects.filter(is_published=True)
    return render(request, 'catalog/product_list.html', {'products': products})

@login_required
def my_products(request):
    products = Product.objects.filter(owner=request.user)
    return render(request, 'products/my_product.html', {'products': products})

@cache_page(60 * 15)
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk, is_published=True)
    return render(request, 'catalog/product_detail.html', {'product': product})
