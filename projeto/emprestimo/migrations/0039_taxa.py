# Generated by Django 3.0.7 on 2020-11-09 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimo', '0038_auto_20201109_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='Taxa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taxa_juros_a_m', models.CharField(blank=True, max_length=25, null=True, verbose_name='Taxa de Juros a.m')),
            ],
            options={
                'ordering': ('taxa_juros_a_m',),
            },
        ),
    ]
