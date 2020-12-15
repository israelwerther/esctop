# Generated by Django 3.0.6 on 2020-05-30 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimo', '0012_auto_20200519_1143'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmprestimoPagamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_pago', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Valor Pago')),
                ('emprestimo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='emprestimo.Emprestimo')),
            ],
        ),
    ]
