# Generated by Django 3.0.7 on 2021-09-26 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avalista', '0027_auto_20210219_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avalista',
            name='fiador_naturalidade',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Naturalidade'),
        ),
        migrations.AlterField(
            model_name='avalista',
            name='fiador_rg',
            field=models.CharField(max_length=20, null=True, verbose_name='RG'),
        ),
    ]