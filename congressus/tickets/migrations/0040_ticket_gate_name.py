# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-16 17:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0039_ticket_sold_in_window'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='gate_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
