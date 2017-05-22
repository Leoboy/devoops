# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dbs', '0008_auto_20151209_1506'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=24, verbose_name=b'\xe8\xa7\x92\xe8\x89\xb2\xe5\x90\x8d')),
                ('DPath', models.CharField(max_length=64, null=True, verbose_name=b'\xe6\x96\x87\xe4\xbb\xb6\xe7\x9b\xae\xe6\xa0\x87\xe8\xb7\xaf\xe5\xbe\x84', blank=True)),
                ('ExeCom', models.CharField(max_length=64, null=True, verbose_name=b'\xe5\x91\xbd\xe4\xbb\xa4', blank=True)),
                ('SPath', models.CharField(max_length=64, null=True, verbose_name=b'\xe6\x96\x87\xe4\xbb\xb6\xe6\xba\x90\xe8\xb7\xaf\xe5\xbe\x84', blank=True)),
                ('File', models.CharField(max_length=64, null=True, verbose_name=b'\xe6\x96\x87\xe4\xbb\xb6', blank=True)),
                ('AsRoot', models.BooleanField(default=False, verbose_name=b'Root')),
                ('Memo', models.CharField(max_length=64, null=True, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True)),
                ('DHost', models.ForeignKey(related_name='dset', verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8\xe8\xa7\x92\xe8\x89\xb2', to='dbs.Servers')),
                ('GPlat', models.ForeignKey(verbose_name=b'\xe6\xb8\xb8\xe6\x88\x8f\xe5\xb9\xb3\xe5\x8f\xb0', to='dbs.GamePlat')),
                ('SHost', models.ForeignKey(related_name='sset', verbose_name=b'\xe6\x96\x87\xe4\xbb\xb6\xe6\xba\x90\xe4\xb8\xbb\xe6\x9c\xba', blank=True, to='dbs.Servers', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='logs',
            name='Act',
        ),
        migrations.RemoveField(
            model_name='logs',
            name='LoginIP',
        ),
        migrations.RemoveField(
            model_name='logs',
            name='LoginUser',
        ),
        migrations.AddField(
            model_name='logs',
            name='ActConnect',
            field=models.TextField(null=True, verbose_name=b'\xe6\x93\x8d\xe4\xbd\x9c\xe5\x86\x85\xe5\xae\xb9', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='logs',
            name='ActIP',
            field=models.IPAddressField(default=1, verbose_name=b'\xe7\x99\xbb\xe5\xbd\x95IP'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logs',
            name='ActMethod',
            field=models.CharField(default=1, max_length=24, verbose_name=b'\xe6\x93\x8d\xe4\xbd\x9c\xe6\x96\xb9\xe6\xb3\x95'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logs',
            name='ActPlat',
            field=models.CharField(default=1, max_length=128, verbose_name=b'\xe6\x93\x8d\xe4\xbd\x9c\xe5\xb9\xb3\xe5\x8f\xb0'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logs',
            name='ActUser',
            field=models.CharField(max_length=128, null=True, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7ID', blank=True),
            preserve_default=True,
        ),
    ]
