# Generated by Django 3.0.7 on 2020-12-24 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimo', '0056_emprestimo_janeiro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprestimo',
            name='janeiro',
        ),
        migrations.AddField(
            model_name='emprestimo',
            name='primeiro',
            field=models.BooleanField(default=False, verbose_name='janeiro'),
        ),
    ]