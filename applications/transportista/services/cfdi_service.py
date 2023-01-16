
import base64
from ..models import Cfdi
import xmltodict
import json
from mailjet_rest import Client
from .print_service import imprimir_carta_porte_envio

def crear_cfdi(comprobante, xml, cadena, embarque):
    cfdi = Cfdi()
    cfdi.fecha = comprobante.Fecha
    cfdi.tipo_de_comprobante = "I"
    cfdi.origen = str(embarque.id).replace('-','')
    cfdi.serie = "TEST"
    cfdi.folio =  embarque.documento
    cfdi.total =   comprobante.Total
    cfdi.emisor_rfc = comprobante.Emisor.Rfc
    cfdi.emisor = comprobante.Emisor.Nombre
    cfdi.receptor_rfc = comprobante.Receptor.Rfc
    cfdi.receptor = comprobante.Receptor.Nombre
    cfdi.version = 0
    cfdi.cadena = cadena
    #cfdi.xml = base64.b64encode(str.encode(xml))
    xmlBase64 = base64.b64encode(str.encode(xml))
    cfdi.xml =  xmlBase64.decode()
    
    cfdi.save()
    
    return cfdi

def getXml(cfdiId):
    cfdi = Cfdi.objects.get(id = cfdiId )
    #print(cfdi.cadena)
    xml = base64.b64decode(cfdi.xml)
    cadena = (cfdi.cadena)
    #print(xml)
    return {'xml':xml, 'cadena':cadena}

def getXmlDictionary(embarque):
    print('*'*50)
    print(embarque)
    print('*'*50)
    cfdi = Cfdi.objects.get(origen = embarque) 
    xml = getXml(cfdi.id)
    xmlDict = xmltodict.parse(xml['xml'])
    #print(xmlDict)
    xmlJson = json.dumps(xmlDict)
    #print(xmlJson)

    return xmlDict

def getXmlDictionaryFromXml(xml):
    xmlDict = xmltodict.parse(xml)
    xmlJson = json.dumps(xmlDict)
    return xmlDict

def enviar_email_cfdi(cfdiId):
    pdf,xml = imprimir_carta_porte_envio(cfdiId)
    pdfB64 = base64.b64encode(pdf).decode()
    xml_bytes = xml.encode('utf-8')
    xmlB64 = base64.b64encode(xml_bytes).decode()
    with open("api_transportista/conf/config.json") as f:
        configuration = json.loads(f.read())
        USER =  configuration['MAIL_JET_USER']
        PASSWORD =  configuration['MAIL_JET_PASSWORD']
        mailjet =  Client(auth=(USER, PASSWORD), version='v3.1')
        data = {
            'Messages': [
                {
                    'From': {
                       'Email':'facturacion@papelsa.mobi',
                        "Name": "facturacion"
                    },
                    "To":[
                        {
                            "Email": "lquintanillab@gmail.com",
                            "Name": "Luis Quintanilla"
                        }
                    ],
                    "Subject": "My first Mailjet Email!",
                    "TextPart": "Greetings from Mailjet!",
                    "HTMLPart": "<h3>Dear passenger 1, welcome to <a href=\"https://www.mailjet.com/\">Mailjet</a>!</h3><br />May the delivery force be with you!",
                    "Attachments": [
                                {
										"ContentType": "application/pdf",
										"Filename": "cfdi.pdf",
										"Base64Content": pdfB64 

								},
                                {
										"ContentType": "application/xml",
										"Filename": "cfdi.xml",
										"Base64Content": xmlB64 

								}
						]
                        
                    
                }
            ]
        }
        result = mailjet.send.create(data=data)
        #print(result.status_code)
        #print(result.json())
