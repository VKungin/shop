from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bio = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    brand = models.ForeignKey("Brand", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=64, unique=True)
    country = models.CharField(max_length=64, unique=False)

    def __str__(self):
        return self.name
