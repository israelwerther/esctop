# Generated by Django 3.0.7 on 2022-04-06 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimo', '0061_auto_20220406_1257'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emprestimo',
            old_name='onlene',
            new_name='online',
        ),
    ]