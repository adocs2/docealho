# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-15 22:17
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20161115_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=tinymce.models.HTMLField(),
        ),
    ]
