# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-07 09:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0131_translation_active_populate"),
    ]

    operations = [
        migrations.AddField(
            model_name="locale",
            name="strings_with_errors",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="locale",
            name="strings_with_warnings",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="project",
            name="strings_with_errors",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="project",
            name="strings_with_warnings",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="projectlocale",
            name="strings_with_errors",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="projectlocale",
            name="strings_with_warnings",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="translatedresource",
            name="strings_with_errors",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="translatedresource",
            name="strings_with_warnings",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
