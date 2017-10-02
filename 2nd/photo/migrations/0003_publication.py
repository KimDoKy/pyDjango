# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-01 11:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_auto_20170922_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('albums', models.ManyToManyField(to='photo.Album')),
            ],
        ),
    ]
