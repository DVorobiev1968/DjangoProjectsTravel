from django.db import models

# создаем класс модели.
from django.urls import reverse


class City(models.Model):
    objects = None
    name = models.CharField(max_length=100, unique=True, verbose_name='Город')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Города'
        verbose_name_plural = 'Города'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('cities:detail', kwargs={'pk': self.pk})
