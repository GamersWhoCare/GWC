# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-25 05:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Collections', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CheckedOutTime', models.DateTimeField(default=django.utils.timezone.now)),
                ('CheckedInTime', models.DateTimeField()),
                ('ModifiedTime', models.DateTimeField(auto_now=True)),
                ('PreConditionNote', models.CharField(max_length=500)),
                ('PostConditionNote', models.CharField(max_length=500)),
                ('PostWeight', models.DecimalField(blank=True, decimal_places=6, max_digits=8, null=True)),
                ('Attendee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Collections.Person')),
            ],
        ),
        migrations.AddField(
            model_name='collection',
            name='AvailableAtEvent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='checkout',
            name='BoardgameFromCollection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Collections.Collection'),
        ),
    ]
