# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import private_files.models.fields
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('maestros', '__first__'),
        ('maestros_generales', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockActual',
            fields=[
                ('id', models.IntegerField(serialize=False, verbose_name='Lote id', primary_key=True)),
                ('referencia', models.TextField(verbose_name='REF. Lote')),
                ('producto_id', models.IntegerField(verbose_name='Producto id')),
                ('producto', models.TextField(verbose_name='Producto')),
                ('fechacaducidad', models.DateField(help_text=b'Fecha caducidad', verbose_name='Fecha Caducidad')),
                ('empresa_id', models.IntegerField(verbose_name='Empresa id')),
                ('empresa', models.TextField(verbose_name='Nombre empresa')),
                ('cant', models.IntegerField(null=True, verbose_name='Cantidad', blank=True)),
                ('peso', models.DecimalField(null=True, verbose_name='Peso', max_digits=10, decimal_places=2, blank=True)),
            ],
            options={
                'db_table': 'trazabilidad_stockactual',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Albaran',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fechaalta', models.DateField(verbose_name='Fecha Alta')),
                ('fechabaja', models.DateField(null=True, verbose_name='Fecha Baja', blank=True)),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('referencia', models.CharField(max_length=50, verbose_name='Num.Alba, S/Ref')),
                ('observaciones', models.TextField(null=True, verbose_name='Observaciones', blank=True)),
                ('fecha_cierre', models.DateField(null=True, verbose_name='Fecha Cierre', blank=True)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Empresa', blank=True, to='maestros_generales.Empresas', null=True)),
                ('proveedor', models.ForeignKey(verbose_name='Proveedor', to='maestros.Terceros', null=True)),
                ('tpdoc', models.ForeignKey(verbose_name='Tipo de Documento', to='maestros_generales.TiposDocumentos')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=django.db.models.deletion.PROTECT)),
            ],
            options={
                'verbose_name': 'Albaran',
                'verbose_name_plural': 'Albaranes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DetalleAlbaran',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fechaalta', models.DateField(verbose_name='Fecha Alta')),
                ('fechabaja', models.DateField(null=True, verbose_name='Fecha Baja', blank=True)),
                ('referencia', models.CharField(max_length=50, null=True, verbose_name='Ref.', blank=True)),
                ('cantidad', models.IntegerField(null=True, verbose_name='Cantidad', blank=True)),
                ('peso', models.DecimalField(null=True, verbose_name='Peso', max_digits=10, decimal_places=2, blank=True)),
                ('volumen', models.DecimalField(null=True, verbose_name='Volumen', max_digits=10, decimal_places=2, blank=True)),
                ('pesobulto', models.DecimalField(null=True, verbose_name='Peso/Bulto', max_digits=10, decimal_places=2, blank=True)),
                ('albaran', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Albaran', to='trazabilidad.Albaran')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Empresa', blank=True, to='maestros_generales.Empresas', null=True)),
            ],
            options={
                'verbose_name': 'Detalle Lote',
                'verbose_name_plural': 'Detalles Lotes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Documentos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('denominacion', models.CharField(max_length=b'200', verbose_name='Denominaci\xf3n')),
                ('contenido', models.TextField(null=True, blank=True)),
                ('archivos', private_files.models.fields.PrivateFileField(help_text='Tama\xf1o maximo 2.5 MB', upload_to=b'trazabilidad', null=True, verbose_name=b'file', blank=True)),
                ('fechaproceso', models.DateField(null=True, verbose_name=b'Fecha de Proceso conversion', blank=True)),
                ('nodescargas', models.PositiveIntegerField(default=0, null=True, verbose_name=b'total descargas', blank=True)),
                ('albaran', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Albaran', blank=True, to='trazabilidad.Albaran', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lotes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fechaalta', models.DateField(verbose_name='Fecha Alta')),
                ('fechabaja', models.DateField(null=True, verbose_name='Fecha Baja', blank=True)),
                ('referencia', models.CharField(max_length=50, null=True, verbose_name='Referencia Lote', blank=True)),
                ('fechacaducidad', models.DateField(help_text=b'Fecha caducidad', verbose_name='Fecha Caducidad')),
                ('templote', models.CharField(max_length=10, null=True, verbose_name='Temp.Lote', blank=True)),
                ('carorganolep', models.CharField(max_length=200, null=True, verbose_name='Organolepticas', blank=True)),
                ('observaciones', models.TextField(null=True, verbose_name='Observaciones', blank=True)),
                ('cantidad', models.IntegerField(null=True, verbose_name='Unidades', blank=True)),
                ('peso', models.DecimalField(null=True, verbose_name='Peso', max_digits=10, decimal_places=2, blank=True)),
                ('volumen', models.DecimalField(null=True, verbose_name='Volumen', max_digits=10, decimal_places=2, blank=True)),
                ('pesobulto', models.DecimalField(null=True, verbose_name='Peso/Unidad', max_digits=10, decimal_places=2, blank=True)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Empresa', blank=True, to='maestros_generales.Empresas', null=True)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Producto', blank=True, to='productos.Productos', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=django.db.models.deletion.PROTECT)),
            ],
            options={
                'verbose_name': 'Lote',
                'verbose_name_plural': 'Lotes',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='documentos',
            name='lotes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Lotes', blank=True, to='trazabilidad.Lotes', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detallealbaran',
            name='lote',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Lote', to='trazabilidad.Lotes'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detallealbaran',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Producto', to='productos.Productos'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detallealbaran',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=django.db.models.deletion.PROTECT),
            preserve_default=True,
        ),
    ]
