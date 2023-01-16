
from django.db import models

class EmbarquesManager(models.Manager):

    def buscarEmbarque(self, documento, sucursal):  
        #print(f"Buscando el embarque {documento} de la sucursal {sucursal} desde el manager ")   
        resultado = self.filter(
         documento = documento , sucursal__nombre = sucursal
        )
        return resultado 

    def buscarEmbarquePendiente(self, documento, sucursal):   
        resultado = self.filter(
        facturado__isnull=True, cancelado__isnull=True,
         documento = documento , sucursal__nombre = sucursal
        )
        return resultado 

    def buscarEmbarqueCancelado(self, documento, sucursal):   
        resultado = self.filter(
        facturado__isnull=True, cancelado__isnull=False,
         documento = documento , sucursal__nombre = sucursal
        )
        return resultado 

    def buscarEmbarqueFacturado(self, documento, sucursal):   
        resultado = self.filter(
        facturado__isnull=False, cancelado__isnull=True,
         documento = documento , sucursal__nombre = sucursal
        )
        return resultado 

    def buscarPendientes(self,fechaInicial, fechaFinal, sucursal):
        #print("Buscando los embarques pendientes")
        resultado = self.filter( facturado__isnull=True, cancelado__isnull=True,fecha__range=[fechaInicial, fechaFinal], sucursal__nombre  =sucursal ).order_by("documento")
        return resultado

    def buscarCancelados(self,fechaInicial, fechaFinal,sucursal):
        #print('Buscando embarques cancelados')
        resultado = self.filter( cancelado__isnull=False, cancelado__range=[fechaInicial, fechaFinal], sucursal__nombre  =sucursal ).order_by("documento")
        return resultado

    def buscarFacturados(self, fechaInicial, fechaFinal, sucursal):
        #print('Buscando Embarques Facturados')
        resultado = self.filter( facturado__isnull=False, fecha__range=[fechaInicial, fechaFinal], sucursal__nombre  =sucursal ).order_by("documento")
        return resultado
