# Generated by Django 3.0.7 on 2020-09-10 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200909_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='dados_bancarios',
            name='tipo_de_conta',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Tipo de conta'),
        ),
    ]