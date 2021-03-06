# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-21 17:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0019_auto_20160616_1936'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(verbose_name='Start at')),
                ('end', models.DateTimeField(verbose_name='End at')),
                ('used', models.BooleanField(default=False)),
                ('extra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='extra_sessions', to='events.Session')),
                ('orig', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orig_sessions', to='events.Session')),
            ],
        ),
    ]
