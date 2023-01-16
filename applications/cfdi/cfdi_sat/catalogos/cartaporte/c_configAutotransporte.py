

from enum import Enum, unique

@unique
class CConfigAutotransporte(Enum):


    C2 = 'C2'
    C3 = 'C3'
    C2R2 = 'C2R2'
    C3R2 = 'C3R2'
    C2R3 = 'C2R3'
    C3R3 = 'C3R3'
    T2S1 = 'T2S1'
    T2S2 = 'T2S2'
    T2S3 = 'T2S3'
    T3S1 = 'T3S1'
    T3S2 = 'T3S2'
    T3S3 = 'T3S3'
    T2S1R2 = 'T2S1R2'
    T2S2R2 = 'T2S2R2'
    T2S1R3 = 'T2S1R3'
    T3S1R2 = 'T3S1R2'
    T3S1R3 = 'T3S1R3'
    T3S2R2 = 'T3S2R2'
    T3S2R3 = 'T3S2R3'
    T3S2R4 = 'T3S2R4'
    T2S2S2 = 'T2S2S2'
    T3S2S2 = 'T3S2S2'
    T3S3S2 = 'T3S3S2'
    OTROEV = 'OTROEV'
    OTROEGP = 'OTROEGP'
    OTROSG = 'OTROSG'
    VL = "VL"
    OTROEVGP = "OTROEVGP"
    GPLUTA = "GPLUTA"
    GPLUTB = "GPLUTB"
    GPLUTC = "GPLUTC"
    GPLUTD = "GPLUTD"
    GPLATA = "GPLATA"
    GPLATB = "GPLATB"
    GPLATC = "GPLATC"
    GPLATD = "GPLATD"

    def getNameSpace():
        namespace = "http://www.sat.gob.mx/sitio_internet/cfd/catalogos/CartaPorte"
        return namespace

    def getName():
        name = "c_CodigoTransporteAereo"
        return name