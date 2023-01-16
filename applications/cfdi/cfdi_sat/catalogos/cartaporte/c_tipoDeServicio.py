from enum import Enum, unique

@unique
class CTipoDeServicio(Enum):

    TS_01 = 'TS01'
    TS_02 = 'TS02'
    TS_03 = 'TS03'
    TS_04 = 'TS04'

    def getNameSpace():
        namespace = "http://www.sat.gob.mx/sitio_internet/cfd/catalogos/CartaPorte"
        return namespace

    def getName():
        name = "c_TipoDeServicio"
        return name