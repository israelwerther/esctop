# Generated by Django 3.0.5 on 2020-05-11 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimo', '0004_auto_20200511_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='data_emprestimo',
            field=models.DateField(blank=True, null=True, verbose_name='Data do Emprestimo'),
        ),
    ]
