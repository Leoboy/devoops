# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dbs', '0005_auto_20151201_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='netpolicy',
            name='Ports',
            field=models.CharField(max_length=255, null=True, verbose_name=b'\xe7\xab\xaf\xe5\x8f\xa3\xe5\x88\x97\xe8\xa1\xa8', blank=True),
            preserve_default=True,
        ),
    ]
