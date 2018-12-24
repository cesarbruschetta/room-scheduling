""" Admin Core """
from django.contrib import admin

from .models import MeetingRoom, Meeting, ActionLog


@admin.register(MeetingRoom)
class MeetingRoomAdmin(admin.ModelAdmin):
    """ Admin class to MeetingRoom """

    list_display = ("name", 'place', 'description')
    search_fields = ['name', 'place']


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    """ Admin class to Meeting """

    list_display = ("name", 'meeting_room', 'start', 'end')
    search_fields = ['name', 'meeting_room__name']


@admin.register(ActionLog)
class ActionLogAdmin(admin.ModelAdmin):
    """ Admin class to ActionLog """

    list_display = ("content_object", 'action', 'creation_date')
    
    def has_change_permission(self, request, obj=None):
        return False
        
    def has_delete_permission(self, request, obj=None):
        return False
    