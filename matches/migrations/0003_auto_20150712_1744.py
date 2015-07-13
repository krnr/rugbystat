# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0002_auto_20150712_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='link',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='team',
            name='logo',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
