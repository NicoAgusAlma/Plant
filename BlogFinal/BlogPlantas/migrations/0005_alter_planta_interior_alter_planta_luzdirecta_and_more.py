# Generated by Django 4.0.3 on 2022-06-04 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogPlantas', '0004_alter_posteo_autor_alter_vivero_stockplantas_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planta',
            name='interior',
            field=models.BooleanField(default=True, verbose_name='interior'),
        ),
        migrations.AlterField(
            model_name='planta',
            name='luzDirecta',
            field=models.BooleanField(default=False, help_text='Necesita luz solar directa?.'),
        ),
        migrations.AlterField(
            model_name='posteo',
            name='autor',
            field=models.CharField(default='Anonimo', max_length=100),
        ),
    ]
