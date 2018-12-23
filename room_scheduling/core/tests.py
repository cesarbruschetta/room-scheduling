""" module to test views to api """
from datetime import datetime, timedelta
from rest_framework.test import APITestCase

from .models import MeetingRoom, Meeting


class TestMeetingRoomView(APITestCase):
    """ Teste to register MeetingRoom in API """

    fixtures = ['data_roons.json']

    def test_register_meeting_room(self):
        """ test to method register meeting_room in api """

        data = {
            "name": "Test Sala",
            "place": "Sem lugar",
            "description": "Sala de reuniao de teste"
        }

        resp = self.client.post("/api/meeting-room/", data=data)
        self.assertEqual(resp.status_code, 201)

    def test_edit_meeting_room(self):
        """ test to method edit meeting_room in api """

        meeting_room = MeetingRoom.objects.all()[0]

        data = {
            "name": "Edit name Sala"
        }

        resp = self.client.patch("/api/meeting-room/%s/" % (meeting_room.id), data=data)
        self.assertEqual(resp.status_code, 200)

        meeting_room = MeetingRoom.objects.get(id=meeting_room.id)
        self.assertEqual(meeting_room.name, "Edit name Sala")

    def test_delete_meeting_room(self):
        """ test to method delete meeting_room in api """

        meeting_room = MeetingRoom.objects.all()[0]

        resp = self.client.delete("/api/meeting-room/%s/" % (meeting_room.id))
        self.assertEqual(resp.status_code, 204)

        query = MeetingRoom.objects.filter(id=meeting_room.id)
        self.assertFalse(query.exists())


class TestMeetingView(APITestCase):
    """ Teste to register Meeting in API """

    fixtures = ['data_roons.json']

    def setUp(self):
        """ Set Up test """

        self.meeting_room = MeetingRoom.objects.all()[0]
        self.start = datetime.now().replace(hour=12, minute=0)
        self.end = self.start + timedelta(minutes=30)

    def test_register_meeting(self):
        """ test to method register meeting in api """

        data = {
            "name": "Reunião de Test",
            "meeting_room": self.meeting_room.id,
            "start": self.start,
            "end": self.end
        }

        resp = self.client.post("/api/meeting/", data=data)
        self.assertEqual(resp.status_code, 201)

    def test_edit_meeting(self):
        """ test to method edit meeting in api """

        meeting = Meeting.objects.all()[0]
        data = {
            "name": "Reunião de Test Edit",
        }

        resp = self.client.patch("/api/meeting/%s/" % (meeting.id), data=data)
        self.assertEqual(resp.status_code, 200)

        meeting = Meeting.objects.get(id=meeting.id)
        self.assertEqual(meeting.name, data['name'])

    def test_delete_meeting(self):
        """ test to method delete meeting in api """

        meeting = Meeting.objects.all()[0]

        resp = self.client.delete("/api/meeting/%s/" % (meeting.id))
        self.assertEqual(resp.status_code, 204)

        query = Meeting.objects.filter(id=meeting.id)
        self.assertFalse(query.exists())

    def test_create_meeting_invalid(self):
        """ test to method create invalid meeting in api """

        data = {
            "name": "Reunião de Test Invalid",
            "meeting_room": self.meeting_room.id,
            "start": self.end,
            "end": self.start
        }

        resp = self.client.post("/api/meeting/", data=data)
        self.assertEqual(resp.status_code, 400)

        data = resp.json()
        self.assertIn("Data de termino deve ser maior que a data de inicio", data['end'])

    def test_create_meeting_duplicate(self):
        """ test to method create duplicate meeting in api """

        meeting = Meeting.objects.all()[0]

        data = {
            "name": "Reunião de Test Invalid",
            "meeting_room": self.meeting_room.id,
            "start": meeting.start,
            "end": meeting.end
        }

        resp = self.client.post("/api/meeting/", data=data)
        self.assertEqual(resp.status_code, 400)

        data = resp.json()
        self.assertIn("Esta sala ja esta reservada para esse horario", data['non_field_errors'])


class TestHomePageView(APITestCase):
    """ Teste to HomePage View """

    def test_get_home(self):
        """ test to get home page """

        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)
