from django.db import models

# Create your models here.
class UrineStrip(models.Model):
    username = models.CharField(max_length=60)
    image = models.ImageField(upload_to='images/')
    rgb = models.JSONField()
