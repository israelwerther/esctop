# Generated by Django 3.0.7 on 2022-05-24 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimo', '0066_auto_20220521_2050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprestimo',
            name='sequencia',
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='presencial',
            field=models.BooleanField(default=False, verbose_name='Presencial'),
        ),
    ]