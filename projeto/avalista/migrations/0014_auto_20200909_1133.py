# Generated by Django 3.0.7 on 2020-09-09 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avalista', '0013_auto_20200909_1036'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avalista',
            old_name='fiador_org_emissor',
            new_name='fiador_orgao_emissor',
        ),
    ]
