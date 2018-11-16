# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-16 17:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_manager_v1', '0007_auto_20181113_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson_concept',
            name='concept_id_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='lesson_concept',
            name='concept_uri',
        ),
        migrations.AlterUniqueTogether(
            name='lesson_concept',
            unique_together=set([('lesson_id_number', 'concept_id_number')]),
        ),
    ]
