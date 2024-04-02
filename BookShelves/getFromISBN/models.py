from django.db import models

# Create your models here.
class ISBN(models.Model):
    isbn = models.IntegerField()