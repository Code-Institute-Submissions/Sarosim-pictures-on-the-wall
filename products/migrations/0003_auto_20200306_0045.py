# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-03-06 00:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200305_2328'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
            ],
        ),
        migrations.CreateModel(
            name='Technologies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('technology_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='artist',
            name='address',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='product',
            name='artist',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='products.Artist'),
        ),
        migrations.AddField(
            model_name='product',
            name='date_uploaded',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='product',
            name='max_print_size',
            field=models.CharField(default='', max_length=16),
        ),
        migrations.AddField(
            model_name='product',
            name='num_of_orders',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='num_of_views',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default='other', on_delete=django.db.models.deletion.CASCADE, to='products.Category'),
        ),
        migrations.AddField(
            model_name='rating',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
        migrations.AddField(
            model_name='product',
            name='available_technologies',
            field=models.ManyToManyField(to='products.Technologies'),
        ),
    ]