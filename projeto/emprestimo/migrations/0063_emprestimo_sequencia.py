# Generated by Django 3.0.7 on 2022-05-02 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimo', '0062_auto_20220406_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprestimo',
            name='sequencia',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='Sequencia'),
        ),
    ]