# Generated by Django 3.0.7 on 2020-09-09 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0043_auto_20200909_1036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='orgao_expedidor',
        ),
        migrations.AddField(
            model_name='cliente',
            name='orgao_emissor',
            field=models.CharField(max_length=15, null=True, verbose_name='Orgão Emissor'),
        ),
    ]