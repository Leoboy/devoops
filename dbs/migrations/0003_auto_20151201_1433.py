# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dbs', '0002_auto_20151120_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='IpGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=24, verbose_name=b'IP\xe7\xbb\x84\xe5\x90\x8d')),
                ('IP', models.TextField(null=True, verbose_name=b'IP\xe5\x9c\xb0\xe5\x9d\x80', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Netpolicy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Weight', models.IntegerField(verbose_name=b'\xe7\xad\x96\xe7\x95\xa5\xe6\x9d\x83\xe9\x87\x8d')),
                ('Chains', models.CharField(default=b'INPUT', max_length=16, verbose_name=b'\xe9\x93\xbe\xe8\xa1\xa8', choices=[(b'INPUT', b'INPUT'), (b'OUTPUT', b'OUTPUT'), (b'FORWARD', b'FORWARD'), (b'PREROUTING', b'PREROUTING'), (b'POSTROUTING', b'POSTROUTING')])),
                ('Protocol', models.CharField(max_length=16, verbose_name=b'\xe7\xbd\x91\xe7\xbb\x9c\xe5\x8d\x8f\xe8\xae\xae')),
                ('Ports', models.CharField(max_length=255, verbose_name=b'\xe7\xab\xaf\xe5\x8f\xa3\xe5\x88\x97\xe8\xa1\xa8')),
                ('Active', models.CharField(max_length=6, verbose_name=b'\xe7\xad\x96\xe7\x95\xa5\xe5\x8a\xa8\xe4\xbd\x9c', choices=[(b'ACCEPT', b'ACCEPT'), (b'DROP', b'DROP'), (b'REJECT', b'REJECT'), (b'LOG', b'LOG')])),
                ('ApplyNum', models.IntegerField(default=0, verbose_name=b'\xe7\xad\x96\xe7\x95\xa5\xe7\x94\x9f\xe6\x95\x88\xe6\xac\xa1\xe6\x95\xb0')),
                ('IpGroupName', models.ForeignKey(verbose_name=b'IP\xe7\xbb\x84', to='dbs.IpGroup')),
                ('Server', models.ForeignKey(verbose_name=b'IP\xe7\xad\x96\xe7\x95\xa5\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8', to='dbs.Servers')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='netpolicy',
            unique_together=set([('Weight', 'Chains', 'Server')]),
        ),
    ]
