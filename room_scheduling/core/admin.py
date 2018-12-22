from django.contrib import admin

from .models import MeetingRoom

# Register your models here.


@admin.register(MeetingRoom)
class MeetingRoomAdmin(admin.ModelAdmin):
    """ Admin class to MeetingRoom """

    list_display = ("name", 'place', 'description')
    search_fields = ['name', 'place']
