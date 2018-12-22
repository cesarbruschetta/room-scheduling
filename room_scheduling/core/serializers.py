
from rest_framework import serializers
from .models import Meeting, MeetingRoom


class MeetingRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingRoom
        fields = ('id', 'name', 'place', 'description')


class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = ('id', 'name', 'meeting_room', 'start', 'end')
