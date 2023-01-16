

class CartaPorte():

    def __init__(self):

        # Ubicaciones type Ubicaciones
        self.Ubicaciones = None

        # Mercancias type Mercancias - required
        self.Mercancias = None

        # FiguraTransporte type FiguraTransporte - required
        self.FiguraTransporte = None

        # Version type String - required
        self.Version = None

        # TranspInternac type String - required
        self.TranspInternac = None

        # EntradaSalidaMerc type String 
        self.EntradaSalidaMerc = None

        #PaisOrigenDestino type CPais
        self.PaisOrigenDestino = None

        # ViaEntradaSalida type String
        self.ViaEntradaSalida = None

        # TotalDistRec type Decimal
        self.TotalDistRec = None