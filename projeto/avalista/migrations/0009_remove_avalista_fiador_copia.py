# Generated by Django 3.0.7 on 2020-08-25 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avalista', '0008_delete_teste'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avalista',
            name='fiador_copia',
        ),
    ]
