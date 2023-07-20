from django.shortcuts import render
import base64
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser

from .services import (crear_ingreso, getXmlDictionary, getXml, cancelarEmbarque, imprimir_carta_porte, getXmlDictionaryFromXml,enviar_email_cfdi
                       ,cancelarCfdi)

from .models import Embarque, Cfdi, Sucursal,FacturistaEmbarques
from .serializers import EmbarquesSerializer


from django.views.generic import ListView




class EmbarquesPendientes(ListAPIView):   
    serializer_class = EmbarquesSerializer
    def get_queryset(self):
        fechaInicial= self.request.query_params.get('fecha_inicial')
        fechaFinal = self.request.query_params.get('fecha_final')
        sucursal = self.request.query_params.get('sucursal')
        return Embarque.objects.buscarPendientes(fechaInicial,fechaFinal,sucursal) 

class BuscarEmbarquePendiente(ListAPIView):
    serializer_class = EmbarquesSerializer 
    def get_queryset(self):
        documento= self.request.query_params.get('documento')
        sucursal = self.request.query_params.get('sucursal')
        return Embarque.objects.buscarEmbarquePendiente(documento,sucursal)

class EmbarquesCancelados(ListAPIView):
    serializer_class = EmbarquesSerializer
    def get_queryset(self):
        fechaInicial= self.request.query_params.get('fecha_inicial')
        fechaFinal = self.request.query_params.get('fecha_final')
        sucursal = self.request.query_params.get('sucursal')
        return Embarque.objects.buscarCancelados(fechaInicial,fechaFinal,sucursal) 

class BuscarEmbarqueCancelado(ListAPIView):
    serializer_class = EmbarquesSerializer 
    def get_queryset(self):
        documento= self.request.query_params.get('documento')
        sucursal = self.request.query_params.get('sucursal')
        return Embarque.objects.buscarEmbarqueCancelado(documento,sucursal)


class EmbarquesFacturados(ListAPIView):
    serializer_class = EmbarquesSerializer
    def get_queryset(self):
        fechaInicial= self.request.query_params.get('fecha_inicial')
        fechaFinal = self.request.query_params.get('fecha_final')
        sucursal = self.request.query_params.get('sucursal')
        #print(f" Periodo: {fechaInicial} - {fechaFinal}")
        return Embarque.objects.buscarFacturados(fechaInicial,fechaFinal, sucursal) 
 
class BuscarEmbarqueFacturado(ListAPIView):
    serializer_class = EmbarquesSerializer 
    def get_queryset(self):
        documento= self.request.query_params.get('documento')
        sucursal = self.request.query_params.get('sucursal')
        return Embarque.objects.buscarEmbarqueFacturado(documento,sucursal)

class CfdiCancelados(ListAPIView):   
    serializer_class = EmbarquesSerializer
    def get_queryset(self):
        fechaInicial= self.request.query_params.get('fecha_inicial')
        fechaFinal = self.request.query_params.get('fecha_final')
        sucursal = self.request.query_params.get('sucursal')
        return Embarque.objects.buscarPendientes(fechaInicial,fechaFinal,sucursal) 

@api_view(['POST'])
def generarCfdiCartaPorte(request):
    if request.method  == 'POST':
     
        embarque_id = request.query_params['embarque']
        resp =  crear_ingreso(embarque_id)
        if resp.get('message'):
            return Response({'message':resp['message']})
        
        xml = resp['xmlTimbrado']
        cfdi =  resp['cfdi']
        xmlDictionary = getXmlDictionaryFromXml(xml)
        return Response({'cfdi':cfdi, 'xmlTimbrado': xmlDictionary })
        #return Response({'Respuesta': 'Exitoso!!!!!!'})


class GenerarCfdiView(APIView):
  
     def post(self, request):
        permission_classes = [IsAuthenticated]
        #print(request.data)
            
        return Response({'Respuesta': 'Exitoso!!!!!!'})

@api_view(['GET'])
def cancelar_embarque(request):
    embarque = request.GET['embarque']
    #print(embarque)
    #print('*'*50)
    embarque = cancelarEmbarque(embarque)
    return Response({"embarque": embarque.documento, "cancelado": embarque.cancelado}) 
  


@api_view(['GET'])
def get_xml_dictionary(request):
    #print("Generando el XML Del Embaruqe")
    embarque = request.GET['embarque']
    #print(f"Generando el XML Del Embarque {embarque}")
    xmlDictionary = getXmlDictionary(embarque)
    return Response(xmlDictionary)

@api_view(['POST'])
def test_file(request):
    if request.method  == 'POST':
        with open('/Users/luisquintanilla/prueba.txt', 'r') as f:
            my_file = File(f)
            #print(my_file)
        return Response({'Respuesta': 'Exitoso!!!!!!'})


@api_view(['GET'])
def get_usuario_sucursal(request):
    ''' data = {'token': token}
    valid_data = TokenVerifySerializer().validate(data)
    user = valid_data['user'] '''
    #print("Obteneiendo el usuario !!!")
    user = request.user
    #print(user.__dict__)
    return Response({'name': user.username})

