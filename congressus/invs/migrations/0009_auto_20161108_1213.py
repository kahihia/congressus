# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-08 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invs', '0008_auto_20161103_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitation',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='invitationtype',
            name='one_time_for_session',
            field=models.BooleanField(default=False, help_text='This is used for passes that will be only valid one time for each session. Invitations always have only one use. So this is ignored in invitations.', verbose_name='one time for session'),
        ),
    ]