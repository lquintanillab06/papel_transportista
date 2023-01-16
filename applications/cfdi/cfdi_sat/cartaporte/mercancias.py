


class Mercancias():

    def __init__(self):

        # Mercancia type List<Mercancia> - required
        self.Mercancia = []

        # AutoTransporte type AutoTransporte
        self.AutoTransporte = None

        # TransporteMaritimo type TransporteMaritimo 
        self.TransporteMaritimo = None

        # TransporteAereo type TransporteAereo 
        self.TransporteAereo = None

        # TransporteFerroviario type TransporteFerroviario
        self.TransporteFerroviario = None

        # PesoBrutoTotal type Decimal - required
        self.PesoBrutoTotal = None

        # UnidadPeso type String - required
        self.UnidadPeso = None 

        # PesoNetoTotal type Decimal
        self.PesoNetoTotal = None
        
        # NumTotalMercancias type Integer - required
        self.NumTotalMercancias = None