# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 14:40
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DietPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
                ('description', models.TextField(help_text='enter information about the recipe')),
                ('quantity', models.DecimalField(decimal_places=2, help_text='Number of Tacos.', max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
                ('photo', models.ImageField(blank=True, upload_to='ingredient_photos')),
                ('uom', models.CharField(choices=[('OZ', 'Ounce')], default='OZ', max_length=2)),
                ('calories', models.DecimalField(decimal_places=2, help_text='Number of calories in this ingredient, per measurement', max_digits=5)),
                ('protein', models.DecimalField(decimal_places=2, help_text='Grams of carbohydrates in this ingredient, per measurement', max_digits=5)),
                ('fat', models.DecimalField(decimal_places=2, help_text='Grams of fat in this ingredient, per measurement', max_digits=5)),
                ('carbohydrates', models.DecimalField(decimal_places=2, help_text='Grams of carbohydrates in this ingredient, per measurement', max_digits=5)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='MealItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='puretacodiet.Meal')),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
                ('description', models.TextField(help_text='enter information about the recipe')),
                ('dietplan', models.ForeignKey(blank='True', null='True', on_delete=django.db.models.deletion.CASCADE, to='puretacodiet.DietPlan')),
                ('meals', models.ManyToManyField(to='puretacodiet.Meal')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
                ('photo', models.ImageField(blank=True, upload_to='recipe_photos')),
                ('info', models.TextField(help_text='enter information about the recipe')),
                ('servings', models.IntegerField(help_text='enter total number of servings')),
                ('weight', models.DecimalField(decimal_places=2, help_text='Total weight of 1 serving, in ounces', max_digits=5)),
                ('calories', models.DecimalField(decimal_places=2, help_text='Number of calories in this recipe, per serving', max_digits=5)),
                ('protein', models.DecimalField(decimal_places=2, help_text='Grams of carbohydrates in this recipe, per serving', max_digits=5)),
                ('fat', models.DecimalField(decimal_places=2, help_text='Grams of fat in this recipe, per serving', max_digits=5)),
                ('carbohydrates', models.DecimalField(decimal_places=2, help_text='Grams of carbohydrates in this recipe, per serving', max_digits=5)),
                ('directions', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['pub_date', 'title'],
            },
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, help_text='Quantity of the ingredient in the amount specified.', max_digits=3)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='puretacodiet.Ingredient')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='puretacodiet.Recipe')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(through='puretacodiet.RecipeIngredient', to='puretacodiet.Ingredient'),
        ),
        migrations.AddField(
            model_name='mealitem',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='puretacodiet.Recipe'),
        ),
        migrations.AddField(
            model_name='meal',
            name='recipes',
            field=models.ManyToManyField(through='puretacodiet.MealItem', to='puretacodiet.Recipe'),
        ),
    ]
