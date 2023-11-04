from django.contrib import admin
from .models import Product, Category, Brand


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "brand", "price")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


class BrandAdmin(admin.ModelAdmin):
    list_display = ("name", "country")


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
