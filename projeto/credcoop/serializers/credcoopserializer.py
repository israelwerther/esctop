from projeto.credcoop.models import ClienteCredcoop, Contato, DadosBancarios, DadosPessoais, Endereco, LocalDeTrabalho
from rest_framework import serializers




class DadosPessoaisCredcoopSerializer(serializers.ModelSerializer):
    class Meta:
        model = DadosPessoais
        fields = '__all__'

class EnderecoCredcoopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'

class ContatoCredcoopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = '__all__'

class LocalDeTrabalhoCredcoopSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalDeTrabalho
        fields = '__all__'


class DadosBancariosCredcoopSerializer(serializers.ModelSerializer):
    class Meta:
        model = DadosBancarios
        fields = '__all__'



class ClienteCredcoopSerializer(serializers.ModelSerializer):
    
    dados_pessoais = DadosPessoaisCredcoopSerializer()
    endereco = EnderecoCredcoopSerializer(many=True)
    contato = ContatoCredcoopSerializer(many=True)
    local_de_trabalho = LocalDeTrabalhoCredcoopSerializer(many=True)
    dados_bancarios = DadosBancariosCredcoopSerializer(many=True)

    class Meta:
        model = ClienteCredcoop
        fields = ['dados_pessoais', 'endereco', 'contato', 'local_de_trabalho', 'dados_bancarios' ]