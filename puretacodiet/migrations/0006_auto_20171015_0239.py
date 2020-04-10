# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-15 02:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puretacodiet', '0005_planinstancelist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='uom',
        ),
        migrations.AddField(
            model_name='recipeingredient',
            name='uom',
            field=models.CharField(choices=[('OZ', 'Ounce'), ('EA', 'Each')], default='OZ', max_length=2),
        ),
    ]