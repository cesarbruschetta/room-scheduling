from django.db import models

# Create your models here.


class MeetingRoom(models.Model):
    """ Model to meeting room """

    name = models.CharField("Nome", max_length=255)
    place = models.CharField("Local", max_length=255)
    description = models.TextField("Descrição")

    def __str__(self):
        return "%s - %s" % (self.name, self.place)

    class Meta:
        """ Meta """
        verbose_name = 'Sala de Reunião'
        verbose_name_plural = 'Salas de Reunião'


class Meeting(models.Model):
    """ Model to meeting """

    name = models.CharField("Nome", max_length=255)
    meeting_room = models.ForeignKey(
        'core.MeetingRoom', on_delete=models.CASCADE)
    start = models.DateTimeField('Data de inicio')
    end = models.DateTimeField('Data de termino')

    def __str__(self):
        return "%s - %s (%s-%s)" % (self.name, self.meeting_room,
                                    self.start, self.end)

    class Meta:
        """ Meta """
        verbose_name = 'Reunião'
        verbose_name_plural = 'Reuniões'
        ordering = ('start',)
