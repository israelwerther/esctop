# Generated by Django 4.1.3 on 2022-12-10 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_auto_20200419_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
