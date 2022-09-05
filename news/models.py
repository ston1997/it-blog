from django.db import models
from django.urls import reverse, reverse_lazy


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='обновлено')
    photo = models.ImageField(upload_to='photos/%Y%m%d', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='категория')


    def get_absolute_url(self):
        return reverse('view_news', kwargs={"news_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'
        ordering = ['-created_at', '-title']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['title']
