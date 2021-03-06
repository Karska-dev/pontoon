# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 12:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0085_auto_20170301_0136"),
    ]

    operations = [
        migrations.AlterField(
            model_name="locale",
            name="direction",
            field=models.CharField(
                choices=[(b"ltr", b"left-to-right"), (b"rtl", b"right-to-left")],
                default=b"ltr",
                help_text=b'\n        Writing direction of the script. Set to "right-to-left" if "rtl" value\n        for the locale script is set to "YES" in\n        <a href="https://github.com/unicode-cldr/cldr-core/blob/master/scriptMetadata.json">CLDR scriptMetadata.json</a>.\n        ',
                max_length=3,
            ),
        ),
        migrations.AlterField(
            model_name="locale",
            name="script",
            field=models.CharField(
                default=b"Latin",
                help_text=b'\n        The script used by this locale. Find it in\n        <a href="http://www.unicode.org/cldr/charts/latest/supplemental/languages_and_scripts.html">CLDR Languages and Scripts</a>.\n        ',
                max_length=128,
            ),
        ),
    ]
