# Generated by Django 3.0.6 on 2020-06-07 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0027_cliente_ibge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='ibge',
        ),
    ]
