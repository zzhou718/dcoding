# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-06 23:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dcoding', '0011_auto_20180404_1734'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='a_access_from',
        ),
    ]
