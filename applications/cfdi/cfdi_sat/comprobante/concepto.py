

class Concepto():

    def __init__(self):
        # Impuestos type Impuestos 
        self.Impuestos = None

        # ACuentaTerceros type ACuentaTerceros 
        self.ACuentaTerceros = None

        # InformacionAduanera type InformacionAduanera 
        self.InformacionAduanera = None

        # CuentaPredial type  CuentaPredial 
        self.CuentaPredial = None

        # ComplementoConcepto type ComplementoConcepto
        self.ComplementoConcepto = None

        #Parte type Parte
        self.Parte = None

        # ClaveProdServ type String - required
        self.ClaveProdServ = None

        # NoIdentificacion type String - required
        self.NoIdentificacion = None

        # Cantidad  type Decimal - required
        self.Cantidad = None

        # ClaveUnidad type String - required
        self.ClaveUnidad = None

        # Unidad type String
        self.Unidad = None

        # Descripcion type String - required
        self.Descripcion = None

        # ValorUnitario type Decimal - required
        self.ValorUnitario = None

        # Importe type Decimal - required
        self.Importe = None

        # Descuento type Decimal 
        self.Descuento = None

        # ObjetoImp type String - required
        self.ObjetoImp = None
