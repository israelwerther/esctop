from email.policy import default
from queue import Empty
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse_lazy
from projeto.core.models import TimeStampedModel
from django.utils.translation import gettext_lazy as _ 
from projeto.cliente.models import Cliente
from projeto.cliente_cnpj.models import Cliente_cnpj
# testando o timedelta
from datetime import timedelta
from django_lifecycle import LifecycleModelMixin, hook
from django.utils import timezone

class Emprestimo(LifecycleModelMixin, models.Model):
    funcionario          = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    cliente              = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    cliente_cnpj         = models.ForeignKey(Cliente_cnpj, on_delete=models.CASCADE, null=True, blank=True)    
    valor_emprestado     = models.DecimalField("Valor Emprestado", max_digits=50, decimal_places=2, null=True, blank=True)
    qtd_parcelas         = models.PositiveIntegerField('Qtd Parcelas', null=True, blank=True)
    valor_prestacao      = models.DecimalField("Valor da parcela", max_digits=50, decimal_places=2, null=True, blank=True)    
    dt_emprestimo        = models.DateField("Data do Empréstimo", auto_now_add=False, auto_now=False, null=True,blank=True)
    dt_vencimento        = models.DateField("Data do Vencimento", auto_now_add=False, auto_now=False, null=True,blank=True)
    n_contrato           = models.CharField("Nº Contrato", max_length=255, unique=True, blank=True, null=True)
    valor_multa          = models.DecimalField("Multa por atraso", max_digits=50, decimal_places=2, null=True, blank=True)
    juros_ao_dia         = models.DecimalField("Juros ao dia", max_digits=50, decimal_places=2, null=True, blank=True)
    valor_mutuado        = models.DecimalField("Valor mutuado", max_digits=50, decimal_places=2, null=True, blank=True)
    juros_ao_mes         = models.DecimalField("Juros ao mês", max_digits=50, decimal_places=2, null=True, blank=True)
    juros_moratorio      = models.DecimalField("Juros Moratório", max_digits=50, decimal_places=4, null=True, blank=True)
    multa_por_atraso     = models.DecimalField("Multa por atraso", max_digits=50, decimal_places=3, null=True, blank=True)
    iof_real             = models.DecimalField("IOF real", max_digits=50, decimal_places=2, null=True, blank=True)
    valor_devido         = models.DecimalField("Valor devido", max_digits=50, decimal_places=2, null=True, blank=True)
    postergar            = models.PositiveIntegerField('Postergar', null=True, blank=True)
    
    # Modalidade do emprestimo é presencial ou online
    presencial           = models.BooleanField("Presencial", default=False)
    online               = models.BooleanField("Online", default=False)

    sequencia = models.PositiveIntegerField("Sequencia", null=True, blank=True)
    created_at  = models.DateTimeField(verbose_name='Registrado em', auto_now_add=True, blank=True, null=True)

    renegociar = models.BooleanField("Renegociação", default=False)

    class Meta:
        ordering = ('-dt_emprestimo',)
    # def __str__(self):
    #     return '{} - {} - {}'.format(self.pk, self.num_doc, self.created.strftime('%d-%m-%Y'))

    def __str__(self):
        return self.n_contrato if self.n_contrato else "Sem número de contrato cadastrado"
    
    def get_absolute_url(self):
        return reverse_lazy('emprestimo:emprestimo_detail', kwargs={'pk': self.pk})

    @hook('before_create')
    def gera_num_contrato(self):
        modalidade = 1 if self.online else 0
        tipo_cliente = 0 if self.cliente else 1
        data = self.dt_emprestimo.strftime('%d%m%Y')
        sequencia = 0

        if Emprestimo.objects.exists():
            ultimo_emprestimo = Emprestimo.objects.filter(
                dt_emprestimo__year = timezone.now().year,
            ).order_by('pk').last()
        
        if not Emprestimo.objects.filter(dt_emprestimo__year = timezone.now().year).exists():
            sequencia = 1
        else:
            sequencia = ultimo_emprestimo.sequencia + 1
        
        self.sequencia = sequencia
        self.n_contrato = f'{modalidade}{tipo_cliente}{data}{sequencia}'

# class EmprestimoParcelas(models.Model):
#     valor_parcela = models.DecimalField("Valor da Parcela", max_digits=10, decimal_places=2, null=True, blank=True)


class EmprestimoPagamento(models.Model):
    emprestimo           = models.ForeignKey(Emprestimo, on_delete=models.PROTECT)
    valor_pago           = models.DecimalField("Valor Pago", max_digits=10, decimal_places=2, null=True, blank=True)
    data_pagamento       = models.DateField("Data do Pagamento", auto_now_add=False, auto_now=False, null=True,blank=True,)



