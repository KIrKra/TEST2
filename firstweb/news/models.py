from django.db import models
from django.urls import reverse

class News(models.Model):
    title = models.CharField('Название',max_length= 20)
    anons = models.CharField("Анонс",max_length=120)
    text = models.TextField('Статья')

    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'pk': self.pk})
    def __str__ (self):
        return f'Новость: {self.title}'
    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = "Новости"