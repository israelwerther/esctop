# Generated by Django 3.0.7 on 2020-09-11 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0051_cliente_anotacoes_trabalho'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='whatsapp_trabalho',
            field=models.BooleanField(default=True),
        ),
    ]
