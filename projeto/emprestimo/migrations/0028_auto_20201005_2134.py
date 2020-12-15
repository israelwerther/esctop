# Generated by Django 3.0.7 on 2020-10-05 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimo', '0027_emprestimo_data_teste2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprestimo',
            name='data_teste',
        ),
        migrations.RemoveField(
            model_name='emprestimo',
            name='data_teste2',
        ),
        migrations.AddField(
            model_name='emprestimo',
            name='dt_teste',
            field=models.DateField(blank=True, null=True, verbose_name='Data do Empréstimo'),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='data_emprestimo',
            field=models.DateField(blank=True, null=True, verbose_name='Data do Empréstimo antigo'),
        ),
    ]