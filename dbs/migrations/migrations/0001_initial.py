# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import dbs.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(unique=True, max_length=32, verbose_name=b'\xe9\x83\xa8\xe9\x97\xa8')),
                ('Memo', models.CharField(max_length=64, null=True, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=24, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d')),
                ('Euser', models.OneToOneField(verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7ID', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GamePlat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(unique=True, max_length=32, verbose_name=b'\xe6\xb8\xb8\xe6\x88\x8f\xe5\xb9\xb3\xe5\x8f\xb0')),
                ('Memo', models.CharField(max_length=64, null=True, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LogAct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ActName', models.CharField(unique=True, max_length=32, verbose_name=b'\xe4\xba\x8b\xe4\xbb\xb6\xe5\x90\x8d\xe7\xa7\xb0')),
                ('Memo', models.CharField(max_length=64, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('LoginIP', models.IPAddressField(verbose_name=b'\xe7\x99\xbb\xe5\xbd\x95IP')),
                ('ActDateTime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\x93\x8d\xe4\xbd\x9c\xe6\x97\xb6\xe9\x97\xb4', null=True)),
                ('Act', models.ForeignKey(verbose_name=b'\xe5\x8a\xa8\xe4\xbd\x9c', to='dbs.LogAct')),
                ('LoginUser', models.ForeignKey(verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7ID', to='dbs.Employee')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServerPlat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(unique=True, max_length=32, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8\xe5\xb9\xb3\xe5\x8f\xb0')),
                ('Memo', models.CharField(max_length=64, null=True, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Servers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('HostName', models.CharField(default=b'\xe6\x96\xb0\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8', unique=True, max_length=16, verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xba\xe5\x90\x8d')),
                ('LoginUser', models.CharField(default=b'root', max_length=16, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8\xe7\x94\xa8\xe6\x88\xb7')),
                ('Password', models.CharField(default=b'T1H3i5n#', max_length=64, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81')),
                ('Port', dbs.models.IntegerRangeField(default=22, verbose_name=b'SSH\xe7\xab\xaf\xe5\x8f\xa3')),
                ('IP1', models.IPAddressField(verbose_name=b'\xe5\x85\xac\xe7\xbd\x91IP')),
                ('IP2', models.IPAddressField(null=True, verbose_name=b'\xe6\x9c\xac\xe5\x9c\xb0IP', blank=True)),
                ('IP3', models.IPAddressField(null=True, verbose_name=b'IP3', blank=True)),
                ('IP4', models.IPAddressField(null=True, verbose_name=b'IP4', blank=True)),
                ('Status', models.CharField(default=b'RUN', max_length=3, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', choices=[(b'RUN', b'\xe8\xbf\x90\xe8\xa1\x8c\xe4\xb8\xad'), (b'SUP', b'\xe5\xbe\x85\xe5\xae\x9a\xe4\xb8\xad'), (b'CLS', b'\xe5\xb7\xb2\xe5\x85\xb3\xe6\x9c\xba'), (b'DEL', b'\xe5\xb7\xb2\xe5\x88\xa0\xe9\x99\xa4')])),
                ('SID', models.CharField(max_length=16, null=True, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8ID', blank=True)),
                ('Memo', models.CharField(max_length=64, null=True, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True)),
                ('GPlat', models.ForeignKey(verbose_name=b'\xe6\xb8\xb8\xe6\x88\x8f\xe5\xb9\xb3\xe5\x8f\xb0', to='dbs.GamePlat')),
                ('SrvPlat', models.ForeignKey(verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8\xe5\xb9\xb3\xe5\x8f\xb0', to='dbs.ServerPlat')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='employee',
            name='Gplat',
            field=models.ManyToManyField(to='dbs.GamePlat', verbose_name=b'\xe6\xb8\xb8\xe6\x88\x8f\xe5\xb9\xb3\xe5\x8f\xb0'),
            preserve_default=True,
        ),
    ]
