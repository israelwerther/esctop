# Generated by Django 3.0.7 on 2020-07-23 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente_cnpj', '0015_auto_20200722_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente_cnpj',
            name='celular1',
            field=models.CharField(blank=True, max_length=17, null=True, verbose_name='Celular 1'),
        ),
        migrations.AlterField(
            model_name='cliente_cnpj',
            name='celular2',
            field=models.CharField(blank=True, max_length=17, null=True, verbose_name='Celular 2'),
        ),
    ]