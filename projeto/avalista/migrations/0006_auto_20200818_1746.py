# Generated by Django 3.0.7 on 2020-08-18 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avalista', '0005_auto_20200814_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avalista',
            name='fiador_agencia',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='FiadorAgência'),
        ),
        migrations.AlterField(
            model_name='avalista',
            name='fiador_bairro',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='FiadorBairro'),
        ),
        migrations.AlterField(
            model_name='avalista',
            name='fiador_banco',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='FiadorBanco'),
        ),
        migrations.AlterField(
            model_name='avalista',
            name='fiador_celular1',
            field=models.CharField(blank=True, max_length=17, null=True, verbose_name='Fiadorcelular 1'),
        ),
        migrations.AlterField(
            model_name='avalista',
            name='fiador_celular2',
            field=models.CharField(blank=True, max_length=17, null=True, verbose_name='Fiadorcelular 2'),
        ),
        migrations.AlterField(
            model_name='avalista',
            name='fiador_cep',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='FiadorCEP'),
        ),
        migrations.AlterField(
            model_name='avalista',
            name='fiador_cidade',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='FiadorCidade'),
        ),
        migrations.AlterField(
            model_name='avalista',
            name='fiador_conta',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='FiadorConta'),
        ),
        migrations.AlterField(
            model_name='avalista',
            name='fiador_contato1',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='FiadorContato 1'),
        ),
        migrations.AlterField(
            model_name='avalista',
            name='fiador_cpf',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='FiadorCPF'),
        ),
        migrations.AlterField(
            model_name='avalista',
            name='fiador_email',
            field=models.EmailField(blank=True, max_length=50, null=True, verbose_name='FiadorEmail'),
        ),
        migrations.AlterField(
            model_name='avalista',
            name='fiador_nome',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='FiadorNome'),
        ),
        migrations.AlterField(
            model_name='avalista',
            name='fiador_numero_casa',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='FiadorNº '),
        ),
        migrations.AlterField(
            model_name='avalista',
            name='fiador_obs_bancaria',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='FiadorObservações'),
        ),
        migrations.AlterField(
            model_name='avalista',
            name='fiador_ponto_referencia',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='FiadorPonto de Referencia'),
        ),
        migrations.AlterField(
            model_name='avalista',
            name='fiador_rg',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='FiadorRG'),
        ),
        migrations.AlterField(
            model_name='avalista',
            name='fiador_rua',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='FiadorRua'),
        ),
        migrations.AlterField(
            model_name='avalista',
            name='fiador_uf',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='FiadorEstado'),
        ),
    ]
