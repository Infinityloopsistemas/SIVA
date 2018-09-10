# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('denominacion', models.CharField(max_length=50)),
                ('file', models.BinaryField()),
                ('content_type_file', models.CharField(max_length=50)),
                ('object_id', models.PositiveIntegerField()),
                ('lugar', models.CharField(default=b'None', max_length=50)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
