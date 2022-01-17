from django.db import models
from django.urls import reverse_lazy
from projeto.cliente.models import Cliente
from projeto.avalista.models import Avalista
from projeto.core.models import Banco, Tipo_de_conta


class Cliente_cnpj(models.Model):
    razao_social          = models.CharField("Razão Social", max_length=50, blank=True, null=True)
    nome_fantasia         = models.CharField("Nome Fantasia", max_length=50, blank=True, null=True)
    cnpj                  = models.CharField("CNPJ", max_length=36, unique=True, blank=True, null=True)
    fundacao              = models.DateField("Fundação",max_length=8, blank=True, null=True)      
    inscricao_estadual    = models.CharField("Inscrição Estadual",blank=True, null=True, max_length=50)
    inscricao_municipal   = models.CharField("Inscrição Municipal", blank=True, null=True,max_length=50)
    #ENDEREÇO
    cep                   = models.CharField("CEP", max_length=10, blank=False, null=True)
    rua                   = models.CharField("Rua", max_length=60, blank=False, null=True)
    bairro                = models.CharField("Bairro", max_length=40, blank=False, null=True)
    cidade                = models.CharField("Cidade", max_length=40, blank=False, null=True)
    uf                    = models.CharField("UF", max_length=2, blank=False, null=True)   
    numero_casa           = models.CharField("Nº ", max_length=5, blank=True, null=True)
    ponto_referencia      = models.CharField("Ponto de Referencia", max_length=100, blank=True, null=True)
    complemento           = models.CharField("Complemento", max_length=100, blank=True, null=True)
    #CONTATO
    contato1              = models.CharField("Contato 1",max_length=15, blank=True, null=True)
    contato2              = models.CharField("Contato 2",max_length=15, blank=True, null=True)
    celular1              = models.CharField("Celular 1",max_length=17, blank=True, null=True)
    whatsapp1             = models.BooleanField("Whatsapp", default=True)
    celular2              = models.CharField("Celular 2",max_length=17, blank=True, null=True)
    whatsapp2             = models.BooleanField("Whatsapp", default=True)
    email                 = models.EmailField("Email", max_length=50, blank=True, null=True)
    # DADOS BANCÁRIOS
    banco                 = models.ForeignKey(Banco, on_delete=models.PROTECT,max_length=25, blank=True, null=True)  
    n_operacao            = models.CharField("Nº operação",max_length=15, blank=True, null=True)
    tipo_de_conta         = models.ForeignKey(Tipo_de_conta, on_delete=models.PROTECT,max_length=25, blank=True, null=True)  
    agencia               = models.CharField("Nº agência",max_length=15, blank=True, null=True)
    conta                 = models.CharField("Nº conta",max_length=15, blank=True, null=True)    
    # REFERÊNCIAS
    ref1_nome             = models.CharField("Nome", max_length=50, blank=True, null=True)
    ref1_contato          = models.CharField("Contato",max_length=17, blank=True, null=True)
    ref1_parentesco       = models.CharField("Parentesco", max_length=50, blank=True, null=True)
    ref2_nome             = models.CharField("Nome", max_length=50, blank=True, null=True)
    ref2_contato          = models.CharField("Contato",max_length=17, blank=True, null=True)
    ref2_parentesco       = models.CharField("Parentesco", max_length=50, blank=True, null=True)
    #REPRESENTANTE
    rep_nome              = models.CharField("Nome", max_length=50, blank=True, null=True)
    rep_cpf               = models.CharField("CPF", max_length=20, unique=True, blank=True, null=True) 
    rep_rg                = models.CharField("RG",max_length=20, blank=True, null=True)
    rep_orgao_emissor     = models.CharField("Orgão Emissor",max_length=20, blank=True, null=True)
    rep_pai               = models.CharField("Nome do Pai",max_length=50, blank=True, null=True)
    rep_mae               = models.CharField("Nome da Mãe",max_length=50, blank=True, null=True)
    rep_data_nasc         = models.DateField("Data de Nascimento",max_length=8, blank=True, null=True)
    rep_naturalidade      = models.CharField("Naturalidade", max_length=20, blank=True, null=True)
    rep_nacionalidade     = models.CharField("Nacionalidade",max_length=20, blank=True, null=True)
    rep_estado_civil      = models.CharField("Estado Civil",max_length=20, blank=True, null=True)
    rep_conjuge_nome      = models.CharField("Nome Cônjuge", max_length=50, blank=True, null=True)
    rep_conjuge_cpf       = models.CharField("CPF Cônjuge", max_length=20, unique=True,blank=True, null=True)
    rep_conjuge_telefone  = models.CharField("Contato Cônjuge",max_length=17, blank=True, null=True)
    #REPRESENTANTE CONTATO
    rep_contato1          = models.CharField("Tel Fixo",max_length=15, blank=True, null=True)
    rep_celular1          = models.CharField("Celular 1",max_length=17, blank=True, null=True)
    rep_whatsapp1         = models.BooleanField("Whatsapp", default=True)
    rep_celular2          = models.CharField("Celular 2",max_length=17, blank=True, null=True)
    rep_whatsapp2         = models.BooleanField("Whatsapp", default=True)
    rep_email             = models.EmailField("Email", max_length=50, blank=True, null=True)
    #REPRESENTANTE EMAIL
    rep_cep               = models.CharField("CEP", max_length=10, blank=True, null=True)
    rep_rua               = models.CharField("Rua", max_length=60, blank=True, null=True)
    rep_bairro            = models.CharField("Bairro", max_length=40, blank=True, null=True)
    rep_cidade            = models.CharField("Cidade", max_length=40, blank=True, null=True)
    rep_uf                = models.CharField("UF", max_length=2, blank=True, null=True)   
    rep_numero_casa       = models.CharField("Nº ", max_length=5, blank=True, null=True)
    rep_ponto_referencia  = models.CharField("Ponto de Referencia", max_length=100, blank=True, null=True)  
    #REPRESENTANTE FIADOR
    fiador                = models.ForeignKey(Avalista, on_delete=models.PROTECT, blank=True, null=True)    

    class Meta:
        ordering = ('razao_social',)
        
    def __str__(self):
        return self.razao_social
    
    def get_absolute_url(self):
        return reverse_lazy('cliente_cnpj:cliente_cnpj_detail', kwargs={'pk': self.pk})

    def save(self, force_insert=False, force_update=False):
        self.razao_social = self.razao_social.upper()
        super(Cliente_cnpj, self).save(force_insert, force_update)


# CRIAR UM TEMPLATE PRA RECEBER ESTES DOIS JÁ SALVOS
