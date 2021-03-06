# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-22 14:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0020_extrasession'),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='name')),
                ('header', models.ImageField(blank=True, null=True, upload_to='templheader', verbose_name='header')),
                ('sponsors', models.ImageField(blank=True, null=True, upload_to='templsponsors', verbose_name='sponsors')),
                ('contributors', models.ImageField(blank=True, null=True, upload_to='templcontributors', verbose_name='contributors')),
                ('links', models.CharField(blank=True, max_length=200, null=True, verbose_name='links')),
                ('info', models.TextField(blank=True, null=True, verbose_name='info text')),
            ],
        ),
    ]
