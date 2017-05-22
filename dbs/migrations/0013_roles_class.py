# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dbs', '0012_auto_20151223_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='roles',
            name='Class',
            field=models.CharField(max_length=64, null=True, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb', blank=True),
            preserve_default=True,
        ),
    ]
