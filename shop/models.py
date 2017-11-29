from django.db import models

# Create your models here.

class Apparel(models.Model):

    apparel_name=models.Charfield(max_length=255)
    apparel_image=models.CharField(max_length=1000)
    apparel_brand=models.CharField(max_length=255)
    apparel_size=models.CharField(max_length=255)

    def __str__(self):
        return