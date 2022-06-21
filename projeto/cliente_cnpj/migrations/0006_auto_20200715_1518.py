# Generated by Django 3.0.6 on 2020-07-15 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente_cnpj', '0005_auto_20200715_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente_cnpj',
            name='agencia',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Agência'),
        ),
        migrations.AddField(
            model_name='cliente_cnpj',
            name='banco',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Banco'),
        ),
        migrations.AddField(
            model_name='cliente_cnpj',
            name='celular1',
            field=models.CharField(blank=True, max_length=17, null=True, verbose_name='celular 1'),
        ),
        migrations.AddField(
            model_name='cliente_cnpj',
            name='celular2',
            field=models.CharField(blank=True, max_length=17, null=True, verbose_name='celular 2'),
        ),
        migrations.AddField(
            model_name='cliente_cnpj',
            name='conta',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Conta'),
        ),
        migrations.AddField(
            model_name='cliente_cnpj',
            name='contato1',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Contato 1'),
        ),
        migrations.AddField(
            model_name='cliente_cnpj',
            name='contato2',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Contato 2'),
        ),
        migrations.AddField(
            model_name='cliente_cnpj',
            name='obs_bancaria',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Observações'),
        ),
    ]
