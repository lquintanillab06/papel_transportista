from enum import Enum, unique

@unique
class CTipoDeComprobante(Enum):
    I = 'I'
    E = 'E'
    T = 'T'
    N = 'N'
    P = 'P'

    def getNameSpace():
        namespace = "http://www.sat.gob.mx/sitio_internet/cfd/catalogos"
        return namespace

    def getName():
        name = "c_TipoDeComprobante"
        return name