# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('maestros', '__first__'),
        ('maestros_generales', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoadDataDevice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fechaalta', models.DateField(auto_now_add=True, verbose_name=b'Fecha Alta', null=True)),
                ('fechabaja', models.DateField(null=True, verbose_name=b'Fecha Baja', blank=True)),
                ('PollCount', models.IntegerField()),
                ('DevicesConnected', models.IntegerField()),
                ('LoopTime', models.DecimalField(max_digits=10, decimal_places=3)),
                ('DevicesConnectedChannel1', models.IntegerField()),
                ('DevicesConnectedChannel2', models.IntegerField()),
                ('DevicesConnectedChannel3', models.IntegerField()),
                ('DataErrorsChannel1', models.IntegerField()),
                ('DataErrorsChannel2', models.IntegerField()),
                ('DataErrorsChannel3', models.IntegerField()),
                ('VoltageChannel1', models.DecimalField(max_digits=10, decimal_places=3)),
                ('VoltageChannel2', models.DecimalField(max_digits=10, decimal_places=3)),
                ('VoltageChannel3', models.DecimalField(max_digits=10, decimal_places=3)),
                ('VoltagePower', models.DecimalField(max_digits=10, decimal_places=3)),
                ('DeviceName', models.CharField(max_length=30)),
                ('HostName', models.CharField(max_length=30)),
                ('MACAddress', models.CharField(max_length=17)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name=b'Empresa', blank=True, to='maestros_generales.Empresas', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LoadDataSensor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=30)),
                ('Family', models.IntegerField()),
                ('ROMId', models.CharField(max_length=30)),
                ('Health', models.IntegerField()),
                ('Channel', models.IntegerField()),
                ('PrimaryValue', models.CharField(max_length=20)),
                ('Temperature', models.DecimalField(max_digits=10, decimal_places=4)),
                ('date', models.DateTimeField(blank=True)),
                ('loadatadevice', models.ForeignKey(to='loaddata.LoadDataDevice')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TrackSondas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=30)),
                ('Family', models.IntegerField()),
                ('ROMId', models.CharField(max_length=30)),
                ('rangoaviso', models.IntegerField(null=True, verbose_name=b'Tiempo de Aviso (min)')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TrackSondasAlarmas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dateaviso', models.DateTimeField()),
                ('valor', models.DecimalField(max_digits=10, decimal_places=4)),
                ('idavisosms', models.CharField(max_length=100, null=True, blank=True)),
                ('tracksonda', models.ForeignKey(to='loaddata.TrackSondas')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TrackTemperaturas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('DeviceName', models.CharField(max_length=30)),
                ('HostName', models.CharField(max_length=30)),
                ('MACAddress', models.CharField(max_length=17)),
                ('fechaalta', models.DateField(auto_now_add=True, verbose_name=b'Fecha Alta', null=True)),
                ('fechabaja', models.DateField(null=True, verbose_name=b'Fecha Baja', blank=True)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name=b'Empresa', blank=True, to='maestros_generales.Empresas', null=True)),
                ('zonas', models.ForeignKey(to='maestros.Zonas')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='tracksondas',
            name='tracktemp',
            field=models.ForeignKey(to='loaddata.TrackTemperaturas'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='loaddatasensor',
            name='tracksonda',
            field=models.ForeignKey(to='loaddata.TrackSondas'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='loaddatadevice',
            name='tracktemp',
            field=models.ForeignKey(to='loaddata.TrackTemperaturas'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='loaddatadevice',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
