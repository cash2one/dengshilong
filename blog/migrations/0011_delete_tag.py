# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-17 19:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20160217_1947'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
