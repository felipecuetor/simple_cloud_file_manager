# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-04 17:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_manager_v1', '0005_tag_tag_importance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='id',
        ),
        migrations.AddField(
            model_name='file',
            name='file_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]