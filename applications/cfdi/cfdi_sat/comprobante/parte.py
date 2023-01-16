


class Parte():

    def __init__(self):

        # InformacionAduanera type List<InformacionAduaneraP>
        self.InformacionAduanera = None

        # ClaveProdServ type String - required
        self.ClaveProdServ = None

        # NoIdentificacion type String 
        self.NoIdentificacion = None

        # Cantidad type Decimal - required 
        self.Cantidad = None

        # Unidad type  String 
        self.Unidad = None

        # Descripcion type String - required
        self.Descripcion = None

        # ValorUnitario type Decimal 
        self.ValorUnitario = None

        # Importe type Decimal 
        self.Importe = None