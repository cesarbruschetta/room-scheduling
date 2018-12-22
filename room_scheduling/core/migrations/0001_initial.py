# Generated by Django 2.1.4 on 2018-12-22 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('start', models.DateTimeField(verbose_name='Data de inicio')),
                ('end', models.DateTimeField(verbose_name='Data de termino')),
            ],
            options={
                'verbose_name': 'Reunião',
                'verbose_name_plural': 'Reuniões',
                'ordering': ('start',),
            },
        ),
        migrations.CreateModel(
            name='MeetingRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('place', models.CharField(max_length=255, verbose_name='Local')),
                ('description', models.TextField(verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Sala de Reunião',
                'verbose_name_plural': 'Salas de Reunião',
            },
        ),
        migrations.AddField(
            model_name='meeting',
            name='meeting_room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.MeetingRoom'),
        ),
    ]
