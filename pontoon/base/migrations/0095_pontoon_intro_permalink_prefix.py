# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-28 23:15
from __future__ import unicode_literals

from django.db import migrations


def load_initial_data(apps, schema_editor):
    Project = apps.get_model("base", "Project")
    repository = Project.objects.get(slug="pontoon-intro").repositories.first()

    if not repository.permalink_prefix:
        repository.permalink_prefix = "https://raw.githubusercontent.com/mozilla/pontoon-intro/master/static/locales/{locale_code}"
        repository.save()


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0094_improve_calculate_stats_performance"),
    ]

    operations = [
        migrations.RunPython(load_initial_data, migrations.RunPython.noop),
    ]
