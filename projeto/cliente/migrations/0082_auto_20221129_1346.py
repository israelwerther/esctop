# Generated by Django 3.0.7 on 2022-11-29 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0081_auto_20221129_1123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='identification_document',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='proof_of_address',
        ),
    ]