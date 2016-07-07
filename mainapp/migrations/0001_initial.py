# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-02 18:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('content', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('room', models.IntegerField()),
                ('idno', models.CharField(max_length=128)),
                ('hostel', models.CharField(max_length=10)),
                ('sex', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Student'),
        ),
    ]
