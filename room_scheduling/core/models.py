""" module to model of meeting and meeting_room """

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save, post_delete
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


class ActionLog(models.Model):
    """ Model To action log """
    
    ACTIONS = (
        ('1', 'Criação'),
        ('2', 'Edição'),
        ('3', 'Exclução'),
    )
    
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    action = models.CharField('Status', max_length=2, choices=ACTIONS, default='1')
    creation_date = models.DateTimeField('Data de criação', auto_now_add=True)
    
    def __str__(self):
        return "%s - %s" % (self.content_object, self.action)

    class Meta:
        """ Meta """
        verbose_name = 'Log de Ações'
        verbose_name_plural = 'Logs de Ações'
        
        
def create_action_log(sender, instance=None, created=False, **kwargs):
    """ Method to create log to action in model """
    
    ActionLog.objects.create(content_object=instance, action='1' and created or '2')

def create_action_log_to_remove(sender, instance=None, created=False, **kwargs):
    """ Method to create log to action in model to remove object """
    
    ActionLog.objects.create(content_object=instance, action='3')


post_save.connect(create_action_log, sender=Meeting)
post_save.connect(create_action_log, sender=MeetingRoom)

post_delete.connect(create_action_log_to_remove, sender=Meeting)
post_delete.connect(create_action_log_to_remove, sender=MeetingRoom)
