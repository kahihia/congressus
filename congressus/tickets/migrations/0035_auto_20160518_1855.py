# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-18 16:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_auto_20160513_1024'),
        ('tickets', '0034_auto_20160518_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='seat',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='seat_layout',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='events.SeatLayout'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='seat_layout_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
