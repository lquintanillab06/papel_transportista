
from zeep import Client

class SolucionFactibleService():

    client = Client('https://testing.solucionfactible.com/ws/services/Timbrado?wsdl')

    def getCfdiTest(self, xml):
        
       
        isZipFile = 0
        xmlBytes = str.encode(xml)
        result = self.client.service.timbrar('testing@solucionfactible.com', 'timbrado.SF.16672', xmlBytes, isZipFile)
        if result.status == 200:#si la autenticación fue correcta y el servicio está disponible para el usuario
            resultadoTimbrado = result.resultados[0]
            #print(resultadoTimbrado.status)
            #print(resultadoTimbrado.mensaje)
                
            if resultadoTimbrado.status==200:#si el timbrado del comprobante fue exitoso
                    #(resultadoTimbrado.uuid)
                    #print(resultadoTimbrado.cfdiTimbrado)
                    xmlTimbrado = resultadoTimbrado.cfdiTimbrado.decode("utf-8")
                    return xmlTimbrado
                    ''' with open(f"xml/FAC-5000-SIGN.xml", mode='w', encoding='utf-8') as f:
                        f.write(resultadoTimbrado.cfdiTimbrado.decode("utf-8"))
                        f.close() '''
            
        else:#ocurrió un error con la autenticación o la disponibilidad del servicio para el usuario
            pass
            #print(result.mensaje) 