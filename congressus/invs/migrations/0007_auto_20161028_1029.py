# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-28 08:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0037_session_dateformat'),
        ('invs', '0006_invitationgenerator_seats'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitationtype',
            name='template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.TicketTemplate', verbose_name='template'),
        ),
        migrations.AddField(
            model_name='invitationtype',
            name='thermal_template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.ThermalTicketTemplate', verbose_name='thermal template'),
        ),
    ]