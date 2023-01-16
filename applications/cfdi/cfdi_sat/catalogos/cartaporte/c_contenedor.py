from enum import Enum, unique

@unique
class CContenedor(Enum):

    TC_01 = 'TC01'
    TC_02 = 'TC02'
    TC_03 = 'TC03'
    TC_04 = 'TC04'
    TC_05 = 'TC05'

    def getNameSpace():
        namespace = "http://www.sat.gob.mx/sitio_internet/cfd/catalogos/CartaPorte"
        return namespace

    def getName():
        name = "c_Contenedor"
        return name