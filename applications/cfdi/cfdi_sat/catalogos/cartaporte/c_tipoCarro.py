from enum import Enum, unique

@unique
class CTipoCarro(Enum):

    TC_01 = 'TC01'
    TC_02 = 'TC02'
    TC_03 = 'TC03'
    TC_04 = 'TC04'
    TC_05 = 'TC05'
    TC_06 = 'TC06'
    TC_07 = 'TC07'
    TC_08 = 'TC08'
    TC_09 = 'TC09'
    TC_10 = 'TC10'
    TC_11 = 'TC11'

    def getNameSpace():
        namespace = "http://www.sat.gob.mx/sitio_internet/cfd/catalogos/CartaPorte"
        return namespace

    def getName():
        name = "c_TipoCarro"
        return name