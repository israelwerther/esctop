# Generated by Django 3.0.7 on 2020-10-08 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimo', '0029_emprestimo_n_de_teste'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprestimo',
            name='n_de_teste',
        ),
    ]
