from fpdf import FPDF
from applications.commons.utils.importeALetra import  ImporteALetra
import qrcode
from tempfile import TemporaryFile
from io import BytesIO
import os, sys, zlib, struct, re, tempfile
import xml.etree.ElementTree as ET
import base64
import xmltodict

from ..models import Cfdi



def imprimir_carta_porte(cfdiId):

    #print("Ejecutando la impresion de carta porte")
    xml,cadena = getXml(cfdiId)
    pdf =  imprimir_cfdi(xml,cadena)
    return pdf

def imprimir_carta_porte_envio(cfdiId):
    
    #print("Ejecutando la impresion de carta porte")
    xml,cadena = getXml(cfdiId)
    pdf =  imprimir_cfdi(xml,cadena)
    return (pdf,xml)


def getXml(cfdiId):
    #print(cfdiId)
    cfdi = Cfdi.objects.get(pk = cfdiId )

    xml =base64.b64decode(cfdi.xml).decode()
    cadena = (cfdi.cadena)
    return (xml,cadena)

def despliegue (data):
    detalles = []
    for child in data:
        detalles.append(child.attrib)
    return detalles

def codigoGenerado(uuid,rfcE,rfcR):
    cadena = f"""https://verificacfdi.facturaelectronica.sat.gob.mx/default.aspx?id={uuid}&re={rfcE}&rr={rfcR}&tt=0.00&fe=fK7wjA=="""
    imagen = qrcode.make(cadena)
    nombre_imagen = "codigo.png"
    archivo_imagen = open(nombre_imagen,"wb")
    imagen.save(archivo_imagen)
    archivo_imagen.close()
    ruta_imagen = './' + nombre_imagen
    return nombre_imagen

class PDF(FPDF):
    # def header(self):
    #     # Logo
    #     self.image('logo.png', 10, 8, 33)
    #     # Arial bold 15
    #     self.set_font('Arial', 'B', 15)
    #     # Move to the right
    #     self.cell(80)
    #     # Title
    #     self.cell(30, 10, 'Title', 1, 0, 'C')
    #     # Line break
    #     self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-6)
        # Arial italic 8
        self.set_font('Arial', 'BI', 7)
        # Page number
        self.cell(0, 10, 'ESTE DOCUMENTO ES UNA REPRESENTACION DE UN CFDI    Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')
    
    def sprintf(self,fmt, *args): return fmt % args

    def parsejpg(self,filename,data_qr):
        fp = TemporaryFile()
        img = qrcode.make(data_qr)
        imgByteArr = BytesIO()
        img.save(imgByteArr, format='JPEG')
        fp.write(imgByteArr.getvalue())
        fp.seek(0)
        try:
                #f = open(filename, 'rb')
                f = fp
                while True:
                    markerHigh, markerLow = struct.unpack('BB', f.read(2))
                    if markerHigh != 0xFF or markerLow < 0xC0:
                        raise SyntaxError('No JPEG marker found')
                    elif markerLow == 0xDA: # SOS
                        raise SyntaxError('No JPEG SOF marker found')
                    elif (markerLow == 0xC8 or # JPG
                        (markerLow >= 0xD0 and markerLow <= 0xD9) or # RSTx
                        (markerLow >= 0xF0 and markerLow <= 0xFD)): # JPGx
                        pass
                    else:
                        dataSize, = struct.unpack('>H', f.read(2))
                        data = f.read(dataSize - 2) if dataSize > 2 else ''
                        if ((markerLow >= 0xC0 and markerLow <= 0xC3) or # SOF0 - SOF3
                            (markerLow >= 0xC5 and markerLow <= 0xC7) or # SOF4 - SOF7
                            (markerLow >= 0xC9 and markerLow <= 0xCB) or # SOF9 - SOF11
                            (markerLow >= 0xCD and markerLow <= 0xCF)): # SOF13 - SOF15
                            bpc, height, width, layers = struct.unpack_from('>BHHB', data)
                            colspace = 'DeviceRGB' if layers == 3 else ('DeviceCMYK' if layers == 4 else 'DeviceGray')
                            break
        except Exception:
            print('Error')
            #self.error('Missing or incorrect image file: %s. error: %s' % (filename, str(exception())))

        # Read whole file from the start
        f.seek(0)
        data = f.read()
        f.close()
        fp.close() 
        return {'w':width,'h':height,'cs':colspace,'bpc':bpc,'f':'DCTDecode','data':data}


    def imagenQr(self, name, x=None, y=None, w=0,h=0,type='',link='',data_qr = ''):
        if(type=='jpg' or type=='jpeg'):
            info=self.parsejpg(name, data_qr)
        info['i']=len(self.images)+1
        self.images[name]=info
        #Automatic width and height calculation if needed
        if(w==0 and h==0):
            #Put image at 72 dpi
            w=info['w']/self.k
            h=info['h']/self.k
        elif(w==0):
            w=h*info['w']/info['h']
        elif(h==0):
            h=w*info['h']/info['w']
        # Flowing mode
        if y is None:
            if (self.y + h > self.page_break_trigger and not self.in_footer and self.accept_page_break()):
                #Automatic page break
                x = self.x
                self.add_page(self.cur_orientation)
                self.x = x
            y = self.y
            self.y += h
        if x is None:
            x = self.x
        self._out(self.sprintf('q %.2f 0 0 %.2f %.2f %.2f cm /I%d Do Q',w*self.k,h*self.k,x*self.k,(self.h-(y+h))*self.k,info['i']))
        if(link):
            self.link(x,y,w,h,link)  

