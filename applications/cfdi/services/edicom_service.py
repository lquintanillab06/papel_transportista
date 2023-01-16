
from suds.client import Client
import ssl
import base64
import zipfile
import json


from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import io


class EdicomService:
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context

    wsdl = "https://cfdiws.sedeb2b.com/EdiwinWS/services/CFDi?wsdl"
    client = Client(wsdl)

   

    def __init__(self):
        with open("api_transportista/conf/config.json") as f:
            self.configuration = json.loads(f.read())

        self.USER =  self.get_config('EDICOM_USER')
        self.PASSWORD =  self.get_config('EDICOM_PASSWORD')

    
    def getCfdiTest(self, xml):
        
        xmlBase64 = base64.b64encode(str.encode(xml))
        stringB64 = xmlBase64.decode()
        #self.client.add_prefix('xmlns:cfdi','http://cfdi.service.ediwinws.edicom.com')
        result = self.client.service.getCfdiTest('PAP830101CR3','yqjvqfofb',stringB64)
        archivoZip = base64.b64decode(result)
        with zipfile.ZipFile(io.BytesIO(archivoZip)) as thezip:
            for zipinfo in thezip.infolist():
                with thezip.open(zipinfo) as thefile:
                    #print(thefile)
                    xmlTxt = thefile.read().decode('utf-8')
                    #print(xmlTxt)
                    return xmlTxt
                    with open(f"xml/zip/myFAc.xml",'w') as xml:
                        xml.write(xmlTxt)


    def cancelCfdi(self, cancelacion):
        #print(cancelacion)
        self.client.add_prefix('xmlns:cfdi','http://cfdi.service.ediwinws.edicom.com')
        empresa = Empresa.objects.get(id='99159e28-c969-11e7-84b5-5065f368f0c2')
        user = self.USER,
        password = self.PASSWORD
        rfcE = cancelacion["rfc_emisor"]
        rfcR = cancelacion["rfc_receptor"]
        uuid = cancelacion["uuid"]
        total = cancelacion["total"]

        cert_file = open("applications/cfdi/cfdi_sat/data/cfdiSello2020/papelCfdi2020.pfx","rb").read()
        cert = base64.b64encode(cert_file)  
        pfx= cert.decode() 
        #pfx= base64.b64encode(empresa.certificado_digital_pfx)
        pfxPassword = 'Pap315a'
        test = False
        result = self.client.service.cancelCFDiAsync(user, password, rfcE, rfcR, uuid, total, pfx, pfxPassword, test)
        #print(result)
        #archivoZip = base64.b64decode(result)
        #print(archivoZip) 

    def get_config(self,variable, config = None):
        if config ==None:
            config = self.configuration
        try:
            return config[variable]
        except:
            msg = "La Variable no Existe"
            raise ImproperlyConfigured(msg)

        