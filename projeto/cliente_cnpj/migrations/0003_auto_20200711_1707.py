# Generated by Django 3.0.7 on 2020-07-11 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente_cnpj', '0002_auto_20200710_0946'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente_cnpj',
            options={'ordering': ('nome_fantasia',)},
        ),
    ]
