# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dbs', '0010_auto_20151221_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='roles',
            name='Type',
            field=models.CharField(max_length=64, null=True, verbose_name=b'\xe7\xb1\xbb\xe5\x88\xab', blank=True),
            preserve_default=True,
        ),
    ]
