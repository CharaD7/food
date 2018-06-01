# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-09 06:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='calories',
            field=models.DecimalField(decimal_places=0, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]