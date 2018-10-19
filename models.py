from django.db import models

class Picture(models.Model):
    image =  models.ImageField(blank=True,null=True)
