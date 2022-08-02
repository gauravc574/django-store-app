from distutils.command.upload import upload
from unicodedata import category
from django.db import models
from .category import Category

class Product(models.Model):
    name =  models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1) #on deletion of category respective products will be deleted
    description = models.CharField(max_length=200, default="", null=True, blank=True)
    image = models.ImageField(upload_to = "uploads/products/")

    def __str__(self) -> str:
        return self.name

    @staticmethod
    def get_all_products():
        return Product.objects.all()