# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-15 10:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0020_auto_20160113_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='tshirt',
            name='type',
            field=models.CharField(choices=[('m', 'Male'), ('f', 'Female')], default='m', max_length=3, verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='tshirt',
            name='size',
            field=models.CharField(choices=[('xxs', 'XXS'), ('xs', 'XS'), ('s', 'S'), ('m', 'M'), ('l', 'L'), ('xl', 'XL'), ('xxl', 'XXL')], default='m', max_length=3, verbose_name='size'),
        ),
    ]
