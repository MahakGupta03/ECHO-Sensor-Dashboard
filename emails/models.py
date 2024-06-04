from django.db import models

# Create your models here.

class Gases(models.Model):
    hydrogensulfide = models.FloatField()
    # carbondioxide = models.FloatField()
    # ammonia = models.FloatField()
    float_level = models.FloatField()
    
