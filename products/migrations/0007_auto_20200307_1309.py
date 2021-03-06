# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-03-07 13:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20200307_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='base_repro_fee',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='size',
            name='longer_side',
            field=models.DecimalField(decimal_places=2, default=15, max_digits=6),
        ),
        migrations.AlterField(
            model_name='size',
            name='shorter_side',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=6),
        ),
    ]
