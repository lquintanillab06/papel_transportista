
from enum import Enum, unique

@unique
class CClaveTipoCarga(Enum):

    CGS = 'CGS'
    CGC = 'CGC'
    GMN = 'GMN'
    GAG = 'GAG'
    OFL = 'OFL'
    PYD = 'PYD'

    def getNameSpace():
        namespace = "http://www.sat.gob.mx/sitio_internet/cfd/catalogos/CartaPorte"
        return namespace

    def getName():
        name = "c_ClaveTipoCarga"
        return name