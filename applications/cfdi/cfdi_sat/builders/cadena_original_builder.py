
import  lxml.etree as ET

from .cartaporte_xml_builder import CartaPorteXmlBuilder



class CadenaOriginalBuilder():


    def build(self,comprobante):
        #print("Generando la cadena original")
        source = self.buildSource(comprobante)
        transformer = self.getTransformer()
        cadena = transformer(source)
        return cadena


    def buildSource(self, comprobante):
        xml = self.cadenaBuilderFactory(comprobante)
        xmlSource = ET.XML(xml)
        return xmlSource

    def getTransformer(self):
        xsltfile = "applications/cfdi/cfdi_sat/xslt/xslt4/cadenaoriginal.xslt"
        xslt = ET.parse(xsltfile)
        transform = ET.XSLT(xslt)
        
        return transform


    def cadenaBuilderFactory(self, comprobante):
        if(comprobante.TipoDeComprobante.value == 'I'):
           return CartaPorteXmlBuilder(comprobante).build().replace('<?xml version="1.0" encoding="utf-8"?>', '')
        
        

