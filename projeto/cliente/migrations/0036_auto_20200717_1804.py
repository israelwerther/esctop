# Generated by Django 3.0.7 on 2020-07-17 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0035_clientecopia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientecopia',
            name='cliente_copia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.Cliente'),
        ),
    ]