from django.db import models

    
class Category(models.Model):
    category_name = models.CharField(100, unique=True)
    
    def __str__(self) -> str:
        return self.category_name
    
class Product(models.Model):
    product_name = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, default=None)
    expire_date = models.DateField()
    units = models.IntegerField()
    
    def __str__(self) -> str:
        return self.product_name
    