

class Mercancia():

    def __init__(self):


        # Pedimentos type List<Pedimentos> 
        self.Pedimentos = None

        # GuiasIdentificacion type GuiasIdentificacion
        self.GuiasIdentificacion = None

        # CantidadTransporta  type CantidadTransporta 
        self.CantidadTransporta = None 

        # DetalleMercancia type DetalleMercancia 
        self.DetalleMercancia = None

        # BienesTransp type String - required
        self.BienesTransp = None

        # ClaveSTCC type String 
        self.ClaveSTCC = None

        # Descripcion type String - required
        self.Descripcion = None

        # Cantidad type Decimal - required
        self.Cantidad = None

        # ClaveUnidad type String - required
        self.ClaveUnidad = None

        # Unidad type String 
        self.Unidad = None

        # Dimensiones  type  String
        self.Dimensiones = None

        # MaterialPeligroso type String 
        self.MaterialPeligroso = None

        # CveMaterialPeligroso type String 
        self.CveMaterialPeligroso = None

        # Embalaje type String 
        self.Embalaje = None

        # DescripEmbalaje type String 
        self.DescripEmbalaje = None

        # PesoEnKg type Decimal - required
        self.PesoEnKg = None

        # ValorMercancia type Decimal 
        self.ValorMercancia = None

        # Moneda type CMoneda 
        self.Moneda = None

        # FraccionArancelaria type String 
        self.FraccionArancelaria = None

        # UUIDComercioExt type String
        self.UUIDComercioExt = None