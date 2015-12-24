from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=255, unique=True)
    def __unicode__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=255) # product item name (e.g. sleeveless dress)
    price = models.DecimalField(max_digits=10, decimal_places=2) # product price (e.g. $19.99)
    link = models.URLField(max_length=500) # link to external url to buy item
    image = models.CharField(max_length=500) # link to image source
    brand = models.ForeignKey('Brand', related_name="brand")
    
    def __unicode__(self):
        return self.name
