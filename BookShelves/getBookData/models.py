from django.db import models

# Create your models here.
class BookData(models.Model):
    isbn = models.IntegerField()
    title = models.CharField(max_length = 255, null=True)
    author = models.CharField(max_length = 255, null=True)
    publisher = models.CharField(max_length = 255, null=True)

    class Meta:
        db_table = "bookdata"
        verbose_name_plural = 'bookdata'