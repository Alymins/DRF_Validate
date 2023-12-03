from rest_framework import serializers

from clients.models import Client
from clients.validators import valid_name, valid_cpf, valid_phone, valid_rg


class ClientSerializer(serializers.ModelSerializer):
    """Show all clients"""
    class Meta:
        model = Client
        fields = "__all__"
    
    def validate(self, data):
        if not valid_name(data['name']):
            raise serializers.ValidationError({"name": "The name cannot have numbers"})
        if not valid_cpf(data['cpf']):
            raise serializers.ValidationError({"cpf": "CPF Number Invalid"})
        if not valid_rg(data["rg"]):
            raise serializers.ValidationError({"rg": "The RG must have 9 digits"})
        if not valid_phone(data['phone']):
            raise serializers.ValidationError({"phone": "The phone must follow this pattern 99 99999-9999"})

               
        return data