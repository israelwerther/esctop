# Generated by Django 3.0.7 on 2020-10-16 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente_cnpj', '0045_auto_20201015_0754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente_cnpj',
            name='nome_fantasia',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Nome Fantasia'),
        ),
        migrations.AlterField(
            model_name='cliente_cnpj',
            name='rep_contato1',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Tel Fixo'),
        ),
    ]
