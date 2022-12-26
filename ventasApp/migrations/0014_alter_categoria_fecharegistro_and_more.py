# Generated by Django 4.0.4 on 2022-08-27 23:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventasApp', '0013_alter_categoria_fecharegistro_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2022, 8, 27, 18, 58, 58, 840336)),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2022, 8, 27, 18, 58, 58, 839338)),
        ),
        migrations.AlterField(
            model_name='detalledocumentocompra',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2022, 8, 27, 18, 58, 58, 852303)),
        ),
        migrations.AlterField(
            model_name='detalledocumentoventa',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2022, 8, 27, 18, 58, 58, 851306)),
        ),
        migrations.AlterField(
            model_name='detallenotaalmacen',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2022, 8, 27, 18, 58, 58, 850309)),
        ),
        migrations.AlterField(
            model_name='detalleordencompra',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2022, 8, 27, 18, 58, 58, 849311)),
        ),
        migrations.AlterField(
            model_name='detallepedidoventa',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2022, 8, 27, 18, 58, 58, 841333)),
        ),
        migrations.AlterField(
            model_name='documentocompra',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2022, 8, 27, 18, 58, 58, 851306)),
        ),
        migrations.AlterField(
            model_name='documentoventa',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2022, 8, 27, 18, 58, 58, 851306)),
        ),
        migrations.AlterField(
            model_name='formapago',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2022, 8, 27, 18, 58, 58, 839338)),
        ),
        migrations.AlterField(
            model_name='notaalmacen',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2022, 8, 27, 18, 58, 58, 850309)),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2022, 8, 27, 18, 58, 58, 842330)),
        ),
        migrations.AlterField(
            model_name='pedidoventa',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2022, 8, 27, 18, 58, 58, 841333)),
        ),
        migrations.AlterField(
            model_name='producto',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2022, 8, 27, 18, 58, 58, 840336)),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2022, 8, 27, 18, 58, 58, 842330)),
        ),
        migrations.AlterField(
            model_name='tipocliente',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2022, 8, 27, 18, 58, 58, 839338)),
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='fechaRegistro',
            field=models.DateField(default=datetime.datetime(2022, 8, 27, 18, 58, 58, 838341)),
        ),
    ]
