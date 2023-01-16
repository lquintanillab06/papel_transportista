from enum import Enum, unique

@unique
class CSubTipoRem(Enum):

    CTR_001 = 'CTR001'
    CTR_002 = 'CTR002'
    CTR_003 = 'CTR003'
    CTR_004 = 'CTR004'
    CTR_005 = 'CTR005'
    CTR_006 = 'CTR006'
    CTR_007 = 'CTR007'
    CTR_008 = 'CTR008'
    CTR_009 = 'CTR009'
    CTR_010 = 'CTR010'
    CTR_011 = 'CTR011'
    CTR_012 = 'CTR012'
    CTR_013 = 'CTR013'
    CTR_014 = 'CTR014'
    CTR_015 = 'CTR015'
    CTR_016 = 'CTR016'
    CTR_017 = 'CTR017'
    CTR_018 = 'CTR018'
    CTR_019 = 'CTR019'
    CTR_020 = 'CTR020'
    CTR_021 = 'CTR021'
    CTR_022 = 'CTR022'
    CTR_023 = 'CTR023'
    CTR_024 = 'CTR024'
    CTR_025 = 'CTR025'
    CTR_026 = 'CTR026'
    CTR_027 = 'CTR027'
    CTR_028 = 'CTR028'
    CTR_029 = 'CTR029'
    CTR_030 = 'CTR030'
    CTR_031 = 'CTR031'
    CTR_032 = 'CTR032'

    def getNameSpace():
        namespace = "http://www.sat.gob.mx/sitio_internet/cfd/catalogos/CartaPorte"
        return namespace

    def getName():
        name = "c_SubTipoRem"
        return name