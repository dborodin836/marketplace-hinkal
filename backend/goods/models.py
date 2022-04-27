from django.db import models
from datetime import datetime as dt

from user.models import Vendor


class Dish(models.Model):
    """Contains dishes"""
    title = models.CharField(max_length=255, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Image', default='default/not-found.png')
    added_date = models.DateTimeField(default=dt.now(), verbose_name='Added')
    added_by = models.ForeignKey(Vendor, null=True, on_delete=models.CASCADE, verbose_name='Vendor')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Price')
    is_active = models.BooleanField(default=True, verbose_name='Showed to user')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Dish'
        verbose_name_plural = 'Dishes'
