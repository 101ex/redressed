from django.db import models

# Create your models here.

class Article(models.Model):
    article_title = models.CharField(max_length=64)
    article_image = models.CharField(max_length=1000)
    article_content = models.CharField(max_length=64)

    def __str__(self):
        return self.article_title + " | " + self.article_image + " | " + self.article_content