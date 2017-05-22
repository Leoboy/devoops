# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dbs', '0007_auto_20151204_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='netpolicy',
            name='Server',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name=b'IP\xe7\xad\x96\xe7\x95\xa5\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8', blank=True, to='dbs.Servers', null=True),
            preserve_default=True,
        ),
    ]
