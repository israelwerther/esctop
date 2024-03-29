# Generated by Django 3.0.7 on 2022-03-16 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20220316_1158'),
        ('avalista', '0028_auto_20210926_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='avalista',
            name='chave_pix',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Chave Pix'),
        ),
        migrations.AddField(
            model_name='avalista',
            name='tipo_de_chave_pix',
            field=models.ForeignKey(blank=True, max_length=50, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Chave_PIX'),
        ),
    ]
