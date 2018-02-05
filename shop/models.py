from django.db import models

# Create your models here.

class ApparelType(models.Model):

    type=models.CharField(max_length=255)
    image=models.FilePathField(max_length=100)

    def __str__(self):
        return self.type + "|" + self.image

class Apparel(models.Model):

    image=models.FilePathField(path=None, max_length=100)
    brand=models.CharField(max_length=255)
    size=models.CharField(max_length=255)
    price=models.PositiveIntegerField()

    sold=models.BooleanField(default=False)
    type=models.ForeignKey(ApparelType, on_delete=models.CASCADE)

    def __str__(self):
        return self.image + "|" + self.brand + "|" + self.size