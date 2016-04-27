# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 10:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0021_auto_20160115_1154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='confirmemail',
            name='event',
        ),
        migrations.RemoveField(
            model_name='emailattachment',
            name='email',
        ),
        migrations.RemoveField(
            model_name='invcode',
            name='event',
        ),
        migrations.AlterField(
            model_name='ticket',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='events.Event'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='inv',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.InvCode'),
        ),
        migrations.DeleteModel(
            name='ConfirmEmail',
        ),
        migrations.DeleteModel(
            name='EmailAttachment',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='InvCode',
        ),
    ]
