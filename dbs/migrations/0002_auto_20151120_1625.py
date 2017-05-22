# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dbs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servers',
            name='DetailStatus',
            field=models.TextField(null=True, verbose_name=b'\xe8\xaf\xa6\xe7\xbb\x86\xe7\x8a\xb6\xe6\x80\x81', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='servers',
            name='IP1',
            field=models.IPAddressField(null=True, verbose_name=b'\xe5\x85\xac\xe7\xbd\x91IP', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='servers',
            name='IP2',
            field=models.IPAddressField(default=1, verbose_name=b'\xe6\x9c\xac\xe5\x9c\xb0IP'),
            preserve_default=False,
        ),
    ]
