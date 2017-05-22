# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dbs', '0003_auto_20151201_1433'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='netpolicy',
            name='ApplyNum',
        ),
    ]
