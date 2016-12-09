# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-09 11:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=300)),
                ('requester', models.CharField(max_length=100)),
                ('assignee', models.CharField(max_length=100)),
                ('ticket_type', models.CharField(max_length=50)),
                ('priority', models.CharField(max_length=50)),
                ('tags', models.CharField(max_length=300)),
            ],
        ),
    ]
