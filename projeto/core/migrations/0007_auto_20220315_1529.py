# Generated by Django 3.0.7 on 2022-03-15 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_chave_pix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chave_pix',
            name='pix_key_type',
            field=models.CharField(blank=True, choices=[('cfpcnpj', 'CPF ou CNPJ'), ('email', 'E-mail'), ('cellphone', 'Celular ou Telefone'), ('randonkey', 'Chave aleatória'), ('dadosbancarios', 'Dados Bancários')], max_length=30, null=True, verbose_name='Tipo de Chave'),
        ),
    ]
