# Generated by Django 3.0.7 on 2020-09-29 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avalista', '0024_avalista_fiador_naturalidade'),
    ]

    operations = [
        migrations.AddField(
            model_name='avalista',
            name='fiador_data_nasc',
            field=models.DateField(max_length=8, null=True, verbose_name='Data de Nascimento'),
        ),
    ]