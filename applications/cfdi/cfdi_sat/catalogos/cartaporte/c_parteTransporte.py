


from enum import Enum, unique

@unique
class CParteTransporte(Enum):

    PT_01 = "PT01"
    PT_02 = "PT02"
    PT_03 = "PT03"
    PT_04 = "PT04"
    PT_05 = "PT05"
    PT_06 = "PT06"
    PT_07 = "PT07"
    PT_08 = "PT08"
    PT_09 = "PT09"
    PT_10 = "PT10"
    PT_11 = "PT11"
    PT_12 = "PT12"

    def getNameSpace():
        namespace = "http://www.sat.gob.mx/sitio_internet/cfd/catalogos/CartaPorte"
        return namespace

    def getName():
        name = "c_ParteTransporte"
        return name