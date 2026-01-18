from django.db import models

class BlogPost(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    content = models.TextField("Содержимое")
    preview = models.ImageField("Превью", upload_to="blog/preview/", blank=True, null=True)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    is_published = models.BooleanField("Опубликовано", default=False)
    views_count = models.IntegerField("Просмотры", default=0)

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return self.title

