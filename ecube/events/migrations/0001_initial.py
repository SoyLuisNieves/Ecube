# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-20 01:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sponsors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('img_event', models.ImageField(upload_to='img_events')),
                ('descirption', models.TextField()),
                ('start', models.DateTimeField()),
                ('finish', models.DateTimeField()),
                ('address', models.TextField()),
                ('place', models.CharField(max_length=150)),
                ('categories', models.TextField()),
                ('official', models.BooleanField(default=0)),
                ('sponsor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sponsors.Sponsor')),
            ],
        ),
    ]
