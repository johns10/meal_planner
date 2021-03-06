# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 19:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puretacodiet', '0002_mealinstance_planinstance'),
    ]

    operations = [
        migrations.AddField(
            model_name='mealitem',
            name='quantity',
            field=models.DecimalField(decimal_places=1, default=1, help_text='Number of servings of this taco in the recipe.', max_digits=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='uom',
            field=models.CharField(choices=[('OZ', 'Ounce'), ('EA', 'Each')], default='OZ', max_length=2),
        ),
    ]
