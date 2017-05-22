# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dbs', '0004_remove_netpolicy_applynum'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='netpolicy',
            unique_together=set([('Weight', 'Server')]),
        ),
    ]