@api_view(['GET'])
def imprimir_cfdi_cartaporte(request):
    cfdiId = request.query_params.get('cfd')
    embarqueId = request.query_params.get('embarque')
    if embarqueId:
        embarqueId = embarqueId.replace("-","")
        #print('Ejecutando la vista para la impresion de la carta porte del embarque',embarqueId)
        cfdi = Cfdi.objects.get(origen = embarqueId)
        cfdiId = cfdi.id
    pdf = imprimir_carta_porte(cfdiId)

    #return Response({'Respuesta': 'Exitoso!!!!!!'})
    return HttpResponse(pdf, content_type='application/pdf')


@api_view(['GET'])
def enviar_email(request):
    #print("Enviando el Email del CFDI")
    embarqueId = request.query_params.get('embarque')
    if embarqueId:
        embarqueId = embarqueId.replace("-","")
        embarque = Embarque.objects.get(pk = embarqueId)
        email = embarque.cliente.email
        email_facturista = embarque.facturista.email
        #print('Ejecutando la vista para la impresion de la carta porte del embarque',embarqueId)
        cfdi = Cfdi.objects.get(origen = embarqueId)
        cfdiId = cfdi.id
        enviar_email_cfdi(cfdiId, email, email_facturista)
    return Response({'Respuesta': 'Exitoso!!!!!!'})


@api_view(['POST'])
def cancelar_cfdi(request):
    print(request.data.get('id'))
    embarque_id = request.data.get('id').replace ("-","")
    embarque = Embarque.objects.get(pk = embarque_id)
    facturista = embarque.facturista
    cfdi = Cfdi.objects.get(origen = embarque_id)
    cancelarCfdi(cfdi, facturista)
    
    return Response({'cacncelacion':'successfull'})

class TestViews(ListView):
    template_name = 'index.html'
    #model = Sucursal
    queryset =  Sucursal.objects.filter(activo=True)
  
    paginate_by: 1
    #context_object_name = "sucursales"
    #queryset =  Sucursal.objects.filter(nombre='ANDRADE')
    ''' def get_queryset(self):
        sucursales = Sucursal.objects.filter(nombre='ANDRADE')
        return sucursales '''

    
  
    def get_context_data(self, **kwargs):
      
        param = self.request.GET.get('param')
        prueba = self.kwargs['prueba']
        otro = self.kwargs['otro']
        context = super().get_context_data(**kwargs)
        context["datos"] = "Pruebas de datos"
        context['prueba'] = prueba
        context['otro'] = otro
        context['param'] = param
        return context
   

"""
    Vistas para cargar y leer archivos de CFDI
"""

@api_view(['GET'])
def get_key(request,facturista_id):
   print("Obteniendo la llave privada")
   facturista = FacturistaEmbarques.objects.filter(pk=facturista_id).first()
   print(facturista)
   print(facturista.llave_privada)
   return Response({"Key":facturista.llave_privada}) 


@api_view(['GET'])
def get_cert(request,facturista_id):
    pass
    ''' facturista = Contribuyente.objects.filter(pk=facturista_id).first()
    cert_file = contribuyente.certificado_digital
    cert = base64.b64encode(cert_file)
    return Response({"Value":"Test"}) '''

@api_view(['GET'])
def get_pfx(request,facturista_id):
    pass
    ''' contribuyente = Contribuyente.objects.filter(pk=facturista_id).first()
    pfx_file = contribuyente.certificado_digital_pfx
    cert = base64.b64encode(pfx_file)
    return Response({"Value":"Test"}) '''

@api_view(['GET'])
def get_numero_certificado(request,facturista_id):
    pass
    ''' contribuyente = Contribuyente.objects.filter(pk=facturista_id).first()
    numero_certificado = contribuyente.numero_certificado
    print(request.accepted_media_type)
    return Response({"Value":numero_certificado}) '''

@api_view(['POST'])
def set_numero_certificado(request,facturista_id):
    pass
    ''' contribuyente = Contribuyente.objects.filter(pk=contribuyente_id).first()
    numero_certificado = request.query_params['numero_certificado']
    contribuyente.numero_certificado = numero_certificado
    contribuyente.save()
    return Response({"Value":"The number was updated successfully"}) '''

class UploadCertView(APIView):
    pass
    parser_classes=[FileUploadParser]

    def post(self, request,facturista_id, filename, format=None):
        cert_file  = request.data['file'].read()
        contribuyente = FacturistaEmbarques.objects.filter(pk=facturista_id).first()
        contribuyente.certificado_digital = cert_file
        contribuyente.save()
        return Response({"Message": "The certified was updated successfully"}) 

class UploadKeyView(APIView):

    parser_classes=[FileUploadParser]

    def post(self, request,facturista_id, filename, format=None):
        print(type(request.data['file']))
        key_file  = request.data['file'].read()
        contribuyente = FacturistaEmbarques.objects.filter(pk=facturista_id).first()
        contribuyente.llave_privada = key_file
        contribuyente.save()
        return Response({"Texto": "The key was updated successfully"})
    

class UploadPfxView(APIView):
    pass

    parser_classes=[FileUploadParser]

    def post(self, request,facturista_id, filename, format=None):
        print(type(request.data['file']))
        pfx_file  = request.data['file'].read()
        facturista = FacturistaEmbarques.objects.filter(pk=facturista_id).first()
        facturista.certificado_digital_pfx= pfx_file
        facturista.save()
        print(request.accepted_media_type)
        return Response({"Message": "The pfx was updated successfully"}) 
