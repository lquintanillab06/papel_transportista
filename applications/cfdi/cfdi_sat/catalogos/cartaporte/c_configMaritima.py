



from enum import Enum, unique

@unique
class CConfigMaritimia(Enum):

    C_2 = 'C2'
    C_3 = 'C3'
    C_2_R_2 = 'C2R2'
    C_3_R_2 = 'C3R2'
    C_2_R_3 = 'C2R3'
    C_3_R_3 = 'C3R3'
    T_2_S_1 = 'T2S1'
    T_2_S_2 = 'T2S2'
    T_2_S_3 = 'T2S3'
    T_3_S_1 = 'T3S1'
    T_3_S_2 = 'T3S2'
    T_3_S_3 = 'T3S3'
    T_2_S_1_R_2 = 'T2S1R2'
    T_2_S_2_R_2 = 'T2S2R2'
    T_2_S_1_R_3 = 'T2S1R3'
    T_3_S_1_R_2 = 'T3S1R2'
    T_3_S_1_R_3 = 'T3S1R3'
    T_3_S_2_R_2 = 'T3S2R2'
    T_3_S_2_R_3 = 'T3S2R3'
    T_3_S_2_R_4 = 'T3S2R4'
    T_2_S_2_S_2 = 'T2S2S2'
    T_3_S_2_S_2 = 'T3S2S2'
    T_3_S_3_S_2 = 'T3S3S2'
    OTROEV = 'OTROEV'
    OTROEGP = 'OTROEGP'
    OTROSG = 'OTROSG'

    def getNameSpace():
        namespace = "http://www.sat.gob.mx/sitio_internet/cfd/catalogos/CartaPorte"
        return namespace

    def getName():
        name = "c_ConfigMaritima"
        return name