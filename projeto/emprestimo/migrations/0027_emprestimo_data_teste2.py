# Generated by Django 3.0.7 on 2020-10-05 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimo', '0026_emprestimo_data_teste'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprestimo',
            name='data_teste2',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Data Teste 2'),
        ),
    ]
