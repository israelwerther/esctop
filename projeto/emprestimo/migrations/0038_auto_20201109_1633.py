# Generated by Django 3.0.7 on 2020-11-09 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimo', '0037_emprestimo_valor_mutuado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='valor_prestacao',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Valor da parcela'),
        ),
    ]
