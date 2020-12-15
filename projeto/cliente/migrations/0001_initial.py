# Generated by Django 3.0.5 on 2020-04-24 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CPF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(blank=True, max_length=11, null=True, verbose_name='CPF')),
                ('data_exp', models.DateTimeField(verbose_name='Data de expedição')),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('endereco', models.CharField(blank=True, max_length=200, null=True, verbose_name='Endereço')),
                ('rg', models.CharField(blank=True, max_length=20, null=True, verbose_name='RG')),
                ('data_nasc', models.DateField(blank=True, max_length=20, null=True, verbose_name='Data de Nascimento')),
                ('anotacoes', models.TextField(blank=True, max_length=100, null=True, verbose_name='Anotações')),
                ('email', models.EmailField(blank=True, max_length=50, null=True, verbose_name='Email')),
                ('num_telefone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefone')),
                ('cpf', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cliente.CPF')),
            ],
        ),
    ]
