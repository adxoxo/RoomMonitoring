from django.urls import path
from .views import RoomParametersView
urlpatterns = [
    path('roomparameters/<int:room_id>/', RoomParametersView.as_view({
        'get':'RoomParametersGet'
    }))
]