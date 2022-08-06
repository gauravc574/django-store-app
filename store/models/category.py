from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self) -> str:
        return self.name

    @staticmethod
    def get_all_categories():
        return Category.objects.all()