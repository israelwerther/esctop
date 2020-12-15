# Generated by Django 3.0.5 on 2020-05-19 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimo', '0010_auto_20200519_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='valor_emprestado',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True, verbose_name='Valor Emprestado'),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='valor_prestacao',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True, verbose_name='Valor da prestação'),
        ),
    ]
