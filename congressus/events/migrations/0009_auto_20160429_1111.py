# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-29 09:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_ticketfield_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticketfield',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='ticketfield',
            name='required',
            field=models.BooleanField(default=False),
        ),
    ]
