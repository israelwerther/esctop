# Generated by Django 3.0.7 on 2021-02-16 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0065_auto_20201015_0700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='nome',
            field=models.CharField(max_length=50, null=True, verbose_name='Nome'),
        ),
    ]
