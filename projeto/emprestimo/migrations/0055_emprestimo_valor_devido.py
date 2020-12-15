# Generated by Django 3.0.7 on 2020-11-13 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimo', '0054_emprestimo_iof_real'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprestimo',
            name='valor_devido',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Valor devido'),
        ),
    ]