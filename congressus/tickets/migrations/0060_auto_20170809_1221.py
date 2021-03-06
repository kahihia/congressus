# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-09 10:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0059_auto_20170809_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multipurchase',
            name='payment_method',
            field=models.CharField(blank=True, choices=[('tpv', 'TPV'), ('paypal', 'Paypal'), ('stripe', 'Stripe'), ('twcash', 'Cash, Ticket Window'), ('twtpv', 'TPV, Ticket Window')], max_length=10, null=True, verbose_name='payment method'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='payment_method',
            field=models.CharField(blank=True, choices=[('tpv', 'TPV'), ('paypal', 'Paypal'), ('stripe', 'Stripe'), ('twcash', 'Cash, Ticket Window'), ('twtpv', 'TPV, Ticket Window')], max_length=10, null=True, verbose_name='payment method'),
        ),
    ]
