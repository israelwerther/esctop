# Generated by Django 3.0.7 on 2020-09-10 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente_cnpj', '0035_auto_20200909_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente_cnpj',
            name='whatsapp',
            field=models.BooleanField(default=True),
        ),
    ]