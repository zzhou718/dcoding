# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-26 05:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dcoding', '0003_auto_20180226_0000'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='question_id',
            new_name='question',
        ),
    ]
