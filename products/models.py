from django.db import models
from django.utils import timezone

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    modification = models.CharField(max_length=100, primary_key=True, verbose_name='Версия')
    release_date = models.DateField(default=timezone.now, **NULLABLE, verbose_name='Дата выпуска')
    description = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='image/', **NULLABLE)
    price = models.FloatField(verbose_name='Цена')
    date_org = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.name} {self.modification}'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='Версия')
    release_date = models.DateField(default=timezone.now, **NULLABLE, verbose_name='Дата выпуска')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'

    def __str__(self):
        return f'{self.title} {self.release_date}'
