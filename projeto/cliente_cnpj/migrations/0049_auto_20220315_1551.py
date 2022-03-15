# Generated by Django 3.0.7 on 2022-03-15 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20220315_1547'),
        ('cliente_cnpj', '0048_auto_20220117_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente_cnpj',
            name='chave_pix',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Chave Pix'),
        ),
        migrations.AddField(
            model_name='cliente_cnpj',
            name='tipo_de_chave_pix',
            field=models.ForeignKey(blank=True, max_length=50, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Chave_PIX'),
        ),
    ]
