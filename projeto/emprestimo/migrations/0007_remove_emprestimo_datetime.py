# Generated by Django 3.0.5 on 2020-05-14 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimo', '0006_emprestimo_datetime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprestimo',
            name='datetime',
        ),
    ]
