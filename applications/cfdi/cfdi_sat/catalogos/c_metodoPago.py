from enum import Enum, unique

@unique
class CMetodoPago(Enum):
    PUE = "PUE"
    PIP = "PIP"
    PPD = "PPD"

    def getNameSpace():
        namespace = "http://www.sat.gob.mx/sitio_internet/cfd/catalogos"
        return namespace

    def getName():
        name = "c_Pais"
        return name