# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dbs', '0009_auto_20151221_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roles',
            name='AsRoot',
            field=models.BooleanField(default=False, verbose_name=b'AsRoot'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='roles',
            name='DHost',
            field=models.ForeignKey(related_name='dset', blank=True, to='dbs.Servers', max_length=64, null=True, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8\xe8\xa7\x92\xe8\x89\xb2'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='roles',
            name='Name',
            field=models.CharField(unique=True, max_length=24, verbose_name=b'\xe8\xa7\x92\xe8\x89\xb2\xe5\x90\x8d'),
            preserve_default=True,
        ),
    ]
