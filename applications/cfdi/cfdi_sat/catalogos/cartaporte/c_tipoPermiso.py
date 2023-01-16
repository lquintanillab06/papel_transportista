from enum import Enum, unique

@unique
class CTipoPermiso(Enum):

    TPAF_01 = 'TPAF01'
    TPAF_02 = 'TPAF02'
    TPAF_03 = 'TPAF03'
    TPAF_04 = 'TPAF04'
    TPAF_05 = 'TPAF05'
    TPAF_06 = 'TPAF06'
    TPAF_07 = 'TPAF07'
    TPAF_08 = 'TPAF08'
    TPAF_09 = 'TPAF09'
    TPAF_10 = 'TPAF10'
    TPAF_11 = 'TPAF11'
    TPAF_12 = 'TPAF12'
    TPAF_13 = 'TPAF13'
    TPAF_14 = 'TPAF14'
    TPAF_15 = 'TPAF15'
    TPAF_16 = 'TPAF16'
    TPAF_17 = 'TPAF17'
    TPAF_18 = 'TPAF18'
    TPAF_19 = 'TPAF19'
    TPAF_20 = 'TPAF20'
    TPTM_01 = 'TPTM01'
    TPTA_01 = 'TPTA01'
    TPTA_02 = 'TPTA02'
    TPTA_03 = 'TPTA03'
    TPTA_04 = 'TPTA04'
    TPXX00 = 'TPXX00'
    

    def getNameSpace():
        namespace = "http://www.sat.gob.mx/sitio_internet/cfd/catalogos/CartaPorte"
        return namespace

    def getName():
        name = "c_TipoPermiso"
        return name