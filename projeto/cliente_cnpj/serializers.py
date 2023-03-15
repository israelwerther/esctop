from rest_framework import serializers
from .models import Cliente_cnpj

class Cliente_cnpjSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente_cnpj
        fields = '__all__'