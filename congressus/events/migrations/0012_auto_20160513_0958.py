# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-13 07:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_auto_20160513_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seatlayout',
            name='direction',
            field=models.CharField(choices=[('u', 'Up'), ('l', 'Left'), ('r', 'Right'), ('d', 'Down')], default='d', max_length=2),
        ),
    ]
