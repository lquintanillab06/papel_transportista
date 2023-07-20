from xml.dom import xmlbuilder
from...cfdi.cfdi_sat.builders import CartaPorteBuilder,CadenaOriginalBuilder,CartaPorteXmlBuilder,CfdiSellador
from ...cfdi.services import EdicomService
from ..models import Embarque
from .cfdi_service import crear_cfdi, getXmlData
import base64

from datetime import datetime



def crear_ingreso(embarque_id):

    embarque = Embarque.objects.get(id = embarque_id)
    facturista = embarque.facturista
    try:
        builder = CartaPorteBuilder(embarque)
    except Exception as e:
        print(e)
        return {'message': "Ocurrio un error"}
    comprobante = builder.build()
    cadena_builder = CadenaOriginalBuilder()
    cadena = cadena_builder.build(comprobante)
    sellador = CfdiSellador()
    #comp = sellador.sellar(cadena,comprobante)
    comp = sellador.sellar(cadena,comprobante,facturista)
    xmlbuilder = CartaPorteXmlBuilder(comprobante)
    xml = xmlbuilder.build()
    #print(xml)
   
    service = EdicomService()
    xmlTimbrado = None
    try:
        xmlTimbrado = service.getCfdiTest(xml)
    except Exception as e:
        print(e)
        return {'message': "Ocurrio un error"}
    cfdi = crear_cfdi(comprobante, xml, cadena, embarque)
    xmlBase64 = base64.b64encode(str.encode(xmlTimbrado))
    embarque.facturado = datetime.now()
    embarque.save()
    cfdi.uuid = getXmlData(xmlTimbrado)
    cfdi.xml =  xmlBase64.decode()
    cfdi.serie = comprobante.Serie
    cfdi.folio = comprobante.Folio
    cfdi.save()
   
    #return {'cfdi':cfdi.id, 'xmlTimbrado': xmlTimbrado }
    return {'cfdi':cfdi.id, 'xmlTimbrado': xmlTimbrado}

def cancelarEmbarque(embarque):
    embarque = Embarque.objects.get(pk=embarque)
    embarque.cancelado= datetime.now() 
    embarque.save()

    return embarque
  

def cancelarCfdi(cancelacion,facturista):
    print("Cancelacion",cancelacion)
    service = EdicomService()
    service.cancelCfdi(cancelacion, facturista)
    #file = service.getUUID()
    #print(file)
   


