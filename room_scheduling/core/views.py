from django.shortcuts import render
from rest_framework import viewsets, filters

from .models import Meeting, MeetingRoom
from .serializers import MeetingRoomSerializer, MeetingSerializer

# Create your views here.


class MeetingRoomViewSet(viewsets.ModelViewSet):
    """
    This viewset from meetroom with provides
    `list`, `detail`, `create` and `delete` actions.
    """

    queryset = MeetingRoom.objects.all()
    serializer_class = MeetingRoomSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class MeetingViewSet(viewsets.ModelViewSet):
    """
    This viewset from meeting with provides
    `list`, `detail`, `create` and `delete` actions.
    """

    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('meeting_room__name',)
