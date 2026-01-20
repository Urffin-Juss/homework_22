from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from products.models import Product


class Command(BaseCommand):
    help = 'Создает группу "Модератор продуктов" с необходимыми правами'

    def handle(self, *args, **kwargs):
        # Получаем ContentType для модели Product
        content_type = ContentType.objects.get_for_model(Product)

        # Получаем нужные разрешения
        delete_permission = Permission.objects.get(
            codename='delete_product',
            content_type=content_type
        )

        unpublish_permission = Permission.objects.get(
            codename='can_unpublish_product',
            content_type=content_type
        )

        # Создаем или получаем группу
        group, created = Group.objects.get_or_create(name='Модератор продуктов')

        # Добавляем разрешения
        group.permissions.add(delete_permission, unpublish_permission)

        if created:
            self.stdout.write(self.style.SUCCESS('Группа "Модератор продуктов" создана'))
        else:
            self.stdout.write(self.style.WARNING('Группа уже существует, обновлена'))

        self.stdout.write(f'Добавлены права: {delete_permission.name}, {unpublish_permission.name}')