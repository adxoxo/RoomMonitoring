from django.urls import path
from .views import RoomListedView, RoomUnlistedView, RoomParametersView
urlpatterns = [
    path('roomparameters/<int:room_id>/', RoomParametersView.as_view({
        'get':'RoomParametersGet'
    })),

    path('unlistedrooms', RoomUnlistedView.as_view({
        'get':'RoomsUnlisted'
    })),

    path('listedrooms', RoomListedView.as_view({
        'get':'RoomsListed'
    }))
]