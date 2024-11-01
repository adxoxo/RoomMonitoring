from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Room, RoomParameters

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class RoomParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomParameters
        fields = '__all__'

class AverageRoomParametersSerializer(serializers.Serializer):
    room_name = serializers.CharField(read_only=True)
    average_temp = serializers.FloatField(read_only=True)
    average_humidity = serializers.FloatField(read_only=True)
    average_air_quality = serializers.FloatField(read_only=True)
    average_dust_ppm = serializers.FloatField(read_only=True)