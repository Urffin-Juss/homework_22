from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Заполняет базу тестовыми данными (удаляет старые)'

    def handle(self, *args, **options):
        # Удаляем старые данные
        self.stdout.write('Удаление старых данных...')
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Создаем категории
        categories = [
            {'name': 'Электроника', 'description': 'Техника и гаджеты'},
            {'name': 'Книги', 'description': 'Художественная литература'},
            {'name': 'Одежда', 'description': 'Мужская и женская одежда'},
            {'name': 'Мебель', 'description': 'Для дома и офиса'},
        ]

        for cat_data in categories:
            Category.objects.create(**cat_data)

        self.stdout.write(f'Создано {len(categories)} категорий')

        # Создаем продукты
        electronics = Category.objects.get(name='Электроника')
        books = Category.objects.get(name='Книги')
        clothes = Category.objects.get(name='Одежда')
        furniture = Category.objects.get(name='Мебель')

        products = [
            {'name': 'Смартфон', 'price': 29999.99, 'category': electronics},
            {'name': 'Ноутбук', 'price': 89999.50, 'category': electronics},
            {'name': 'Наушники', 'price': 4999.00, 'category': electronics},
            {'name': 'Роман', 'price': 599.99, 'category': books},
            {'name': 'Учебник', 'price': 1299.00, 'category': books},
            {'name': 'Футболка', 'price': 1999.00, 'category': clothes},
            {'name': 'Джинсы', 'price': 3999.00, 'category': clothes},
            {'name': 'Стул', 'price': 4999.00, 'category': furniture},
            {'name': 'Стол', 'price': 12999.00, 'category': furniture},
        ]

        for prod_data in products:
            Product.objects.create(**prod_data)

        self.stdout.write(self.style.SUCCESS(f'Создано {len(products)} продуктов'))

        # Выводим статистику
        self.stdout.write('\nСтатистика:')
        for category in Category.objects.all():
            count = Product.objects.filter(category=category).count()
            self.stdout.write(f'{category.name}: {count} продуктов')