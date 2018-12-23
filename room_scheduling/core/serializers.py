""" modules to serializer models """

from rest_framework import serializers
from .models import Meeting, MeetingRoom


class MeetingRoomSerializer(serializers.ModelSerializer):
    """ Class to Serializer model meeting_room """

    class Meta:
        """ Meta Class """
        model = MeetingRoom
        fields = ('id', 'name', 'place', 'description')


class MeetingSerializer(serializers.ModelSerializer):
    """ Class to Serializer model meeting """

    meeting_room_name = serializers.SerializerMethodField(read_only=True)

    def get_meeting_room_name(self, obj):
        """ return name to meeting_room """
        return obj.meeting_room.name

    class Meta:
        """ meta class """
        model = Meeting
        fields = ('id', 'name', 'meeting_room', 'meeting_room_name', 'start', 'end')

    def validate(self, data):
        """ method to valid data """

        end_data = data.get('end') or self.instance.end
        start_data = data.get('start') or self.instance.start

        if end_data <= start_data:
            raise serializers.ValidationError({
                'end': ['Data de termino deve ser maior que a data de inicio'],
            })

        query = Meeting.objects.filter(
            meeting_room=data.get('meeting_room') or self.instance.meeting_room.id,
            start__gte=start_data, end__lte=end_data
        )
        if self.instance:
            query = query.exclude(pk=self.instance.pk)

        if query.exists():
            raise serializers.ValidationError(
                'Esta sala ja esta reservada para esse horario')

        return data
