# Generated by Django 3.0.7 on 2022-05-21 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimo', '0064_emprestimo_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='presencial',
            field=models.BooleanField(default=True, verbose_name='Presencial'),
        ),
    ]