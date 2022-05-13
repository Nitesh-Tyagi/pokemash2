from django.db import models

# Create your models here.

class Photo(models.Model):
    name = models.CharField(primary_key=True, default="", max_length=30)
    img = models.ImageField(upload_to='static', default="")
    rating = models.PositiveSmallIntegerField(default=1400,blank=True,null=True)