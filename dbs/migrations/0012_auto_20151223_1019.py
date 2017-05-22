# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dbs', '0011_roles_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roles',
            name='File',
            field=models.CharField(max_length=255, null=True, verbose_name=b'\xe6\x96\x87\xe4\xbb\xb6/\xe5\x8f\x82\xe6\x95\xb0', blank=True),
            preserve_default=True,
        ),
    ]
