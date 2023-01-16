from enum import Enum, unique

@unique
class CContenedorMaritimo(Enum):

    CM_001 = 'CM001'
    CM_002 = 'CM002'
    CM_003 = 'CM003'
    CM_004 = 'CM004'
    CM_005 = 'CM005'
    CM_006 = 'CM006'
    CM_007 = 'CM007'
    CM_008 = 'CM008'
    CM_009 = 'CM009'

    def getNameSpace():
        namespace = "http://www.sat.gob.mx/sitio_internet/cfd/catalogos/CartaPorte"
        return namespace

    def getName():
        name = "c_ContenedorMaritimo"
        return name