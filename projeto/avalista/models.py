from django.db import models
from django.urls import reverse_lazy
from projeto.core.models import Banco, Tipo_de_conta

class Avalista(models.Model): 
    fiador_nome                = models.CharField("Nome", max_length=50, blank=True, null=True)
    fiador_cpf                 = models.CharField("CPF", max_length=20, unique=True, blank=True, null=True) 
    fiador_rg                  = models.CharField("RG",max_length=20, blank=True, null=True)
    fiador_orgao_emissor       = models.CharField("Orgão Emissor",max_length=20, blank=True, null=True)
    fiador_data_nasc           = models.DateField("Data de Nascimento",max_length=8, blank=False, null=True) 
    fiador_estado_civil        = models.CharField("Estado Civil",max_length=20, blank=True, null=True)
    fiador_naturalidade        = models.CharField("Naturalidade", max_length=20, blank=False, null=True) 
    fiador_nacionalidade       = models.CharField("Nacionalidade",max_length=20, blank=True, null=True)
    fiador_email               = models.EmailField("Email", max_length=50, blank=True, null=True)
    fiador_contato1            = models.CharField("Contato 1",max_length=15, blank=True, null=True)
    fiador_celular1            = models.CharField("celular 1",max_length=17, blank=True, null=True)
    whatsapp1                  = models.BooleanField("Whatsapp", default=True)
    fiador_celular2            = models.CharField("celular 2",max_length=17, blank=True, null=True)
    whatsapp2                  = models.BooleanField("Whatsapp", default=True)
    fiador_cep                 = models.CharField("CEP", max_length=10, blank=True, null=True)
    fiador_rua                 = models.CharField("Rua", max_length=60, blank=True, null=True)
    fiador_bairro              = models.CharField("Bairro", max_length=40, blank=True, null=True)
    fiador_cidade              = models.CharField("Cidade", max_length=40, blank=True, null=True)
    fiador_uf                  = models.CharField("UF", max_length=2, blank=True, null=True)   
    fiador_numero_casa         = models.CharField("Nº ", max_length=5, blank=True, null=True)
    fiador_ponto_referencia    = models.CharField("Ponto de Referencia", max_length=100, blank=True, null=True)
    fiador_complemento         = models.CharField("Complemento", max_length=100, blank=True, null=True)

    banco                      = models.ForeignKey(Banco, on_delete=models.PROTECT,max_length=25, blank=True, null=True)  
    fiador_n_operacao          = models.CharField("Nº operação",max_length=15, blank=True, null=True)
    fiador_agencia             = models.CharField("Nº agência",max_length=15, blank=True, null=True)
    fiador_conta               = models.CharField("Nº conta",max_length=15, blank=True, null=True)
    tipo_de_conta              = models.ForeignKey(Tipo_de_conta, on_delete=models.PROTECT,max_length=25, blank=True, null=True)  


    class Meta:
        ordering = ('fiador_nome',) 
    
    def __str__(self):
        return str(self.fiador_nome)
    
    def get_absolute_url(self):
        return reverse_lazy('avalista:avalista_detail', kwargs={'pk': self.pk})   

    def save(self, force_insert=False, force_update=False):
        self.fiador_nome = self.fiador_nome.upper()
        super(Avalista, self).save(force_insert, force_update)       
    
    # def save(self, force_insert=False, force_update=False):
    #     self.fiador_nome = self.fiador_nome.upper()
    #     super(Avalista, self).save(force_insert, force_update)
