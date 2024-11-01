from django.shortcuts import render
from rest_framework import serializers
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response 
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Avg
# Create your views here.
 
from .models import Room, RoomParameters
from .serializers import RoomSerializer, RoomParameterSerializer, AverageRoomParametersSerializer
# Create your views here.

class RoomListedView(ViewSet):
    
    def RoomsListed(self, request):
    
        listedrooms = Room.objects.filter(listed=True)
        serializer = RoomSerializer(listedrooms, many=True)

        return Response(serializer.data, status=200)


class RoomUnlistedView(ViewSet):

    def RoomsUnlisted(self, request):
    
        listedrooms = Room.objects.filter(listed=False)
        serializer = RoomSerializer(roomsunlisted, many=True)

        return Response(serializer.data, status=200)

class RoomParametersView(ViewSet):

    def RoomParametersGet(self, request, room_id):

        try:
            room = Room.objects.get(pk=room_id)
            room_parameters = RoomParameters.objects.filter(room=room)

            if not room_parameters.exists():
                return Response({'message': 'No parameters found for this room'}, status=status.HTTP_404_NOT_FOUND)

            average_temp = room_parameters.aggregate(Avg('temp'))['temp__avg']
            average_humidity = room_parameters.aggregate(Avg('humidity'))['humidity__avg']
            average_air_quality = room_parameters.aggregate(Avg('air_quality'))['air_quality__avg']
            average_dust_ppm = room_parameters.aggregate(Avg('dust_ppm'))['dust_ppm__avg']

            serializer = AverageRoomParametersSerializer({
                'room_name': room.name,
                'average_temp': average_temp,
                'average_humidity': average_humidity,
                'average_air_quality': average_air_quality,
                'average_dust_ppm': average_dust_ppm,
            })

            return Response(serializer.data)

        except Room.DoesNotExist:
            return Response({'message': 'Room not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except Exception as e:
            return Response({'error': str(e)}, status=500)