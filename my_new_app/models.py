from django.db import models

# Create your models here.
class shop(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    img = models.ImageField(upload_to='picture')
    price = models.IntegerField()