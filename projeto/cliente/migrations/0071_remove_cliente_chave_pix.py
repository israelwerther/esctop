# Generated by Django 3.0.7 on 2022-03-15 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0070_auto_20220315_1532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='chave_pix',
        ),
    ]
