# Generated by Django 4.0.3 on 2022-05-31 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreComun', models.CharField(max_length=40)),
                ('nombreCientifico', models.CharField(max_length=50)),
                ('familia', models.CharField(help_text='Arbol, planta, flor, cactacea, etc.', max_length=50)),
                ('sustrato', models.CharField(help_text='Algun tipo de tierra especial?', max_length=50)),
                ('precio', models.IntegerField(help_text='Precio en U$s blue.')),
                ('viveros', models.CharField(help_text='Viveros donde encontrarla.', max_length=100)),
                ('peligrosComunes', models.CharField(help_text='Problemas más usuales.', max_length=100)),
                ('interior', models.BooleanField(help_text='La planta es de interior?.')),
                ('luzDirecta', models.BooleanField(help_text='Necesita luz solar directa?.')),
                ('frecuenciaRiego', models.IntegerField(help_text='Riegos mensuales.')),
                ('descripcion', models.CharField(help_text='Descripcion de la planta.', max_length=3000)),
            ],
        ),
        migrations.CreateModel(
            name='Posteo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('subtitulo', models.CharField(max_length=100)),
                ('fecha', models.DateField(help_text='AAAA/MM/DD')),
                ('texto', models.CharField(max_length=5000)),
                ('autor', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Problema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreProblema', models.CharField(max_length=40)),
                ('nombreCientifico', models.CharField(max_length=50)),
                ('peligro', models.CharField(help_text='Bajo, Medio o Alto', max_length=10)),
                ('productos', models.CharField(help_text='Productos de ayuda.', max_length=50)),
                ('solucion', models.CharField(help_text='Manera de solucionarlo', max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('precio', models.IntegerField(help_text='Precio en U$s blue.')),
                ('solucionaProblemas', models.CharField(help_text='Problemas que soluciona.', max_length=200)),
                ('puntoDeVenta', models.CharField(help_text='Viveros donde comprarlo.', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Vivero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('provincia', models.CharField(max_length=40)),
                ('localidad', models.CharField(max_length=40)),
                ('calle', models.CharField(max_length=40)),
                ('altura', models.CharField(max_length=40)),
                ('telefono', models.IntegerField()),
                ('stockPlantas', models.CharField(help_text='Plantas en stock.', max_length=2000)),
                ('stockProductos', models.CharField(help_text='Productos en stock.', max_length=2000)),
            ],
        ),
    ]
