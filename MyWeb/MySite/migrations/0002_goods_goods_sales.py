# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-05-16 12:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MySite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='goods_sales',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
