from enum import Enum, unique

@unique
class CUsoCFDI(Enum):
    G_01 = "G01"
    G_02 = "G02"
    G_03 = "G03"
    I_01 = "I01"
    I_02 = "I02"
    I_03 = "I03"
    I_04 = "I04"
    I_05 = "I05"
    I_06 = "I06"
    I_07 = "I07"
    I_08 = "I08"
    D_01 = "D01"
    D_02 = "D02"
    D_03 = "D03"
    D_04 = "D04"
    D_05 = "D05"
    D_06 = "D06"
    D_07 = "D07"
    D_08 = "D08"
    D_09 = "D09"
    D_10 = "D10"
    P_01 = "P01"
    S_01 = "S01"
    CP_01 = "CP01"
    CN_01 = "CN01"

    def getNameSpace():
        namespace = "http://www.sat.gob.mx/sitio_internet/cfd/catalogos"
        return namespace

    def getName():
        name = "c_UsoCFDI"
        return name