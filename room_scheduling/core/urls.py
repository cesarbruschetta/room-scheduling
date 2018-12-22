from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import MeetingRoomViewSet, MeetingViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'meeting-room', MeetingRoomViewSet)
router.register(r'meeting', MeetingViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
