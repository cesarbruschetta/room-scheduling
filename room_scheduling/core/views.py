""" module to views of core """

from django.http import HttpResponse
from django.views import View
from rest_framework import viewsets, filters

from .models import Meeting, MeetingRoom
from .serializers import MeetingRoomSerializer, MeetingSerializer


class MeetingRoomViewSet(viewsets.ModelViewSet):
    """ This viewset from meetroom with provides
        `list`, `detail`, `create` and `delete` actions.
    """

    queryset = MeetingRoom.objects.all()
    serializer_class = MeetingRoomSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class MeetingViewSet(viewsets.ModelViewSet):
    """ This viewset from meeting with provides
        `list`, `detail`, `create` and delete` actions.
    """

    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('meeting_room__name', 'start', 'end')


class HomePage(View):
    """ class to homePage view """

    def get(self, request, *args, **kwargs):
        """ Home page """

        html = """
            <h2>Documentação completa</h2>
            <a href="https://room-scheduling.readthedocs.io/" >Readthedocs</a>

            <h2 id="endpointsparagestaodesalas">End Points Para Gestao de Salas</h2>
            <ul>
                <li><code>GET    /api/meeting-room/</code> - Lista as salas criadas no sistema</li>
                <li><code>GET    /api/meeting-room/?search=termo</code> - Listar as salas criadas,
                filtrando pelo "termo"</li>
                <li><code>POST   /api/meeting-room/</code> - Registrar uma nova sala de reunião</li>
                <li><code>PATCH  /api/meeting-room/:id/</code> - Editar uma sala de reunião existente</li>
                <li><code>DELETE /api/meeting-room/:id/</code> - Remover uma sala de reunião existente</li>
            </ul>
            <h2 id="endpointsparagestaodereservas">End Points Para Gestao de Reservas</h2>
            <ul>
                <li><code>GET    /api/meeting/</code> - Lista as reservas criadas no sistema</li>
                <li><code>GET    /api/meeting/?search=termo</code> - Listar as reservas criadas,
                filtrando pelo "termo"</li>
                <li><code>POST   /api/meeting/</code> - Registrar uma nova reserva</li>
                <li><code>PATCH  /api/meeting/:id/</code> - Editar uma reserva existente</li>
                <li><code>DELETE /api/meeting/:id/</code> - Remover uma reserva existente</li>
            </ul>
        """
        return HttpResponse(html)
