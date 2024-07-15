from django.db import models
from apps.user.models import User

class Article(models.Model):

    name = models.CharField(
        max_length=200,
        verbose_name='Название статьи'
    )

    article_text = models.TextField(
        verbose_name='Текст статьи'
    )

    is_public = models.BooleanField(
        default=True
    )

    user = models.ForeignKey(
        User, 
        verbose_name='Автор статьи', 
        on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.name
