from enum import Enum, unique

@unique
class CTipoFactor(Enum):
    TASA = 'Tasa'
    CUOTA = 'Cuota'
    EXENTO = 'Excento'

    def getNameSpace():
        namespace = "http://www.sat.gob.mx/sitio_internet/cfd/catalogos"
        return namespace

    def getName():
        name = "c_TipoFactor"
        return name