# Generated by Django 3.0.5 on 2020-04-18 21:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produto', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now_add=True, verbose_name='Modificado em')),
                ('nf', models.PositiveIntegerField(blank=True, null=True, verbose_name='nota fiscal')),
                ('movimento', models.CharField(choices=[('e', 'entrada'), ('s', 'saida')], max_length=1, verbose_name='')),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='EstoqueItens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField()),
                ('saldo', models.PositiveIntegerField()),
                ('estoque', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.Estoque')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.Produto')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
    ]
