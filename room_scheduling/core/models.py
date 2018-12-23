""" module to model of meeting and meeting_room """

from django.core.exceptions import ValidationError
from django.db import models


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

    def clean(self):
        """ valide date_start larger end_date """

        if self.end <= self.start:
            raise ValidationError({
                'end': ['Data de termino deve ser maior que a data de inicio'],
            })

    class Meta:
        """ Meta """
        verbose_name = 'Reunião'
        verbose_name_plural = 'Reuniões'
        ordering = ('start',)
