from django.db import models


class Award(models.Model):
    title = models.CharField(max_length=60)
    img = models.ImageField(upload_to='static/images')

    def __str__(self):
        return self.title