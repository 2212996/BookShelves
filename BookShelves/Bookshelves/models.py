from django.db import models

class Image(models.Model):

    image = models.ImageField(
        verbose_name="画像",
        blank=True,
        null=True
    )

    class Meta:
        db_table = "image"
