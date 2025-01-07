from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    category = models.CharField(max_length=255)
    author = models.CharField(max_length=255)