# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-01 01:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0002_logaccesscontrol'),
    ]

    operations = [
        migrations.AddField(
            model_name='logaccesscontrol',
            name='status',
            field=models.CharField(choices=[('ok', 'ok'), ('wrong', 'wrong'), ('used', 'used'), ('maybe', 'maybe')], default='ok', max_length=10),
        ),
    ]
