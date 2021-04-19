from django.contrib import admin
from Product.models import Category, Product


# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'short_description', 'pub_date']


admin.site.register(Product, ProductAdmin)
