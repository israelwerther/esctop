# Generated by Django 3.0.7 on 2022-03-15 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20220315_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chave_pix',
            name='pix_key_type',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Tipo de Chave'),
        ),
    ]
