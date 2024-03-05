from django.db import models

# Create your models here.
class FlipkartData(models.Model):
    product_name = models.CharField(max_length=1000)
    image_source = models.CharField(max_length=1000)
    ratings = models.CharField(max_length=50)
    brand_name = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    actual_price = models.CharField(max_length=50)
    category = models.CharField(max_length=50)

class GemData(models.Model):
    product_name = models.CharField(max_length=1000)
    image_source = models.CharField(max_length=1000)
    ratings = models.CharField(max_length=50)
    brand_name = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    actual_price = models.CharField(max_length=50)
    category = models.CharField(max_length=50)