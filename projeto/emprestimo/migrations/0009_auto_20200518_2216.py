# Generated by Django 3.0.5 on 2020-05-18 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimo', '0008_auto_20200516_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='valor_emprestado',
            field=models.FloatField(blank=True, null=True, verbose_name='Valor Emprestado'),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='valor_prestacao',
            field=models.FloatField(blank=True, null=True, verbose_name='Valor da prestação'),
        ),
    ]