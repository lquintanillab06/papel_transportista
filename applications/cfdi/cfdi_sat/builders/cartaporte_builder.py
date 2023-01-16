
from ..cartaporte import CartaPorte,Ubicaciones,Ubicacion,Domicilio,Mercancias,Mercancia,AutoTransporte,IdentificacionVehicular,Seguros,TiposFigura,FiguraTransporte
from ..comprobante import  (Comprobante,Emisor,Receptor,Conceptos,Concepto,Impuestos,Traslados,Traslado,Retenciones,Retencion,Complemento,
                            Impuestos10,Traslados10,Traslado10,Retenciones10,Retencion10)
from ..catalogos import CTipoDeComprobante,CUsoCFDI,CTipoFactor
from ....commons.utils.dateUtils import DateUtils
from ....commons.utils.monedaUtils import MonedaUtils
from ....core.models import Folio
from ....transportista.models import CodigosPostalesMX, InstruccionDeEnvio



class CartaPorteBuilder():

    def __init__(self, embarque):
        self.comprobante = Comprobante()
        self.embarque = embarque
        self.total_impuestos_trasladados = 0.00
        self.total_impuestos_retenidos = 0.00
        self.total_distancia_recorrida = 0
        self.subtotal  = 0.00
        self.base_traslados = 0.00
        self.kilos = 0
        self.valor = 0
        self.complemento = None
        self.carta_porte = None
        self.total_peso_bruto = 0
        self.total_mercancias = 0

    def build(self):
        self.build_comprobante()
        self.build_emisor()
        self.build_receptor()
        self.build_conceptos()
        self.build_impuestos_comprobante()
        self.build_complemento_cartaporte()
        self.build_totales()

        return self.comprobante

    def build_comprobante(self):
        serie_cfdi = self.embarque.facturista.serie_cfdi
        self.comprobante.Version = self.embarque.facturista.version_de_cfdi
        self.comprobante.NoCertificado = '00001000000516081309'
        self.comprobante.TipoDeComprobante = CTipoDeComprobante.I
        self.comprobante.Serie = serie_cfdi
        self.comprobante.Fecha = DateUtils.getNowFormatted()
        self.comprobante.Moneda = MonedaUtils.monedaResolve('MXN')
        self.comprobante.Folio = Folio.objects.get_next_folio(serie_cfdi)
        self.comprobante.Exportacion = "01"
        self.comprobante.LugarExpedicion = self.embarque.sucursal.direccion_codigo_postal
        self.comprobante.FormaPago = "99"
        self.comprobante.MetodoPago = "PPD"

    def build_emisor(self):
        facturista = self.embarque.facturista
        emisor = Emisor()
        emisor.Rfc =facturista.rfc
        emisor.Nombre = facturista.razon_social
        emisor.RegimenFiscal = facturista.regimen_fiscal
        self.comprobante.Emisor = emisor


    def build_receptor(self):
        cliente = self.embarque.cliente
        receptor = Receptor()
        receptor.Rfc = cliente.rfc
        receptor.Nombre = cliente.razon_social
        receptor.UsoDeCfdi = CUsoCFDI.S_01
        receptor.DomicilioFiscalReceptor = cliente.direccion_codigo_postal
        receptor.RegimenFiscalReceptor = cliente.regimen_fiscal
        self.comprobante.Receptor = receptor

    def build_conceptos(self):
 
        comision = 0
        for envio in self.embarque.envios.all():
            self.kilos += envio.kilos
            self.valor += round(float(envio.importe_comision),2)
            self.subtotal = round(float(self.valor),2)

        conceptos = Conceptos()
        concepto = Concepto()
        concepto.ClaveProdServ = '78101802'
        concepto.NoIdentificacion = 'Traslado de mercancias'
        concepto.Cantidad = 1
        concepto.ClaveUnidad = 'E48'
        concepto.Unidad = 'Pieza'
        concepto.Descripcion = 'Servicio de Traslado de Papel para la industria gráfica'
        concepto.ValorUnitario = round(float(self.valor),2)
        concepto.Descuento  = 0.00
        concepto.Importe = round(float(self.valor),2)
        concepto.ObjetoImp = '02'

        concepto.Impuestos = self.build_impuestos_concepto()

        conceptos.Concepto.append(concepto)
        self.comprobante.Conceptos = conceptos

    def build_impuestos_concepto(self):
        impuestos_concepto = Impuestos()
        traslados = Traslados()
        traslado =  self.build_traslado_concepto()
        traslados.Traslado.append(traslado)
        retenciones = Retenciones()
        retencion = self.build_retencion_iva_concepto()
        retenciones.Retencion.append(retencion)

        impuestos_concepto.Traslados = traslados
        impuestos_concepto.Retenciones = retenciones

        return impuestos_concepto
        

    def build_traslado_concepto(self):
        trasladoConcepto = Traslado()
        trasladoConcepto.Base =round(float(self.valor),2)
        trasladoConcepto.Impuesto = '002'
        trasladoConcepto.TipoFactor = CTipoFactor.TASA
        trasladoConcepto.TasaOCuota = '0.160000'
        trasladoConcepto.Importe = round(float(self.valor) * 0.16 ,2)
        
        #
        self.total_impuestos_trasladados = trasladoConcepto.Importe
        self.base_traslados = self.valor

        return trasladoConcepto

    def build_retencion_iva_concepto(self):
        retencionIvaConcepto = Retencion()
        retencionIvaConcepto.Base = round(float(self.valor),2)
        retencionIvaConcepto.Impuesto = '002'
        retencionIvaConcepto.TipoFactor = CTipoFactor.TASA
        retencionIvaConcepto.TasaOCuota = '0.040000'
        retencionIvaConcepto.Importe = round(float(self.valor) * 0.04 ,2)

        #
        self.total_impuestos_retenidos = retencionIvaConcepto.Importe

        return retencionIvaConcepto
        

    def build_retencion_isr_concepto(self):
        pass


    def build_impuestos_comprobante(self):

        impuestos10 = Impuestos10()
        #
        impuestos10.TotalImpuestosTrasladados = self.total_impuestos_trasladados
        impuestos10.TotalImpuestosRetenidos = self.total_impuestos_retenidos
        traslados10 = Traslados10()
        traslado10 = Traslado10()
        traslado10.Impuesto = '002'
        traslado10.TipoFactor = CTipoFactor.TASA
        traslado10.TasaOCuota = '0.160000'

        traslado10.Importe = self.total_impuestos_trasladados
        traslado10.Base = round(float(self.base_traslados),2)


        impuestos10.Traslados = traslados10
        traslados10.Traslado = traslado10


        retenciones10 = Retenciones10()
        retencion10 = Retencion10()
        retencion10.Impuesto = '002'
        #retencion10.TipoFactor = CTipoFactor.TASA
        #retencion10.TasaOCuota = '0.040000'
        #
        retencion10.Importe = self.total_impuestos_retenidos
        impuestos10.Retenciones = retenciones10
        retenciones10.Retencion = retencion10

        self.comprobante.Impuestos = impuestos10

        
    def build_totales(self):
        self.comprobante.Total = round(float(self.subtotal)+ float(self.total_impuestos_trasladados)  - float(self.total_impuestos_retenidos),2)
        self.comprobante.SubTotal = round(float(self.subtotal),2)
        self.comprobante.Descuento = 0.00

    def build_certificado(self):
        pass


    def build_complemento_cartaporte(self):
        complemento_cp = Complemento() 
        self.carta_porte = CartaPorte()
        self.carta_porte.Version = '2.0'
        self.carta_porte.TranspInternac = 'No'
        self.build_ubicaciones_cartaporte()
        self.carta_porte.TotalDistRec = self.total_distancia_recorrida
        self.build_mercancias_cartaporte()
        self.build_figura_transporte()
        complemento_cp.any.append(self.carta_porte)
        self.comprobante.Complemento = complemento_cp

    def build_ubicaciones_cartaporte(self):
        ubicaciones = Ubicaciones()
        ubicacion_origen = Ubicacion()
        ubicacion_origen.TipoUbicacion = 'Origen'
        ubicacion_origen.FechaHoraSalidaLlegada = DateUtils.cfdiDate(self.embarque.or_fecha_hora_salida)
        ubicacion_origen.IDUbicacion = self.embarque.or_origen
        ubicacion_origen.RFCRemitenteDestinatario = self.embarque.or_rfc_remitente
        ubicacion_origen.DistanciaRecorrida = self.embarque.cp_total_distancia_recorrida
        domicilio_ubicacion_origen = Domicilio()

        codigo_postal_origen = get_codigo_postal_sat(self.embarque.sucursal.direccion_codigo_postal, self.embarque.sucursal.direccion_colonia)

        domicilio_ubicacion_origen.CodigoPostal = codigo_postal_origen.codigo_sat
        domicilio_ubicacion_origen.Estado = codigo_postal_origen.estado_sat
        domicilio_ubicacion_origen.Pais = 'MEX'
        #
        domicilio_ubicacion_origen.Localidad = codigo_postal_origen.localidad_sat
        domicilio_ubicacion_origen.Municipio = codigo_postal_origen.municipio_sat
        ubicacion_origen.Domicilio = domicilio_ubicacion_origen
        ubicaciones.Ubicacion.append(ubicacion_origen)
        for envio in self.embarque.envios.all():
            ubicacion_destino = Ubicacion()
            ubicacion_destino.TipoUbicacion = 'Destino'
            ubicacion_destino.FechaHoraSalidaLlegada = DateUtils.cfdiDate(self.embarque.or_fecha_hora_salida)
            ubicacion_destino.IDUbicacion = envio.de_destino
            ubicacion_destino.RFCRemitenteDestinatario = envio.de_rfc_destinatario
            domicilio_ubicacion_destino = Domicilio()
            instruccion = InstruccionDeEnvio.objects.get(envio = envio)
            self.total_distancia_recorrida += instruccion.ub_distancia_recorrida
            ubicacion_destino.DistanciaRecorrida = instruccion.ub_distancia_recorrida
            codigo_postal_destino = get_codigo_postal_sat(instruccion.direccion_codigo_postal, instruccion.direccion_colonia)
            domicilio_ubicacion_destino.CodigoPostal = codigo_postal_destino.codigo_sat
            domicilio_ubicacion_destino.Estado = codigo_postal_destino.estado_sat
            domicilio_ubicacion_destino.Pais = 'MEX'
            domicilio_ubicacion_destino.Localidad = codigo_postal_destino.localidad_sat
            domicilio_ubicacion_destino.Municipio = codigo_postal_destino.municipio_sat
            ubicacion_destino.Domicilio = domicilio_ubicacion_destino
            ubicaciones.Ubicacion.append(ubicacion_destino)

        self.carta_porte.Ubicaciones = ubicaciones

    def build_mercancias_cartaporte(self):
        mercancias = Mercancias()
        mercancias.UnidadPeso = self.embarque.me_unidad_peso

        for envio in self.embarque.envios.all():
            for envio_det in envio.enviosdet.all():
                mercancia = Mercancia()
                mercancia.Cantidad  = envio_det.me_cantidad
                mercancia.BienesTransp = envio_det.me_bienes_transp
                mercancia.Descripcion = envio_det.me_descripcion
                mercancia.Cantidad = envio_det.me_cantidad
                mercancia.ClaveUnidad = envio_det.me_clave_unidad
                mercancia.Unidad = envio_det.me_unidad
                mercancia.MaterialPeligroso = 'No'
                mercancia.PesoEnKg = envio_det.me_kilos
                mercancia.ValorMercancia = envio_det.valor
                mercancia.Moneda = envio_det.moneda
                mercancias.Mercancia.append(mercancia)

                self.total_peso_bruto += envio_det.me_kilos
                self.total_mercancias += 1
                

        mercancias.PesoBrutoTotal = round(float(self.total_peso_bruto),2)
        mercancias.NumTotalMercancias = self.total_mercancias

        autotransporte = self.build_autotransporte()
        mercancias.AutoTransporte = autotransporte
        self.carta_porte.Mercancias = mercancias

    def build_autotransporte(self):
        autotransporte = AutoTransporte()
        transporte =self.embarque.operador.transporte
        autotransporte.PermSCT = transporte.af_perm_sct
        autotransporte.NumPermisoSCT = transporte.af_num_permiso_sct
        identificacionVehicular = IdentificacionVehicular()
        identificacionVehicular.ConfigVehicular = transporte.iv_config_vehicular
        identificacionVehicular.PlacaVM = transporte.iv_placa_vm
        identificacionVehicular.AnioModeloVM = transporte.iv_anio_modelo
        autotransporte.IdentificacionVehicular = identificacionVehicular
        seguros = Seguros()
        seguros.AseguraRespCivil = transporte.af_nombre_aseg
        seguros.PolizaRespCivil = transporte.af_num_poliza_seguro
        autotransporte.Seguros = seguros

        return autotransporte

    def build_figura_transporte(self):
        figura_transporte = FiguraTransporte()
        operador = self.build_operador()
        figura_transporte.TiposFigura .append(operador)
        propietario = self.build_propietario()
        if propietario.RFCFigura != operador.RFCFigura:
            figura_transporte.TiposFigura .append(propietario)

        self.carta_porte.FiguraTransporte = figura_transporte 
     

    def build_operador(self):
        operador = TiposFigura()
        operador.TipoFigura = '01'
        operador.RFCFigura = self.embarque.operador.rfc
        operador.NumLicencia = self.embarque.operador.num_licencia
        operador.NombreFigura = self.embarque.operador.nombre
        return operador



    def build_propietario(self):
        propietario = TiposFigura()
        
        propietario.TipoFigura = '02'
        propietario.RFCFigura = self.embarque.operador.transporte.propietario.rfc
        propietario.NombreFigura = self.embarque.operador.transporte.propietario.nombre
        
        return propietario


def get_codigo_postal_sat(codigo_postal, colonia):
    #print(codigo_postal,colonia, sep="-")
    codigo = CodigosPostalesMX.objects.get(codigo = codigo_postal, colonia = colonia)
    return codigo

      
