from django.db import models
from django.core import validators
from posts import thumbnail


# Create your models here.


class OnlineStore(models.Model):
    image = thumbnail.ImageField(upload_to='store_image', blank=True, null=True)
    title = models.CharField(max_length=50)
    description = models.TextField(null=True)
    parameters = models.TextField(null=True)

    price = models.FloatField()
    rate = models.FloatField(default=5, validators=[validators.MaxValueValidator(5)])



from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='category_icons/')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

