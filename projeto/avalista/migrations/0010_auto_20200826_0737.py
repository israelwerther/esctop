# Generated by Django 3.0.7 on 2020-08-26 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avalista', '0009_remove_avalista_fiador_copia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avalista',
            name='fiador_agencia',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Agência'),
        ),
        migrations.AlterField(
            model_name='avalista',
            name='fiador_bairro',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Bairro'),
        ),
        migrations.AlterField(
            model_name='avalista',
            name='fiador_banco',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Banco'),
        ),
        migrations.AlterField(
            model_name='avalista',
            name='fiador_celular1',
            field=models.CharField(blank=True, max_length=17, null=True, verbose_name='celular 1'),
        ),
        migrations.AlterField(
            model_name='avalista',
            name='fiador_celular2',
            field=models.CharField(blank=True, max_length=17, null=True, verbose_name='celular 2'),
        ),
        migrations.AlterField(
            model_name='avalista',
            name='fiador_cep',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='avalista',
            name='fiador_cidade',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='avalista',
            name='fiador_conta',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Conta'),
        ),
        migrations.AlterField(
            model_name='avalista',
            name='fiador_contato1',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Contato 1'),
        ),
        migrations.AlterField(
            model_name='avalista',
            name='fiador_cpf',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='avalista',
            name='fiador_email',
            field=models.EmailField(blank=True, max_length=50, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='avalista',
            name='fiador_nome',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='avalista',
            name='fiador_numero_casa',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Nº '),
        ),
        migrations.AlterField(
            model_name='avalista',
            name='fiador_obs_bancaria',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Observações'),
        ),
        migrations.AlterField(
            model_name='avalista',
            name='fiador_ponto_referencia',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Ponto de Referencia'),
        ),
        migrations.AlterField(
            model_name='avalista',
            name='fiador_rg',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='RG'),
        ),
        migrations.AlterField(
            model_name='avalista',
            name='fiador_rua',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Rua'),
        ),
        migrations.AlterField(
            model_name='avalista',
            name='fiador_uf',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='Estado'),
        ),
    ]
