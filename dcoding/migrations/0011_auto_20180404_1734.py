# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-04 21:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dcoding', '0010_auto_20180403_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='t_answering',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='t_thinking',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
