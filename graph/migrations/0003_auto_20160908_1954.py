# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-08 19:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.CharField(max_length=80, primary_key=True, serialize=False),
        ),
    ]