# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dbs', '0006_auto_20151201_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='netpolicy',
            name='Policystat',
            field=models.TextField(null=True, verbose_name=b'\xe5\x8d\x8f\xe8\xae\xae\xe7\x8a\xb6\xe6\x80\x81', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='netpolicy',
            name='Ports',
            field=models.TextField(null=True, verbose_name=b'\xe7\xab\xaf\xe5\x8f\xa3\xe5\x88\x97\xe8\xa1\xa8', blank=True),
            preserve_default=True,
        ),
    ]
