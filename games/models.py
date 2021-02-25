from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, primary_key=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=100, null=True)
    year = models.IntegerField()
    category = models.ForeignKey(Category, related_name="games", on_delete=models.CASCADE)
   
    def __str__(self):
        return self.name

