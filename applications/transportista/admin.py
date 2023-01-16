from django.contrib import admin
from .models import FacturistaEmbarques, Operador, Propietario, TransporteEmbarques

# Register your models here.


admin.site.register(FacturistaEmbarques)
admin.site.register(Operador)
admin.site.register(Propietario)
admin.site.register(TransporteEmbarques)