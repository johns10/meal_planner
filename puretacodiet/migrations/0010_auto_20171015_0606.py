# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-15 06:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('puretacodiet', '0009_userprofile_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='mobilephome',
            new_name='mobilephone',
        ),
    ]
