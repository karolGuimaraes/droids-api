from rest_framework import serializers
from droid_api.models import *

class PecaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peca
        fields = ['descricao']

class ContaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conta
        fields = ['username', 'telefone', 'email', 'first_name', 'last_name', 'password']

    def to_representation(self, obj):
        self.Meta.fields = ['username', 'telefone', 'email']
        return super(ContaSerializer, self).to_representation(obj) 

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['cep', 'logradouro', 'numero', 'complemento', 'bairro', 'cidade', 'estado']

class DemandaSerializer(serializers.ModelSerializer):
    peca = PecaSerializer()
    anunciante = ContaSerializer(read_only=True)
    endereco_entrega = EnderecoSerializer()
    finalizada = serializers.SerializerMethodField()

    def get_finalizada(self, obj):
        return "Finalizada" if obj.finalizada else "Aberta"

    class Meta:
        model = Demanda
        fields = ['id', 'finalizada', 'peca', 'anunciante', 'endereco_entrega']
