from xml.dom import xmlbuilder
from...cfdi.cfdi_sat.builders import CartaPorteBuilder,CadenaOriginalBuilder,CartaPorteXmlBuilder,CfdiSellador
from ...cfdi.services import EdicomService
from ..models import Embarque
from .cfdi_service import crear_cfdi
import base64

from datetime import datetime



def crear_ingreso(embarque_id):

    embarque = Embarque.objects.get(id = embarque_id)
    builder = CartaPorteBuilder(embarque)
    comprobante = builder.build()
    cadena_builder = CadenaOriginalBuilder()
    cadena = cadena_builder.build(comprobante)
    sellador = CfdiSellador()
    comp = sellador.sellar(cadena,comprobante)
    xmlbuilder = CartaPorteXmlBuilder(comprobante)
    xml = xmlbuilder.build()
    #print(xml)
    cfdi = crear_cfdi(comprobante, xml, cadena, embarque)
    service = EdicomService()
    xmlTimbrado = service.getCfdiTest(xml)
    #print(xmlTimbrado)
    xmlBase64 = base64.b64encode(str.encode(xmlTimbrado))
    #xmlBase64 = base64.b64encode(str.encode(xml))
    embarque.facturado = datetime.now()
    embarque.save()
    cfdi.xml =  xmlBase64.decode()
    cfdi.save()
   
    #return {'cfdi':cfdi.id, 'xmlTimbrado': xmlTimbrado }
    return {'cfdi':cfdi.id, 'xmlTimbrado': xmlTimbrado}

def cancelarEmbarque(embarque):
    embarque = Embarque.objects.get(pk=embarque)
    embarque.cancelado= datetime.now() 
    embarque.save()

    return embarque
  

   


