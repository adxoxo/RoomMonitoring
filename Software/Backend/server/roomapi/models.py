from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=200, null=True)    
    mac_address = models.CharField(max_length=200, null=True)
    listed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}" 

class RoomParameters(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    temp = models.FloatField(null=True)
    humidity = models.FloatField(null=True)
    air_quality = models.FloatField(null=True)
    dust_ppm = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.room}" 
    