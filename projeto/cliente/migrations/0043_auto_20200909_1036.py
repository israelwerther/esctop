# Generated by Django 3.0.7 on 2020-09-09 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0042_cliente_complemento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='uf',
            field=models.CharField(max_length=2, null=True, verbose_name='UF'),
        ),
    ]