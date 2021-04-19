from datetime import datetime

from django.db import models

# Create your models here
from django.utils import timezone
from djmoney.models.fields import MoneyField


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    @property
    def get_products(self):
        return Product.objects.filter(category__name=self.name)

    class Meta:
        verbose_name = 'Categorie'


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False)
    short_description = models.TextField(max_length=200)
    full_description = models.TextField(max_length=10000, blank=True)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', blank=False)
    discount = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', blank=False, default=0)
    image = models.ImageField(upload_to="images/", blank=False, default='')
    image2 = models.ImageField(upload_to="images/", blank=False, default='')
    document = models.FileField(upload_to="documents/", blank=False, default='')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    class Meta:
        verbose_name = 'Product'
