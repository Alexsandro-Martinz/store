from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, related_name="category_id", on_delete=models.DO_NOTHING, null=True, default=None)
    expire_date = models.DateField()
    units = models.IntegerField(blank=True, default=0)

    def __str__(self) -> str:
        return self.product_name
