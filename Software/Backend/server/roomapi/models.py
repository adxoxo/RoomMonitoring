from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=200, null=True)    
    device_id = models.CharField(max_length=200, null=True)
    listed = models.BooleanField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)

class RoomParameters(models.Model):
    temp = models.FloatField(null=True)
    humidity = models.FloatField(null=True)
    air_quality = models.FloatField(null=True)
    dust_ppm = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    