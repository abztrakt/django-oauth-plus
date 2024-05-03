# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("oauth_provider", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="Consumer",
            name="user",
        ),
        migrations.RemoveField(
            model_name="Token",
            name="user",
        ),
    ]
