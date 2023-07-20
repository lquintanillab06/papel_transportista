from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import  pkcs1_15
import base64
import hashlib
import uuid

#from applications.core.models import Empresa

from applications.transportista.models import FacturistaEmbarques

class CfdiSellador():
   
   def sellar_oldy(self,cadenaOriginal):
             
      # print ("---------- Cadena ---------------")
      # print(cadenaOriginal)
      ''' cert_file = open("applications/cfdi/cfdi_sat/data/jol/00001000000516081309.cer","rb").read()
      cert = base64.b64encode(cert_file) '''
      # print("____________ Cert Base 64 ____________")
      # print(cert.decode("utf-8"))
      key = open("applications/cfdi/cfdi_sat/data/jol/JOL_2022.key","rb").read()
      rsakey = RSA.importKey(key)
      # print("_____________ KEY ______________________")
      # print(rsakey)
      # print("_____________ Digest ______________________")
      cadenaB = bytes(str(cadenaOriginal), 'utf-8')
      hash = SHA256.new(cadenaB)
      # print(hash.digest())
      # print("______ Firma____________________________")
      signature = pkcs1_15.new(rsakey).sign(hash)
      firma = base64.b64encode(signature)
      # print(firma.decode("utf-8"))
      # print("______ Firma____________________________")
      #firma = base64.b64encode(rsakey.encrypt(digest,None)[0])
      #comprobante.Certificado = cert.decode("utf-8")
      return firma.decode("utf-8")

      #return comprobante

   def getCertificado(self):
      cert_file = open("applications/cfdi/cfdi_sat/data/jol/00001000000516081309.cer","rb").read()
      cert = base64.b64encode(cert_file)
      return cert.decode("utf-8")

   def getCertificado2(self, certificado_digital):
      # print("Obteniendo el certificado desde la base de datos")
      cert_file = certificado_digital
      cert = base64.b64encode(cert_file)
      return cert.decode("utf-8")

   def sellar2(self,cadenaOriginal, llave_privada):
             
      # print("Obteniendo la llave privada desde la Base de Datos")
      key = llave_privada
      rsakey = RSA.importKey(key)
      cadenaB = bytes(str(cadenaOriginal), 'utf-8')
      hash = SHA256.new(cadenaB)
      signature = pkcs1_15.new(rsakey).sign(hash)
      firma = base64.b64encode(signature)
      return firma.decode("utf-8")

      #return comprobante


   def sellar_old(self,cadenaOriginal, comprobante):
             
      #print ("---------- Cadena ---------------")
      #print(cadenaOriginal)
      cert_file = open("applications/cfdi/cfdi_sat/data/jol/00001000000516081309.cer","rb").read()
      cert = base64.b64encode(cert_file)
      #print("____________ Cert Base 64 ____________")
      #print(cert.decode("utf-8"))
      key = open("applications/cfdi/cfdi_sat/data/jol/JOL_2022.key","rb").read()
      rsakey = RSA.importKey(key)
      #print("_____________ KEY ______________________")
      #print(rsakey)
      #print("_____________ Digest ______________________")
      cadenaB = bytes(str(cadenaOriginal), 'utf-8')
      hash = SHA256.new(cadenaB)
      #print(hash.digest())
      #print("______ Firma____________________________")
      signature = pkcs1_15.new(rsakey).sign(hash)
      firma = base64.b64encode(signature)
      #print(firma.decode("utf-8"))
      #print("______ Firma____________________________")
      #firma = base64.b64encode(rsakey.encrypt(digest,None)[0])
      comprobante.Certificado = cert.decode("utf-8")
      comprobante.Sello = firma.decode("utf-8")
      

      return comprobante
   
   def sellar(self,cadenaOriginal, comprobante, facturista):
      cert_file = facturista.certificado_digital
      cert = base64.b64encode(cert_file)
      key = facturista.llave_privada
      rsakey = RSA.importKey(key)
      cadenaB = bytes(str(cadenaOriginal), 'utf-8')
      hash = SHA256.new(cadenaB)
      signature = pkcs1_15.new(rsakey).sign(hash)
      firma = base64.b64encode(signature)
      comprobante.Certificado = cert.decode("utf-8")
      comprobante.Sello = firma.decode("utf-8")
      return comprobante


    
