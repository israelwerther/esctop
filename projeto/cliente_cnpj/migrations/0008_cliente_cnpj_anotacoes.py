# Generated by Django 3.0.7 on 2020-07-21 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente_cnpj', '0007_cliente_cnpj_representante'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente_cnpj',
            name='anotacoes',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='Anotações'),
        ),
    ]
