from django.core.cache import cache
from .models import Product, Category


def get_product_by_category(category_slug, use_cache=True):
  cache_key = f'products_by_category_{category_slug}'

  if use_cache:
      products = cache.get(cache_key)
      if products is not None:
          return products

  try:
    category = Category.objects.get(slug=category_slug)
    products = list(Product.objects.filter(
        category=category,
        is_published=True
    ).select_related('owner', 'category'))

  except Category.DoesNotExist:

    products = []

    cache.set(cache_key, products, 60 * 15)

  return products

def get_category_stats():
  cache_key = 'category_stats'
  stats = cache.get(cache_key)

  if stats is not None:
      from django.db.models import Count, Avg
      stats = Category.objects.annotate(
          product_count=Count('products'),
          avg_count=Avg('products_count')
      ).values('name', 'slug', 'products_count', 'avg_price')

      stats = list(stats)
      cache.set(cache_key, stats, 60 * 15)

      return stats






