# Generated by Django 3.0.5 on 2020-05-11 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimo', '0003_emprestimo_data_emprestimo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='data_emprestimo',
            field=models.DateField(blank=True, verbose_name='Data do Emprestimo'),
        ),
    ]