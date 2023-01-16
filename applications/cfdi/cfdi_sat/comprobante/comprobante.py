

class Comprobante():

   def __init__(self):
        # InformacionGlobal type InformacionGlobal
        self.InformacionGlobal = None

        # CfdiRelacionados type List<CfdiRelacionados>
        self.CfdiRelacionados = []

        # Emisor type Emisor - required
        self.Emisor = None

        # Receptor type Receptor - required
        self.Receptor = None

        # Conceptos type Conceptos
        self.Conceptos = None

        # Impuestos type Impuestos
        self.Impuestos = None

        # Complemento type Complemento
        self.Complemento = []

        #Adenda type Adenda
        self.Adenda = None

        # Version type String
        self.Version = None

        # Serie type Serie
        self.Serie = None

        # Folio type Folio
        self.Folio = None

        # Fecha type String - required
        self.Fecha = None

        # Sello type String - required
        self.Sello = None

        # FormaPago type String - required
        self.FormaPago = None

        # NoCertificado type String - required
        self.NoCertificado = None

        # Certificado type String - required
        self.Certificado = None

        # CondicionesDePago type String 
        self.CondicionesDePago = None

        # SubTotal  type Decimal - required
        self.SubTotal = None

        # Descuento type Decimal 
        self.Descuento = None

        # Moneda Type CMoneda - required
        self.Moneda = None

        # TipoCambio type Decimal 
        self.TipoCambio = None 

        # Total type Decimal - required
        self.Total = None

        # TipoDeComprobante type CTipoDeComprobante  - required
        self.TipoDeComprobante = None

        # Exportacion type String - required
        self.Exportacion = None

        # MetodoPago type CMetodoPago
        self.MetodoPago = None

        # LugarExpedicion type String - required
        self.LugarExpedicion = None

        # Confirmacion type String
        self.Confirmacion = None

