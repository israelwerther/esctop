# Generated by Django 3.0.7 on 2020-10-02 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimo', '0022_remove_emprestimo_data_teste'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprestimo',
            name='n_contrato',
            field=models.CharField(blank=True, max_length=13, null=True, unique=True),
        ),
    ]