def imprimir_cfdi(xml,cadena):
    #print(xml)
    ns = {'cfdi': "http://www.sat.gob.mx/cfd/4" ,'cartaporte20':'http://www.sat.gob.mx/CartaPorte20','tfd': 'http://www.sat.gob.mx/TimbreFiscalDigital'}
    tree = ET.fromstring(xml) 
    comprobante = tree.attrib
    receptor = tree.find('cfdi:Receptor',ns).attrib
    emisor = tree.find('cfdi:Emisor',ns).attrib
    carta = tree.find('cfdi:Complemento/cartaporte20:CartaPorte', ns).attrib
    concepto = tree.find('.//cfdi:Concepto', ns).attrib
    conceptos = tree.findall('.//cfdi:Conceptos', ns)
    traslado = tree.find('.//cfdi:Traslado', ns).attrib
    retencion = tree.find('.//cfdi:Retencion', ns).attrib
    impuestos = tree.find('./cfdi:Impuestos', ns).attrib
    ubicaciones = tree.find('.//cartaporte20:Ubicaciones', ns)
    mercanciageneral = tree.find('.//cartaporte20:Mercancias', ns).attrib
    mercanciap = tree.findall('.//cartaporte20:Mercancia', ns)
    autotransporte = tree.find('.//cartaporte20:Autotransporte', ns).attrib
    idenVehiculo = tree.find('.//cartaporte20:IdentificacionVehicular', ns).attrib
    seguro = tree.find('.//cartaporte20:Seguros', ns).attrib
    timbrado = tree.find('.//tfd:TimbreFiscalDigital', ns).attrib
    domicilioD = tree.find('.//cartaporte20:Domicilio',ns).attrib
    listaDetalle = despliegue(ubicaciones)
    mercap = despliegue(mercanciap)

    pdf = PDF('P','cm','Letter')
    pdf.alias_nb_pages()

    pdf.add_page()

        
    pdf.set_font('Times', 'B', 7)
    #CUADRO NUMERO 1 
    pdf.rect(x=1,y=1,w=8.5,h=3.55)
    #informacion de la parte numero 2
    #pdf.image('logo.png', x=4, y=1.2, w=7,h=2.0)
    #1
    pdf.set_text_color(r= 0, g= 0, b = 0)
    pdf.cell(w=8.5,h=0.35,txt=f"{emisor['Nombre']}",align = "C", fill = 0, border=1)
    pdf.set_fill_color(r=192 , g= 192, b = 192)
    pdf.set_text_color(r= 255, g= 255, b = 255)
    pdf.cell(w=8.5,h=0.35,txt="FOLIO FISCAL (UUID)",align = "C", fill = 1,border = 1)
    pdf.cell(w=2.5,h=0.35,txt="SERIE Y FOLIO",align = "C", fill = 1,border = 1,ln=1)
    pdf.set_text_color(r= 0, g= 0, b = 0)
    pdf.cell(w=8.5,h=0.35,txt="",align = "C", fill = 0, border=0)
    #pdf.cell(w=8.5,h=0.35,txt=f"{timbrado['UUID']}",align = "C", fill = 0)
    pdf.cell(w=8.5,h=0.35,txt=f"test",align = "C", fill = 0)
    pdf.cell(w=2.5,h=0.35,txt=f"{comprobante['Serie']} - {comprobante['Folio']}",align = "C", fill = 0, ln=1,border="R")


    #2
    pdf.cell(w=8.5,h=0.35,txt="",align = "C", fill = 0)
    pdf.set_fill_color(r=192 , g= 192, b = 192)
    pdf.set_text_color(r= 255, g= 255, b = 255)
    pdf.cell(w=3.5,h=0.35,txt="FORMA PAGO",align = "C", fill = 1,border = 1)
    pdf.cell(w=3.5,h=0.35,txt="METODO PAGO",align = "C", fill = 1,border = 1)
    pdf.cell(w=4,h=0.35,txt="CONDICIONES PAGO",align = "C", fill = 1,border = 1,ln=1)

    pdf.cell(w=8.5,h=0.35,txt="",align = "C", fill = 0)
    pdf.set_fill_color(r=192 , g= 192, b = 192)
    pdf.set_text_color(r= 0, g= 0, b = 0)
    pdf.cell(w=3.5,h=0.35,txt=f"{comprobante['FormaPago']}",align = "C", fill = 0)
    pdf.cell(w=3.5,h=0.35,txt=f"{comprobante['MetodoPago']}",align = "C", fill = 0)
    valorCP=""
    if comprobante['CondicionesDePago'] == 'None':
        valorCP = ""
    else:
        valorCP = comprobante['CondicionesDePago']
    pdf.cell(w=4,h=0.35,txt=f"{valorCP}",align = "C", fill = 0,border="R",ln=1)

    #3
    pdf.cell(w=8.5,h=0.35,txt="",align = "C", fill = 0)
    pdf.set_fill_color(r=192 , g= 192, b = 192)
    pdf.set_text_color(r= 255, g= 255, b = 255)
    pdf.cell(w=11,h=0.35,txt="RECEPTOR",align = "C", fill = 1,border = 1,ln=1)

    pdf.cell(w=8.5,h=0.35,txt="",align = "C", fill = 0)
    pdf.set_fill_color(r=192 , g= 192, b = 192)
    pdf.set_text_color(r= 0, g= 0, b = 0)
    pdf.set_font('Times', 'B', 8)
    pdf.multi_cell(w=11,h=0.4,txt=f"{receptor['Nombre']} \n      R.F.C.: {receptor['Rfc']}              USO CFDI: {receptor['UsoCFDI']}"
    ,align = "C", fill = 0,border=0)
    pdf.rect(x=9.5,y=2.75,w=11,h=1.8)


    pdf.set_font('Times', 'B', 8)
    pdf.ln(1)
    # pdf.cell(w=13,h=1,txt="RFC:",align = "L", fill = 0,ln=2)
    # pdf.cell(w=13,h=1,txt="Regimen Fiscal: ",align = "L", fill = 0,ln=3)
    # pdf.cell(w=13,h=1,txt="Lugar de Expedicion: ",align = "L", fill = 0,ln=4)
    # DATOS DEL EMISOR 
    pdf.set_text_color(r= 0, g= 0, b = 0)
    rr = emisor['Rfc']
    abv = rr[0:4]
    pdf.set_font('Times', 'B', 45)
    pdf.text(x=3.3,y=2.8,txt=(f"{abv}"))
    pdf.set_font('Times', 'B', 8)
    #pdf.text(x=1.1,y=3.3,txt=f"PAPER IMPORTS S.A DE C.V")
    pdf.text(x=1.1,y=3.55,txt=f"R.F.C: {emisor['Rfc']}")
    pdf.text(x=1.1,y=3.95,txt=f"REGIMEN FISCAL: {emisor['RegimenFiscal']}")
    pdf.text(x=4.8,y=3.95,txt=f"EXPEDIDO EN: {comprobante['LugarExpedicion']}")
    pdf.text(x=1.1,y=4.35,txt=f"Ver.CFDI: {comprobante['Version']}")
    pdf.text(x=3.8,y=4.35,txt=f"FECHA: {comprobante['Fecha']}")



    #PRIMERA TABLA 
    pdf.set_text_color(r= 255, g= 255, b = 255)
    pdf.set_font('Times', 'B', 7)
    pdf.cell(w=3,h=0.35,txt="No.IDENTIFICACION",align = "C", fill = 1, border = 1)
    pdf.cell(w=1.55,h=0.35,txt="CANTIDAD",align = "C", fill = 1, border = 1)
    pdf.cell(w=2.3,h=0.35,txt="UNIDAD CLAVE",align = "C", fill = 1, border = 1)
    pdf.cell(w=7.7,h=0.35,txt="DESCRIPCION",align = "C", fill = 1, border = 1)
    pdf.cell(w=2.5,h=0.35,txt="PRECIO UNIT",align = "C", fill = 1, border = 1)
    pdf.multi_cell(w=2.45,h=0.35,txt="IMPORTE",align = "C", fill = 1, border = 1)
    pdf.set_text_color(r= 0, g= 0, b = 0)
    pdf.set_font('Times', '', 7)
    pdf.cell(w=3,h=0.35,txt=f"{concepto['NoIdentificacion']}",align = "C", fill = 0, border = 1)
    pdf.cell(w=1.55,h=0.35,txt=f"{concepto['Cantidad']}",align = "C", fill = 0, border = 1)
    pdf.cell(w=2.3,h=0.35,txt=f"{concepto['ClaveUnidad']}",align = "C", fill = 0, border = 1)
    pdf.cell(w=7.7,h=0.35,txt=f"{concepto['Descripcion']}",align = "C", fill = 0, border = 1)
    pdf.set_font('Times', 'B', 7)
    pdf.cell(w=2.5,h=0.35,txt=f"{float(concepto['ValorUnitario'])}",align = "C", fill = 0, border = 1)
    pdf.multi_cell(w=2.45,h=0.35,txt=f"{float(concepto['Importe'])}",align = "C", fill = 0, border = 1)

    pdf.set_fill_color(r=192 , g= 192, b = 192)
    pdf.set_text_color(r= 0, g= 0, b = 0)
    pdf.set_font('Times', 'B', 5)
    pdf.cell(w=0.8,h=0.22,txt="",align = "C", fill = 0, border = 0)
    pdf.cell(w=1.4,h=0.22,txt="CveProdSAT",align = "C", fill = 0, border = 1)
    pdf.cell(w=1.9,h=0.22,txt="Unidad SAT",align = "C", fill = 0, border = 1)
    pdf.cell(w=1.9,h=0.22,txt="Descto",align = "C", fill = 0, border = 1)
    pdf.cell(w=1.9,h=0.22,txt="Impuesto",align = "C", fill = 0, border = 1)
    pdf.cell(w=1.9,h=0.22,txt="TipoFactor",align = "C", fill = 0, border = 1)
    pdf.cell(w=1.9,h=0.22,txt="TasaOCuota",align = "C", fill = 0, border = 1)
    pdf.cell(w=1.9,h=0.22,txt="Base",align = "C", fill = 0, border = 1)
    pdf.cell(w=1.9,h=0.22,txt="ImprteIva",align = "C", fill = 0, border = 1,ln=1)
    pdf.set_text_color(r= 0, g= 0, b = 0)
    pdf.set_font('Times', '', 5)
    pdf.cell(w=0.8,h=0.22,txt="",align = "C", fill = 0, border = 0)
    pdf.cell(w=1.4,h=0.22,txt=f"{concepto['ClaveProdServ']}",align = "C", fill = 0,border = 1)
    pdf.cell(w=1.9,h=0.22,txt=f"{concepto['Unidad']}",align = "C", fill = 0,border = 1)
    pdf.cell(w=1.9,h=0.22,txt=f"{concepto['Descuento']}",align = "C", fill = 0,border = 1)
    pdf.cell(w=1.9,h=0.22,txt=f"{traslado['Impuesto']}",align = "C", fill = 0,border = 1)
    pdf.cell(w=1.9,h=0.22,txt=f"{traslado['TipoFactor']}",align = "C", fill = 0,border = 1)
    pdf.cell(w=1.9,h=0.22,txt=f"{traslado['TasaOCuota']}",align = "C", fill = 0,border = 1)
    pdf.cell(w=1.9,h=0.22,txt=f"{float(traslado['Base'])}",align = "C", fill = 0,border = 1)
    pdf.cell(w=1.9,h=0.22,txt=f"{traslado['Importe']}",align = "C", fill = 0,border = 1)
    
    
    #TOTALES
    pdf.ln(0.52)
    pdf.set_text_color(r= 0, g= 0, b = 0)
    pdf.set_font('Times', 'B', 7)
    pdf.cell(w=12.5,h=0.35,txt="IMPORTE CON LETRA",align = "L", fill = 0)
    pdf.cell(w=5,h=0.35,txt="SUBTOTAL",align = "R", fill = 0, )
    pdf.set_font('Times', '', 7)
    pdf.cell(w=2,h=0.35,txt=f"{float(comprobante['SubTotal'])}",align = "R", fill = 0, ln=1)

    pdf.cell(w=15.5,h=0.55,txt=f"{(ImporteALetra.convertirALetras(float(comprobante['Total'])))}",align = "L", fill = 0, border = 1)
    #pdf.cell(w=15.5,h=0.55,txt=f"{(ImporteALetra.convertirALetras(19999999))}",align = "L", fill = 0, border = 1)
    pdf.set_font('Times', 'B', 7)
    pdf.cell(w=2,h=0.35,txt="DESCUENTO",align = "R", fill = 0, border = 0 )
    pdf.set_font('Times', '', 7)
    pdf.cell(w=2,h=0.35,txt=f"{comprobante['Descuento']}",align = "R", fill = 0,ln=1)

    sbt = float(comprobante['SubTotal'])
    ivaT = float(impuestos['TotalImpuestosTrasladados'])
    sbTtl = float(sbt + ivaT)

    pdf.cell(w=12.5,h=0.35,txt="",align = "L", fill = 0, )
    pdf.set_font('Times', 'B', 7)
    pdf.cell(w=5,h=0.35,txt="SUBTOTAL 1",align = "R", fill = 0,)
    pdf.set_font('Times', '', 7)
    pdf.cell(w=2,h=0.35,txt=f"{sbTtl}",align = "R", fill = 0,ln=1)

    pdf.cell(w=12.5,h=0.35,txt="",align = "L", fill = 0, )
    pdf.set_font('Times', 'B', 7)
    pdf.cell(w=5,h=0.35,txt="I.V.A. 16%",align = "R", fill = 0,)
    pdf.set_font('Times', '', 7)
    pdf.cell(w=2,h=0.35,txt=f"{impuestos['TotalImpuestosTrasladados']}",align = "R", fill = 0, ln=1)


    pdf.cell(w=12.5,h=0.35,txt="",align = "L", fill = 0,)
    pdf.set_font('Times', 'B', 7)
    pdf.cell(w=5,h=0.35,txt="RETENCION",align = "R", fill = 0, )
    pdf.set_font('Times', '', 7)
    pdf.cell(w=2,h=0.35,txt=f"{impuestos['TotalImpuestosRetenidos']}",align = "R", fill = 0, ln=1)

    pdf.cell(w=12.5,h=0.35,txt="",align = "L", fill = 0)
    pdf.set_font('Times', 'B', 7)
    pdf.cell(w=5,h=0.35,txt="TOTAL",align = "R", fill = 0)
    pdf.set_font('Times', '', 7)
    pdf.cell(w=2,h=0.35,txt=f"{comprobante['Total']}",align = "R", fill = 0,ln=1)



    #SEGUNDA TABLA CARTA PORTE
    pdf.ln(0.22)
    pdf.set_fill_color(r=192 , g= 192, b = 192)
    pdf.set_text_color(r= 255, g= 255, b = 255)
    pdf.set_font('Times', 'B', 11)
    pdf.multi_cell(w=19.5,h=0.55,txt="CARTA PORTE",align = "C", fill = 1, border = 1)
    pdf.set_font('Times', 'B', 8)
    pdf.set_text_color(r= 0, g= 0, b = 0)
    pdf.cell(w=3.9,h=0.55,txt="Version",align = "C", fill = 1, border = 1)
    pdf.cell(w=3.9,h=0.55,txt="Transp. Internac",align = "C", fill = 1, border = 1)
    pdf.cell(w=3.9,h=0.55,txt="EntradaSalidaMerc",align = "C", fill = 1, border = 1)
    pdf.cell(w=3.9,h=0.55,txt="ViaEntradaSalida",align = "C", fill = 1, border = 1)
    pdf.multi_cell(w=3.9,h=0.55,txt="TotalDistRecorr",align = "C", fill = 1, border = 1)
    pdf.set_text_color(r= 0, g= 0, b = 0)
    pdf.set_font('Times', 'B', 8)
    pdf.cell(w=3.9,h=0.55,txt=f"{carta['Version']}",align = "C", fill = 0, border = 1)
    pdf.cell(w=3.9,h=0.55,txt=f"{carta['TranspInternac']}",align = "C", fill = 0, border = 1)
    pdf.cell(w=3.9,h=0.55,txt="",align = "C", fill = 0, border = 1)
    pdf.cell(w=3.9,h=0.55,txt="",align = "C", fill = 0, border = 1)
    pdf.multi_cell(w=3.9,h=0.55,txt=f"{carta['TotalDistRec']}",align = "C", fill = 0, border = 1)


    #TERCERA TABLA UBICACIONES 
    pdf.ln(0.3)
    pdf.set_fill_color(r=192 , g= 192, b = 192)
    pdf.set_text_color(r= 255, g= 255, b = 255)
    pdf.set_font('Times', 'B', 11)
    pdf.multi_cell(w=19.5,h=0.55,txt="UBICACIONES",align = "C", fill = 1, border = 1)
    pdf.set_font('Times', 'B', 8)
    pdf.set_text_color(r= 0, g= 0, b = 0)
    pdf.multi_cell(w=19.5,h=0.55,txt="DISTANCIA RECORRIDA",align = "L", fill = 1, border = 1)
    pdf.multi_cell(w=19.5,h=0.55,txt=f"{listaDetalle[1]['DistanciaRecorrida']}",align = "L", fill = 0, border = 0)

    pdf.cell(w=6.5,h=0.7,txt="ORIGEN",align = "C", fill = 1)
    pdf.cell(w=6.5,h=0.7,txt="DESTINO",align = "C", fill = 1)
    pdf.multi_cell(w=6.5,h=0.7,txt="DOMICILIO",align = "C", fill = 1)

    pdf.cell(w=6.5,h=0.7,txt=f"IdOrigen:  {listaDetalle[0]['IDUbicacion']}",align = "L", fill = 0)
    pdf.cell(w=6.5,h=0.7,txt=f"IdDestino:  {listaDetalle[1]['IDUbicacion']}",align = "L", fill = 0)
    # pdf.multi_cell(w=6.5,h=0.7,txt=f"Calle: {domicilioD['Calle']}",align = "L", fill = 0)
    pdf.multi_cell(w=6.5,h=0.7,txt=f"Calle: ",align = "L", fill = 0)

    pdf.cell(w=6.5,h=0.7,txt=f"RFC:  {listaDetalle[0]['RFCRemitenteDestinatario']}",align = "L", fill = 0)
    pdf.cell(w=6.5,h=0.7,txt=f"RFC:  {listaDetalle[1]['RFCRemitenteDestinatario']}",align = "L", fill = 0)
    pdf.multi_cell(w=6.5,h=0.7,txt=f"C.P:  {domicilioD['CodigoPostal']} ",align = "L", fill = 0)

    pdf.cell(w=6.5,h=0.7,txt=f"FechaSalida:  {listaDetalle[0]['FechaHoraSalidaLlegada']}",align = "L", fill = 0)
    pdf.cell(w=6.5,h=0.7,txt=f"FechaEntrada:  {listaDetalle[1]['FechaHoraSalidaLlegada']}",align = "L", fill = 0)
    pdf.multi_cell(w=6.5,h=0.7,txt=f"Municipio:  {domicilioD['Municipio']} ",align = "L", fill = 0)

    pdf.cell(w=6.5,h=0.7,txt="",align = "C", fill = 0)
    pdf.cell(w=6.5,h=0.7,txt="",align = "C", fill = 0)
    pdf.multi_cell(w=6.5,h=0.7,txt=f"Estado:  {domicilioD['Estado']}  Pais:  {domicilioD['Pais']} ",align = "L", fill = 0)
   

    #MERCANCIAS
    pdf.ln(0.22)
    pdf.set_fill_color(r=192 , g= 192, b = 192)
    pdf.set_text_color(r= 255, g= 255, b = 255)
    pdf.multi_cell(w=19.5,h=0.55,txt="MERCANCIAS",align = "C", fill = 1, border = 1)
    pdf.set_font('Times', 'B', 8)
    pdf.set_text_color(r= 0, g= 0, b = 0)
    txtMercancia = f"""PESO BRUTO TOTAL:  {mercanciageneral['PesoBrutoTotal']}                      UNIDAD PESO: {mercanciageneral['UnidadPeso']}                    NUM TOTAL MERCANCIAS: {mercanciageneral['NumTotalMercancias']}"""
    pdf.multi_cell(w=19.5,h=0.75,txt=f"{txtMercancia}",align = "C", fill = 0, border = 1)


    #MERCANCIA
    pdf.ln(0.3)
    pdf.set_fill_color(r=192 , g= 192, b = 192)
    pdf.set_text_color(r= 255, g= 255, b = 255)
    pdf.multi_cell(w=19.5,h=0.55,txt="MERCANCIA",align = "C", fill = 1, border = 1)
    pdf.set_font('Times', 'B', 8)
    pdf.set_text_color(r= 0, g= 0, b = 0)

    pdf.set_font('Times', 'B', 7)
    pdf.cell(w=1.6,h=0.35,txt="BienesTransp",align = "C", fill = 1, border = 1)
    pdf.cell(w=1.25,h=0.35,txt="Cantidad",align = "C", fill = 1, border = 1)
    pdf.cell(w=1.6,h=0.35,txt="Clave Unidad",align = "C", fill = 1, border = 1)
    pdf.cell(w=9.15,h=0.35,txt="Descripcion",align = "C", fill = 1, border = 1)
    pdf.cell(w=1.4,h=0.35,txt="UnidadSAT",align = "C", fill = 1, border = 1)
    pdf.cell(w=1.3,h=0.35,txt="Peso KG.",align = "C", fill = 1, border = 1)
    pdf.cell(w=1.2,h=0.35,txt="Moneda",align = "C", fill = 1, border = 1)
    pdf.multi_cell(w=2,h=0.35,txt="ValorMercancia",align = "C", fill = 1, border = 1)

    for id in range(len(mercap)):

        pdf.set_text_color(r= 0, g= 0, b = 0)
        pdf.set_font('Times', '', 7)
        pdf.cell(w=1.6,h=0.35,txt=f"{mercap[id]['BienesTransp']}",align = "C", fill = 0, border = 1)
        pdf.cell(w=1.25,h=0.35,txt=f"{mercap[id]['Cantidad']}",align = "C", fill = 0, border = 1)
        pdf.cell(w=1.6,h=0.35,txt=f"{mercap[id]['ClaveUnidad']}",align = "C", fill = 0, border = 1)
        pdf.cell(w=9.15,h=0.35,txt=f"{mercap[id]['Descripcion']}",align = "C", fill = 0, border = 1)
        pdf.cell(w=1.4,h=0.35,txt=f"{mercap[id]['Unidad']}",align = "C", fill = 0,border = 1)
        pdf.cell(w=1.3,h=0.35,txt=f"{mercap[id]['PesoEnKg']}",align = "C", fill = 0,border = 1)
        pdf.cell(w=1.2,h=0.35,txt=f"{mercap[id]['Moneda']}",align = "C", fill = 0, border = 1)
        pdf.multi_cell(w=2,h=0.35,txt=f"{mercap[id]['ValorMercancia']}",align = "C", fill = 0, border = 1)

        pdf.ln(0.25)

    #AUTOTRANSPORTE    
    pdf.ln(0.22)
    pdf.set_fill_color(r=192 , g= 192, b = 192)
    pdf.set_text_color(r= 255, g= 255, b = 255)
    pdf.set_font('Times', 'B', 9)
    pdf.multi_cell(w=19.5,h=0.55,txt="AUTOTRANSPORTE",align = "C", fill = 1, border = 1)
    pdf.set_font('Times', 'B', 8)
    pdf.set_text_color(r= 0, g= 0, b = 0)
    txtMercancia = f"""PermSCT:  {autotransporte['PermSCT']}                      NumPermisoSCT: {autotransporte['NumPermisoSCT']}                    Nombre Aseguradora: {seguro['AseguraRespCivil']}          NumPolizaSeguro: {seguro['PolizaRespCivil']} """
    pdf.multi_cell(w=19.5,h=0.75,txt=f"{txtMercancia}",align = "C", fill = 0, border = 1)

    #IDENTIFICACION VEHICULAR
    pdf.ln(0.22)
    pdf.set_fill_color(r=192 , g= 192, b = 192)
    pdf.set_text_color(r= 255, g= 255, b = 255)
    pdf.set_font('Times', 'B', 9)
    pdf.multi_cell(w=19.5,h=0.55,txt="IDENTIFICACION VEHICULAR",align = "C", fill = 1, border = 1)
    pdf.set_font('Times', 'B', 8)
    pdf.set_text_color(r= 0, g= 0, b = 0)
    txtMercancia = f"""Config:  {idenVehiculo['ConfigVehicular']}                      PlacaVM: {idenVehiculo['PlacaVM']}                    AnioModeloVM: {idenVehiculo['AnioModeloVM']}"""
    pdf.multi_cell(w=19.5,h=0.75,txt=f"{txtMercancia}",align = "C", fill = 0, border = 1)
    
    #print(pdf.get_x())

    if (len(mercap)) <=22:
        pdf.set_auto_page_break(True, margin = 5)#5 y 2
    else:
        pdf.set_auto_page_break(True, margin = 2)#5 y 2
    #nn = codigoGenerado(timbrado['UUID'],emisor['Rfc'],receptor['Rfc'])
    pdf.ln(0.22)
    pdf.cell(w=0,h=0.55,txt="",align = "C", fill = 0)
    pdf.imagenQr("codigoqr.jpg", x = 1, y = None, w = 5, h = 5,type="jpg",
    data_qr=f"""https://verificacfdi.facturaelectronica.sat.gob.mx/default.aspx?id={timbrado['UUID']}&re={emisor['Rfc']}&rr={receptor['Rfc']}&tt=0.00&fe=fK7wjA==""")
    #data_qr=f"""https://verificacfdi.facturaelectronica.sat.gob.mx/default.aspx?re={emisor['Rfc']}&rr={receptor['Rfc']}&tt=0.00&fe=fK7wjA==""")
    yy = pdf.get_y() - 3.5
    #pdf.text(x=1,y=None,txt="prueba de texto")
    pdf.set_text_color(r=0,g=0,b=0)
    pdf.set_font('Times', 'B', 8)
    pdf.text(x=7,y=yy,txt="R.F.C. PROV. CERTIF :")
    pdf.set_font('Times', '', 8)
    pdf.text(x=10.5,y=yy,txt=f"{timbrado['RfcProvCertif']}")
    #pdf.text(x=10.5,y=yy,txt=f"test")

    pdf.set_font('Times', 'B', 8)
    pdf.text(x=7,y=(yy+0.5),txt="TIPO DE DOCUMENTO :")
    pdf.set_font('Times', '', 8)
    if (comprobante['TipoDeComprobante'] == "I"):
        pdf.text(x=10.5,y=(yy+0.5),txt=f"INGRESO")
    else:
        pdf.text(x=10.5,y=(yy+0.5),txt=f"{comprobante['TipoDeComprobante']}")
    pdf.set_font('Times', 'B', 8)
    pdf.text(x=7,y=(yy+1),txt="FECHA TIMBRADO :")
    pdf.set_font('Times', '', 8)
    pdf.text(x=10.5,y=(yy+1),txt=f"{timbrado['FechaTimbrado']}")
    #pdf.text(x=10.5,y=(yy+1),txt=f"test")

    pdf.set_font('Times', 'B', 8)
    pdf.text(x=7,y=(yy+1.5),txt="CERTIFICADO SAT :")
    pdf.set_font('Times', '', 8)
    pdf.text(x=10.5,y=(yy+1.5),txt=f"{timbrado['NoCertificadoSAT']}")
    #pdf.text(x=10.5,y=(yy+1.5),txt=f"test")

    pdf.set_font('Times', 'B', 8)
    pdf.text(x=7,y=(yy+2),txt="CERTIFICADO EMISOR :")
    pdf.set_font('Times', '', 8)
    pdf.text(x=10.5,y=(yy+2),txt=f"{comprobante['NoCertificado']}")

    pdf.ln(0.2)
    pdf.set_font('Times', 'B', 10)
    pdf.cell(w=5,h=0.55,txt="SELLO DIGITAL DEL CFDI:",ln=1)
    pdf.set_font('Times', '', 5)
    pdf.multi_cell(w=19.5,h=0.35,txt=f"{timbrado['SelloCFD']}",
    #pdf.multi_cell(w=19.5,h=0.35,txt=f"test",
    border=1,align="J")

    pdf.set_font('Times', 'B', 10)
    pdf.cell(w=5,h=0.55,txt="SELLO DIGITAL DEL SAT:",ln=1)
    pdf.set_font('Times', '', 5)
    pdf.multi_cell(w=19.5,h=0.35,txt=f"{timbrado['SelloSAT']}",
    #pdf.multi_cell(w=19.5,h=0.35,txt=f"test",
    border=1,align="J")

    pdf.set_font('Times', 'B', 10)
    pdf.cell(w=5,h=0.55,txt="CADENA ORIGINAL DEL COMPLEMENTO DE CERTIFICACION DIGITAL DEL SAT:",ln=1)
    pdf.set_font('Times', '', 5)
    pdf.multi_cell(w=19.5,h=0.35,txt=f"{cadena}",
    #pdf.multi_cell(w=19.5,h=0.35,txt=f"Texto cadena",
    border=1,align="L")

    reporte = pdf.output(dest='S').encode('latin-1')
    return reporte
    

