# Generated by Django 3.0.7 on 2022-05-24 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimo', '0068_auto_20220522_1157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprestimo',
            name='sequencia',
        ),
    ]
