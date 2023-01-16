

class Receptor():

    """Nodo requerido para precisar la información del contribuyente receptor
    del comprobante.Atributo requerido para precisar la Clave del Registro
    Federal de Contribuyentes correspondiente al contribuyente receptor del
    comprobante.Atributo opcional para precisar el nombre, denominación o
    razón social del contribuyente receptor del comprobante.Atributo
    condicional para registrar la clave del país de residencia para efectos
    fiscales del receptor del comprobante, cuando se trate de un
    extranjero, y que es conforme con la especificación ISO 3166-1 alpha-3.
    Es requerido cuando se incluya el complemento de comercio exterior o se
    registre el atributo NumRegIdTrib.Atributo condicional para expresar el
    número de registro de identidad fiscal del receptor cuando sea
    residente en el extranjero. Es requerido cuando se incluya el
    complemento de comercio exterior.Atributo requerido para expresar la
    clave del uso que dará a esta factura el receptor del CFDI."""

    def __init__(self):

        # Rfc type String - required
        self.Rfc = None

        # Nombre type String - required
        self.Nombre = None

        # DomicilioFiscalReceptor type String - required
        self.DomicilioFiscalReceptor = None

        # ResidenciaFiscal type CPais
        self.ResidenciaFiscal = None

        # NumRegIdTrib type String
        self.NumRegIdTrib = None

        # RegimenFiscalReceptor type String - required
        self.RegimenFiscalReceptor = None

        # UsoDeCfdi type CUsoDeCfdi - required
        self.UsoDeCfdi = None

