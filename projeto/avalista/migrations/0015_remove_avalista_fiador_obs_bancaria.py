# Generated by Django 3.0.7 on 2020-09-09 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avalista', '0014_auto_20200909_1133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avalista',
            name='fiador_obs_bancaria',
        ),
    ]
