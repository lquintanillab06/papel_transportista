from enum import Enum, unique

@unique
class CTipoDeTrafico(Enum):

    TT_01 = "TT01"
    TT_02 = "TT02"
    TT_03 = "TT03"
    TT_04 = "TT04"

    def getNameSpace():
        namespace = "http://www.sat.gob.mx/sitio_internet/cfd/catalogos/CartaPorte"
        return namespace

    def getName():
        name = "c_TipoDeTrafico"
        return name