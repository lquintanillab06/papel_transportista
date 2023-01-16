import xmltodict


from ..cartaporte.cartaporte import CartaPorte

class CartaPorteXmlBuilder():
 

    # Prefijos para nodos y atributos del Xml
    prefixComprobante = "cfdi:"
    prefixNs = "xmlns:"

    def __init__(self,comprobante):
        self.comprobante = comprobante
        self.complemento = comprobante.Complemento.any[0]
        self.prefixComplemento = 'cartaporte20:'

    def build(self):
        
        # Definicion de los namespace del SAT
        cfdi = "http://www.sat.gob.mx/cfd/4"
        #pago10 = "http://www.sat.gob.mx/Pagos"
        #ine = "http://www.sat.gob.mx/ine"
        #nomina12 = "http://www.sat.gob.mx/nomina12" 
        xsi="http://www.w3.org/2001/XMLSchema-instance"
        schemaLocation="http://www.sat.gob.mx/cfd/4 http://www.sat.gob.mx/sitio_internet/cfd/4/cfdv40.xsd http://www.sat.gob.mx/CartaPorte20 http://www.sat.gob.mx/sitio_internet/cfd/CartaPorte/CartaPorte20.xsd"
        cartaporte = "http://www.sat.gob.mx/CartaPorte20"

        # Builders Nodos comprobantes
        emisor = self.buildEmisorDict()
        receptor = self.buildReceptorDict()
        conceptos = self.buildConceptosDict()
        impuestos = self.builImpuestosComprobanteDict()
        complementoDict = self.build_complemento()

        dictionaryComprobante = {
                f"{self.prefixComprobante}Comprobante":{
                "@xsi:schemaLocation": schemaLocation,
                f"@{self.prefixNs}cfdi": cfdi,
                #f"@{self.prefixNs}pago10": pago10,
                #f"@{self.prefixNs}ine": ine,
                #f"@{self.prefixNs}nomina12": nomina12 ,
                f"@{self.prefixNs}xsi": xsi,
                f"@{self.prefixNs}cartaporte20": cartaporte,
                
                "@Version": self.comprobante.Version,
                "@Serie": self.comprobante.Serie,
                "@Folio": self.comprobante.Folio,
                "@Fecha": self.comprobante.Fecha,
                "@Sello": self.comprobante.Sello,
                "@NoCertificado": self.comprobante.NoCertificado,
                "@Certificado": self.comprobante.Certificado,
                "@TipoDeComprobante": self.comprobante.TipoDeComprobante.value,
                "@SubTotal": self.comprobante.SubTotal,
                "@Descuento": self.comprobante.Descuento,
                "@Moneda":self.comprobante.Moneda.value,
                "@LugarExpedicion":self.comprobante.LugarExpedicion,
                "@FormaPago": self.comprobante.FormaPago,
                "@CondicionesDePago": self.comprobante.CondicionesDePago,
                "@MetodoPago": self.comprobante.MetodoPago,
                "@Total": self.comprobante.Total,
                "@Exportacion": self.comprobante.Exportacion,
               
                f"{self.prefixComprobante}Emisor":emisor,
                f"{self.prefixComprobante}Receptor":receptor,
                f"{self.prefixComprobante}Conceptos":conceptos,
                f"{self.prefixComprobante}Impuestos":impuestos,
                f"{self.prefixComprobante}Complemento": complementoDict
                
               
            }
        }

        xml = xmltodict.unparse(dictionaryComprobante, pretty=True)
        return xml

    def buildEmisorDict(self):
        emisor ={
        "@Rfc":self.comprobante.Emisor.Rfc,
        "@Nombre":self.comprobante.Emisor.Nombre,
        "@RegimenFiscal":self.comprobante.Emisor.RegimenFiscal
        }
        return emisor
    
    def buildReceptorDict(self):
        receptor ={
            "@Rfc":self.comprobante.Receptor.Rfc,
            "@Nombre":self.comprobante.Receptor.Nombre,
            "@UsoCFDI":self.comprobante.Receptor.UsoDeCfdi.value,
            "@RegimenFiscalReceptor": self.comprobante.Receptor.RegimenFiscalReceptor,
            "@DomicilioFiscalReceptor": self.comprobante.Receptor.DomicilioFiscalReceptor
        }
        return receptor

    def buildConceptosDict(self):
        #conceptosDict = [{ '#text':'concepto0!!!'},{ '#text':'concepto1!!!'}]
        conceptosDict = []

        for concepto in self.comprobante.Conceptos.Concepto:
            conceptoDict = self.buildConceptoDict(concepto)
            conceptosDict.append(conceptoDict)
        conceptos={
            f"{self.prefixComprobante}Concepto": conceptosDict
        }  
        return conceptos
    
    def buildConceptoDict(self, concepto):
        
        traslado = concepto.Impuestos.Traslados.Traslado[0].__dict__

        conceptoDict = {
            "@ClaveProdServ": concepto.ClaveProdServ,
            "@NoIdentificacion": concepto.NoIdentificacion,
            "@Cantidad": concepto.Cantidad,
            "@ClaveUnidad": concepto.ClaveUnidad,
            "@Unidad": concepto.Unidad,
            "@Descripcion": concepto.Descripcion,
            "@ValorUnitario": concepto.ValorUnitario,
            "@Importe": concepto.Importe,
            "@Descuento": concepto.Descuento,
            "@ObjetoImp": concepto.ObjetoImp,
        }

        conceptoDict[f"{self.prefixComprobante}Impuestos"] =  {
                f"{self.prefixComprobante}Traslados":{
                     f"{self.prefixComprobante}Traslado":{
                         "@Base": traslado['Base'],
                         "@Impuesto": traslado['Impuesto'],
                         "@TipoFactor": traslado['TipoFactor'].value,
                         "@TasaOCuota": traslado['TasaOCuota'],
                         "@Importe": traslado['Importe']
                     }
                }
            } 

        if concepto.Impuestos.Retenciones:
            retencion = concepto.Impuestos.Retenciones.Retencion[0].__dict__
            conceptoDict[f"{self.prefixComprobante}Impuestos"] =  {
                f"{self.prefixComprobante}Traslados":{
                     f"{self.prefixComprobante}Traslado":{
                         "@Base": traslado['Base'],
                         "@Impuesto": traslado['Impuesto'],
                         "@TipoFactor": traslado['TipoFactor'].value,
                         "@TasaOCuota": traslado['TasaOCuota'],
                         "@Importe": traslado['Importe']
                     }
                },
                f"{self.prefixComprobante}Retenciones":{
                        f"{self.prefixComprobante}Retencion":{
                            "@Base": retencion['Base'],
                            "@Impuesto": retencion['Impuesto'],
                            "@TipoFactor": retencion['TipoFactor'].value,
                            "@TasaOCuota": retencion['TasaOCuota'],   
                            "@Importe": retencion['Importe'] 
                    }
                }
            }
        return conceptoDict


    def builImpuestosComprobanteDict(self):
        traslado = self.comprobante.Impuestos.Traslados.Traslado
        retencion = self.comprobante.Impuestos.Retenciones.Retencion
        impuestosDict = {
                "@TotalImpuestosTrasladados": self.comprobante.Impuestos.TotalImpuestosTrasladados,
                "@TotalImpuestosRetenidos": self.comprobante.Impuestos.TotalImpuestosRetenidos,
                 f"{self.prefixComprobante}Retenciones":{
                    f"{self.prefixComprobante}Retencion":{
                        "@Impuesto": retencion.Impuesto,
                        #"@TipoFactor": retencion.TipoFactor.value,
                        #"@TasaOCuota": retencion.TasaOCuota,
                        "@Importe": retencion.Importe,
                    }
                },
                f"{self.prefixComprobante}Traslados":{
                    f"{self.prefixComprobante}Traslado":{
                        "@Impuesto": traslado.Impuesto,
                        "@TipoFactor": traslado.TipoFactor.value,
                        "@TasaOCuota": traslado.TasaOCuota,
                        "@Importe": traslado.Importe,
                        "@Base": traslado.Base
                    }
                },
               
        }
        return impuestosDict

    def build_complemento(self):
        
       
        ubicaciones = self.buildUbicacionesDict()
        mercancias = self.buildMercanciasDict()
        figuraTransporte = self.buildFiguraTransporteDict()
        complementoDict = {
                    f"{self.prefixComplemento}CartaPorte":{
                        "@Version": self.complemento.Version,
                        "@TranspInternac": self.complemento.TranspInternac,
                        "@TotalDistRec": self.complemento.TotalDistRec,
                        f"{self.prefixComplemento}Ubicaciones": ubicaciones,
                        f"{self.prefixComplemento}Mercancias": mercancias,
                        f"{self.prefixComplemento}FiguraTransporte": figuraTransporte
                    }
                }
        

        return complementoDict


    def buildUbicacionesDict(self):
        ubicacionesDict = []
        for ubicacion in self.complemento.Ubicaciones.Ubicacion:
            ubicacionDict = self.buildUbicacionDict(ubicacion)
            ubicacionesDict.append(ubicacionDict)
        ubicaciones = {
            f"{self.prefixComplemento}Ubicacion": ubicacionesDict
        }  
        return ubicaciones
        

    def buildUbicacionDict(self, ubicacion):
        ubicacionDict={
            '@TipoUbicacion': ubicacion.TipoUbicacion,
            '@IDUbicacion': ubicacion.IDUbicacion,
            '@RFCRemitenteDestinatario': ubicacion.RFCRemitenteDestinatario,
            '@FechaHoraSalidaLlegada': ubicacion.FechaHoraSalidaLlegada,
             f"{self.prefixComplemento}Domicilio":{
                 # '@Calle': ubicacion.Domicilio.Calle,
                 '@Estado': ubicacion.Domicilio.Estado,
                 '@Pais': ubicacion.Domicilio.Pais,
                 '@CodigoPostal': ubicacion.Domicilio.CodigoPostal,
                 #'@Localidad': ubicacion.Domicilio.Localidad,
                 '@Municipio': ubicacion.Domicilio.Municipio
             }  
              
        }
        if ubicacion.TipoUbicacion == 'Destino':
           ubicacionDict.update( {'@DistanciaRecorrida': ubicacion.DistanciaRecorrida})

        return ubicacionDict


    def buildMercanciasDict(self):
        mercanciasDict = []
        autoTransporte = self.complemento.Mercancias.AutoTransporte
        for mercancia in self.complemento.Mercancias.Mercancia:
            mercanciaDict = self.buildMercanciaDict(mercancia)
            mercanciasDict.append(mercanciaDict)
        mercancias = {
            "@NumTotalMercancias":self.complemento.Mercancias.NumTotalMercancias,
            "@PesoBrutoTotal":self.complemento.Mercancias.PesoBrutoTotal,
            "@UnidadPeso":"KGM",
            f"{self.prefixComplemento}Mercancia": mercanciasDict,
            f"{self.prefixComplemento}Autotransporte": {             
                        "@NumPermisoSCT": autoTransporte.NumPermisoSCT,    
                        "@PermSCT":autoTransporte.PermSCT,
                        f"{self.prefixComplemento}IdentificacionVehicular": {
                            "@AnioModeloVM":autoTransporte.IdentificacionVehicular.AnioModeloVM,
                            "@ConfigVehicular":autoTransporte.IdentificacionVehicular.ConfigVehicular,
                            "@PlacaVM":autoTransporte.IdentificacionVehicular.PlacaVM,
                        },
                        f"{self.prefixComplemento}Seguros": {
                            "@AseguraRespCivil":autoTransporte.Seguros.AseguraRespCivil,
                            "@PolizaRespCivil": autoTransporte.Seguros.PolizaRespCivil,
                        }

                    }
        }
        return mercancias

    def buildMercanciaDict(self, mercancia):
        mercanciaDict = {
            "@Cantidad":  mercancia.Cantidad,
            "@BienesTransp":mercancia.BienesTransp,
            "@Descripcion":mercancia.Descripcion,
            "@ClaveUnidad": mercancia.ClaveUnidad,
            "@Unidad": mercancia.Unidad,
            "@PesoEnKg": mercancia.PesoEnKg,
            "@ValorMercancia":mercancia.ValorMercancia,
            "@Moneda":mercancia.Moneda,
            "@MaterialPeligroso": mercancia.MaterialPeligroso,
        }

        return mercanciaDict

    def buildFiguraTransporteDict(self):
        figuraTransporteList = []

        for tipoFigura in  self.complemento.FiguraTransporte.TiposFigura:
            tipo = self.buildTipoFigura(tipoFigura)
            
            figuraTransporteList.append(tipo)
        figuraTransporteDict = {
            f"{self.prefixComplemento}TiposFigura": figuraTransporteList
        }   
        return figuraTransporteDict

    def buildTipoFigura(self, tipoFigura):

            tipoFiguraDict = {
                '@TipoFigura': tipoFigura.TipoFigura,
                '@RFCFigura': tipoFigura.RFCFigura,
                '@NombreFigura': tipoFigura.NombreFigura
            }
            if tipoFigura.TipoFigura == '01':
                tipoFiguraDict.update({'@NumLicencia': tipoFigura.NumLicencia})
            if tipoFigura.TipoFigura == '02':
                partesDict = {f"{self.prefixComplemento}PartesTransporte": {   
                            "@ParteTransporte": "PT02"
                    }
                }
                tipoFiguraDict.update(partesDict)

            return tipoFiguraDict
        

   

    
  

        
        
       
        