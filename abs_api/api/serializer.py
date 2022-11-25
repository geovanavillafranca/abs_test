from calendar import c
from api.models import Client, Seller, Product
from api.validators import *

from rest_framework import serializers


class ClientSerializer(serializers.ModelSerializer):	
    class Meta:
        model = Client
        fields = '__all__'
    
    def validate(self, data):
        if not valid_number(data['phone_number']):
            raise serializers.ValidationError({'phone_number': "O número de celular deve seguir este modelo: 11 912341234"})

        if not valid_zip_code(data['zip_code']):
            raise serializers.ValidationError({'zip_code': 'O CEP é inválido, deve  seguir este modelo 12345-123'})
            
        return data



class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = '__all__'
    

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'





