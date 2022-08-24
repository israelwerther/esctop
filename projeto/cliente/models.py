#para campo required
#https://stackoverflow.com/questions/1134667/django-required-field-in-model-form/1429646
from django.db import models
from django.urls import reverse_lazy
from projeto.core.models import Banco, Chave_PIX, Tipo_de_conta


class Cliente(models.Model):
    #Dados pessoais do Cliente Credcoop
    nome                  = models.CharField("Nome", max_length=50, blank=False, null=True)
    cpf                   = models.CharField("CPF", max_length=20, unique=True)
    rg                    = models.CharField("RG",max_length=20, blank=False, null=True)
    orgao_emissor         = models.CharField("Orgão Emissor", max_length=15, blank=False, null=True)
    data_nasc             = models.DateField("Data de Nascimento",max_length=8, blank=False, null=True)
    naturalidade          = models.CharField("Naturalidade", max_length=20, blank=False, null=True)    
    nacionalidade         = models.CharField("Nacionalidade", max_length=15, blank=True, null=True)
    estado_civil          = models.CharField("Estado Civil", max_length=15, blank=True, null=True)  
    conjuge_nome          = models.CharField("Nome Cônjuge", max_length=50, blank=True, null=True)
    conjuge_cpf           = models.CharField("CPF Cônjuge", max_length=20, unique=True,blank=True, null=True)
    conjuge_telefone      = models.CharField("Contato Cônjuge",max_length=17, blank=True, null=True)
    nome_da_mae           = models.CharField("Nome da Mãe", max_length=50, blank=False, null=True)
    nome_do_pai           = models.CharField("Nome da Pai", max_length=50, blank=True, null=True)
    # ENDEREÇO
    cep                   = models.CharField("CEP", max_length=10, blank=False, null=True)
    rua                   = models.CharField("Rua", max_length=60, blank=False, null=True)
    bairro                = models.CharField("Bairro", max_length=40, blank=False, null=True)
    cidade                = models.CharField("Cidade", max_length=40, blank=False, null=True)
    uf                    = models.CharField("UF", max_length=2, blank=False, null=True)   
    numero_casa           = models.CharField("Nº ", max_length=5, blank=True, null=True)
    ponto_referencia      = models.CharField("Ponto de Referencia", max_length=100, blank=True, null=True)
    complemento           = models.CharField("Complemento", max_length=100, blank=True, null=True)
    # CONTATO
    contato1              = models.CharField("Contato 1",max_length=15, blank=True, null=True)
    contato2              = models.CharField("Contato 2",max_length=15, blank=True, null=True)
    celular1              = models.CharField("celular 1",max_length=17, blank=True, null=True)
    celular2              = models.CharField("celular 2",max_length=17, blank=True, null=True)
    whatsapp1             = models.BooleanField("Whatsapp", default=True)
    whatsapp2             = models.BooleanField("Whatsapp", default=True)
    email                 = models.EmailField("Email", max_length=50, blank=True, null=True)    
    # ONDE VAI ESSE CAMPO?
    sacado                = models.CharField("Sacado",max_length=50, blank=True, null=True)
    # DADOS DO LOCAL DE TRABALHO
    nome_fantasia         = models.CharField("Nome Fantasia",max_length=50, blank=True, null=True)
    contato1_trabalho     = models.CharField("Contato 1",max_length=15, blank=True, null=True)
    contato2_trabalho     = models.CharField("Contato 2",max_length=15, blank=True, null=True)
    celular1_trabalho     = models.CharField("celular 1",max_length=17, blank=True, null=True)
    celular2_trabalho     = models.CharField("celular 2",max_length=17, blank=True, null=True)
    whatsapp1_trabalho    = models.BooleanField("Whatsapp", default=True)
    whatsapp2_trabalho    = models.BooleanField("Whatsapp", default=True)
    cep_trabalho          = models.CharField("CEP", max_length=10, blank=True, null=True)
    rua_trabalho          = models.CharField("Rua", max_length=60, blank=True, null=True)
    bairro_trabalho       = models.CharField("Bairro", max_length=40, blank=True, null=True)
    cidade_trabalho       = models.CharField("Cidade", max_length=40, blank=True, null=True)
    uf_trabalho           = models.CharField("Estado", max_length=2, blank=True, null=True)
    numero_casa_trabalho  = models.CharField("Nº ", max_length=5, blank=True, null=True)
    referencia_trabalho   = models.CharField("Ponto de Referencia",max_length=50, blank=True, null=True)  
    obs_trabalho          = models.TextField("Observações",max_length=200, blank=True, null=True)
    # DADOS BANCÁRIOS
    banco                 = models.ForeignKey(Banco, on_delete=models.PROTECT,max_length=25, blank=True, null=True)  
    n_operacao            = models.CharField("Nº operação",max_length=15, blank=True, null=True)
    agencia               = models.CharField("Nº agência",max_length=15, blank=True, null=True)
    conta                 = models.CharField("Nº conta",max_length=15, blank=True, null=True)   
    tipo_de_conta         = models.ForeignKey(Tipo_de_conta, on_delete=models.PROTECT,max_length=25, blank=True, null=True)
    tipo_de_chave_pix     = models.ForeignKey(Chave_PIX, on_delete=models.PROTECT,max_length=50, blank=True, null=True)
    chave_pix             = models.CharField("Chave Pix", max_length=50, blank=True, null=True)   

    # REFERÊNCIAS
    ref1_nome             = models.CharField("Nome", max_length=50, blank=True, null=True)
    ref1_contato          = models.CharField("Contato",max_length=17, blank=True, null=True)
    ref1_parentesco       = models.CharField("Parentesco", max_length=50, blank=True, null=True)
    ref2_nome             = models.CharField("Nome", max_length=50, blank=True, null=True)
    ref2_contato          = models.CharField("Contato",max_length=17, blank=True, null=True)
    ref2_parentesco       = models.CharField("Parentesco", max_length=50, blank=True, null=True)
    ref3_nome             = models.CharField("Nome", max_length=50, blank=True, null=True)
    ref3_contato          = models.CharField("Contato",max_length=17, blank=True, null=True)
    ref3_parentesco       = models.CharField("Parentesco", max_length=50, blank=True, null=True)

    fiador                = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    fiador_inativo        = models.BooleanField("Fiador inativo", default=False)

    class Meta:
        ordering = ('nome',) #confirme se é a organização e apague o coment

    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse_lazy('cliente:cliente_detail', kwargs={'pk': self.pk})
    
    def save(self, force_insert=False, force_update=False):
        self.nome = self.nome.upper()
        super(Cliente, self).save(force_insert, force_update)

