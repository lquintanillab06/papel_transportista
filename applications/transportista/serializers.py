

from rest_framework import serializers

from applications.transportista.models import (
        Embarque,FacturistaEmbarques,Sucursal,Operador
    )


class FacturistaSerializer(serializers.ModelSerializer):
    class Meta:
        model=  FacturistaEmbarques
        fields = ['id','nombre','clave']

class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model=  Sucursal
        fields = ['id','nombre','clave']

class OperadorSerializer(serializers.ModelSerializer):
    class Meta:
        model=  Operador
        fields = ['id','nombre']

class EmbarquesSerializer(serializers.ModelSerializer):
    facturista = FacturistaSerializer(many=False, read_only=True)
    sucursal = SucursalSerializer(many=False, read_only=True)
    operador = OperadorSerializer(many=False, read_only=True)
    class Meta: 
        model = Embarque
        fields= ['id','documento','fecha','facturista','sucursal','operador','importe_comision','valor','cancelado']
       