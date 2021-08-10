#para campo required
#https://stackoverflow.com/questions/1134667/django-required-field-in-model-form/1429646
from django.db import models
from django.urls import reverse_lazy
from projeto.core.models import Banco, Tipo_de_conta

class DadosPessoais(models.Model):
    #dados pessoais 
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

class Endereco(models.Model):
    # ENDEREÇO
    cep                   = models.CharField("CEP", max_length=10, blank=False, null=True)
    rua                   = models.CharField("Rua", max_length=60, blank=False, null=True)
    bairro                = models.CharField("Bairro", max_length=40, blank=False, null=True)
    cidade                = models.CharField("Cidade", max_length=40, blank=False, null=True)
    uf                    = models.CharField("UF", max_length=2, blank=False, null=True)   
    numero_casa           = models.CharField("Nº ", max_length=5, blank=True, null=True)
    ponto_referencia      = models.CharField("Ponto de Referencia", max_length=100, blank=True, null=True)
    complemento           = models.CharField("Complemento", max_length=100, blank=True, null=True)

    def __str__(self):
        return f'Rua {self.rua} bairro {self.bairro}'

class Contato(models.Model):
    # CONTATO
    contato              = models.CharField("Contato 1",max_length=15, blank=True, null=True)
    whatsapp             = models.BooleanField("Whatsapp", default=True)
    email                 = models.EmailField("Email", max_length=50, blank=True, null=True) 

class Referencias(models.Model):
    # REFERÊNCIAS
    nome             = models.CharField("Nome", max_length=50, blank=True, null=True)
    contato = models.ForeignKey(Contato, on_delete=models.CASCADE)
    parentesco       = models.CharField("Parentesco", max_length=50, blank=True, null=True)
    

class LocalDeTrabalho(models.Model):
    # DADOS DO LOCAL DE TRABALHO
    nome_fantasia         = models.CharField("Nome Fantasia",max_length=50, blank=True, null=True)
    contato = models.ManyToManyField(Contato)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    referencia_trabalho   = models.CharField("Ponto de Referencia",max_length=50, blank=True, null=True)  
    obs_trabalho          = models.TextField("Observações",max_length=200, blank=True, null=True)

class DadosBancarios(models.Model):

    # DADOS BANCÁRIOS
    banco                 = models.ForeignKey(Banco, on_delete=models.PROTECT,max_length=25, blank=True, null=True)  
    n_operacao            = models.CharField("Nº operação",max_length=15, blank=True, null=True)
    agencia               = models.CharField("Nº agência",max_length=15, blank=True, null=True)
    conta                 = models.CharField("Nº conta",max_length=15, blank=True, null=True)
    tipo_de_conta         = models.ForeignKey(Tipo_de_conta, on_delete=models.PROTECT,max_length=25, blank=True, null=True)


# cliente credcoop
class ClienteCredcoop(models.Model):   

    dados_pessoais = models.ForeignKey(DadosPessoais, on_delete=models.CASCADE)
    endereco = models.ManyToManyField(Endereco, "Endereco")
    contato = models.ManyToManyField(Contato, "Contato")
    local_de_trabalho = models.ManyToManyField(LocalDeTrabalho)
    dados_bancarios = models.ManyToManyField(DadosBancarios)
    
    # ONDE VAI ESSE CAMPO?
    # sacado                = models.CharField("Sacado",max_length=50, blank=True, null=True)      

    fiador                = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.dados_pessoais.nome
    
    def save(self, force_insert=False, force_update=False):
        self.nome = self.dados_pessoais.nome.upper()
        super(ClienteCredcoop, self).save(force_insert, force_update)

