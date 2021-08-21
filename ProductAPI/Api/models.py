from django.db import models

class Product(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    Color = models.CharField(max_length=500)
    size = models.CharField(max_length=10)

    def __str__(self):
        return self.name


 