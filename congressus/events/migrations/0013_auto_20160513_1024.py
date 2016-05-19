# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-13 08:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_auto_20160513_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='seatmap',
            name='scene_bottom',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='seatmap',
            name='scene_left',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='seatmap',
            name='scene_right',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='seatmap',
            name='scene_top',
            field=models.IntegerField(default=0),
        ),
    ]