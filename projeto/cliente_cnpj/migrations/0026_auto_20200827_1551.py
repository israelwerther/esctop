# Generated by Django 3.0.7 on 2020-08-27 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente_cnpj', '0025_auto_20200826_0909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente_cnpj',
            name='rep_agencia',
        ),
        migrations.RemoveField(
            model_name='cliente_cnpj',
            name='rep_banco',
        ),
        migrations.RemoveField(
            model_name='cliente_cnpj',
            name='rep_conta',
        ),
        migrations.RemoveField(
            model_name='cliente_cnpj',
            name='rep_obs_bancaria',
        ),
    ]
