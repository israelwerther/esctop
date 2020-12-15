# Generated by Django 3.0.7 on 2020-09-10 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_banco_tipo_de_conta'),
        ('cliente', '0047_cliente_whatsapp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='banco',
            field=models.ForeignKey(blank=True, max_length=25, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Banco'),
        ),
    ]