# Generated by Django 3.0.7 on 2022-05-22 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimo', '0067_auto_20220521_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='presencial',
            field=models.BooleanField(default=False, verbose_name='Presencial'),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='sequencia',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Sequencia'),
        ),
    ]