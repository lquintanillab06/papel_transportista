import math
from decimal import Decimal #, getcontext

class ImporteALetra():



    def __init__(self):
        self.__flag = 1
        self.__numero = 0
        self.__importe_parcial = 0
        self.__num = 0
        self.__num_letra = 0
        self.__num_letras = 0
        self.__num_letram = 0
        self.__num_letradm = 0
        self.__num_letracm = 0
        self.__num_letramm = 0
        self.__num_letradmm = 0

        self.flag = self.__flag
    
   
    def __unidad(self, numero):
        amount = math.floor(numero)

        if(amount == 9):
            self.__num = "NUEVE"
            return self.__num
        if(amount == 8):
            self.__num = "OCHO"
            return self.__num
        if(amount == 7):
            self.__num = "SIETE"
            return self.__num
        if(amount == 6):
            self.__num = "SEIS"
            return self.__num
        if(amount == 5):
            self.__num = "CINCO"
            return self.__num
        if(amount == 4):
            self.__num = "CUATRO"
            return self.__num
        if(amount == 3):
            self.__num = "TRES"
            return self.__num
        if(amount == 2):
            self.__num = "DOS"
            return self.__num
        if(amount == 1 and self.__flag == 0):
            self.__num = "UNO"
            return self.__num
        if(amount == 1 and self.__flag == 1):
            self.__num = "UN"
            return self.__num
        if(amount == 0):
            self.__num = ""
            return self.__num 
    
   
    def __decena(self, numero):
        
        if (numero >= 90 and numero < 100):
            self.__num_letra = "NOVENTA "
            if (numero > 90):
                self.__num_letra = f"{self.__num_letra} Y {self.__unidad(numero - 90)}" 
                return self.__num_letra
            return self.__num_letra
      
        if (numero >= 80 and numero < 90):
            self.__num_letra = "OCHENTA "
            if (numero > 80):
                self.__num_letra = f"{self.__num_letra} Y {self.__unidad(numero - 80)}" 
                return self.__num_letra
            return self.__num_letra
        
        if (numero >= 70 and numero < 80):
            self.__num_letra = "SETENTA "
            if (numero > 70):
                self.__num_letra = f"{self.__num_letra} Y {self.__unidad(numero - 70)}" 
                return self.__num_letra
            return self.__num_letra

        if (numero >= 60 and numero < 70):
            self.__num_letra = "SESENTA "
            if (numero > 60):
                self.__num_letra = f"{self.__num_letra} Y {self.__unidad(numero - 60)}" 
                return self.__num_letra
            return self.__num_letra
        
        if (numero >= 50 and numero < 60):
            self.__num_letra = "CINCUENTA "
            if (numero > 50):
                self.__num_letra = f"{self.__num_letra} Y {self.__unidad(numero - 50)}" 
                return self.__num_letra
            return self.__num_letra

        if (numero >= 40 and numero < 50):
            self.__num_letra = "CUARENTA "
            if (numero > 40):
                self.__num_letra = f"{self.__num_letra} Y {self.__unidad(numero - 40)}" 
                return self.__num_letra
            return self.__num_letra

        if (numero >= 30 and numero < 40):
            self.__num_letra = "TREINTA "
            if (numero > 30):
                self.__num_letra = f"{self.__num_letra} Y {self.__unidad(numero - 30)}" 
                return self.__num_letra
            return self.__num_letra
            
        if (numero >= 20 and numero < 30):
            if (numero == 20):
                self.__num_letra = "VEINTE "
            else:
                self.__num_letra = f"VEINTI{self.__unidad(numero - 20)}" 
                return self.__num_letra
            return self.__num_letra
       
        if (numero >= 10  and numero <20):
            amount = math.floor(numero)
            if (amount == 10):
                self.__num_letra = "DIEZ "
            if (amount == 11):
                self.__num_letra = "ONCE "
            if (amount == 12):
                self.__num_letra = "DOCE "
            if (amount == 13):
                self.__num_letra = "TRECE "
            if (amount == 14):
                self.__num_letra = "CATORCE "
            if (amount == 15):
                self.__num_letra = "QUINCE "
            if (amount == 16):
                self.__num_letra = "DIECISEIS "
            if (amount == 17):
                self.__num_letra = "DIECISIETE "
            if (amount == 18):
                self.__num_letra = "DIECIOCHO "
            if (amount == 19):
                self.__num_letra = "DIECINUEVE "

            return self.__num_letra

        if (numero < 10):
            self.__num_letra = self.__unidad(numero)
        return self.__num_letra
        
   
    def __centena(self, numero):
        
        if (numero >= 100):
           
            if(numero >=900 and numero <1000) :
                self.__num_letras = "NOVECIENTOS "
                if (numero > 900):
                    self.__num_letras =f"{self.__num_letras} {self.__decena(numero - 900)} "
                return self.__num_letras

            if(numero >=800 and numero <900) :
                self.__num_letras = "OCHOCIENTOS "
                if (numero > 800):
                    self.__num_letras =f"{self.__num_letras} {self.__decena(numero - 800)} "
                return self.__num_letras
            
            if(numero >=700 and numero <800) :
                self.__num_letras = "SETECIENTOS "
                if (numero > 700):
                    self.__num_letras =f"{self.__num_letras} {self.__decena(numero - 700)} "
                return self.__num_letras
            
            if(numero >=600 and numero <700) :
                self.__num_letras = "SEISCIENTOS "
                if (numero > 600):
                    self.__num_letras =f"{self.__num_letras} {self.__decena(numero - 600)} "
                return self.__num_letras
            
            if(numero >=500 and numero <600) :
                self.__num_letras = "QUINIENTOS "
                if (numero > 500):      
                    self.__num_letras =f"{self.__num_letras} {self.__decena(numero - 500)} "
                return self.__num_letras

            if(numero >=400 and numero <500) :
                self.__num_letras = "CUATROCIENTOS "
                if (numero > 400):
                    self.__num_letras =f"{self.__num_letras} {self.__decena(numero - 400)} "
                return self.__num_letras
            
            if(numero >=300 and numero <400) :
                self.__num_letras = "TRESCIENTOS "
                if (numero > 300):
                    self.__num_letras =f"{self.__num_letras} {self.__decena(numero - 300)} "
                return self.__num_letras
            
            if(numero >=200 and numero <300) :
                self.__num_letras = "DOSCIENTOS "
                if (numero > 200):
                    self.__num_letras =f"{self.__num_letras} {self.__decena(numero - 200)} "
                return self.__num_letras

            if(numero >=100 and numero <200) :
                if (numero == 100):
                    self.__num_letras = "CIEN "
                if (numero > 100):
                    self.__num_letras =f"CIENTO {self.__decena(numero - 100)} "
                return self.__num_letras

        if (numero < 100):
            self.__num_letras =self.__decena(numero)
        
        return self.__num_letras
             
   
    def __miles(self, numero):
      
        if (numero >= 1000 and numero <2000):
            self.__num_letram = f"MIL {self.__centena(numero % 1000)}"
            return self.__num_letram

        if (numero >= 2000 and numero < 10000):
            self.__num_letram = f"{self.__unidad(numero/1000)} MIL {self.__centena(numero % 1000)}"
            return self.__num_letram

        if (numero < 1000):
            self.__num_letram = self.__centena(numero)
            return self.__num_letram

   
    def __decmiles(self, numero):
        if (numero == 10000):
            self.__num_letradm = "DIEZ MIL"
            return self.__num_letradm

        if (numero > 10000 and numero <20000):
            self.__num_letradm =  f"{self.__decena(numero/1000)} MIL {self.__centena(numero%1000)}"
            return self.__num_letradm

        if (numero >= 20000 and numero <100000):
            self.__num_letradm = f"{self.__decena(numero/1000)} MIL {self.__miles(numero%1000)}"
            return self.__num_letradm
        

        if (numero < 10000):
            self.__num_letradm = self.__miles(numero)
            return self.__num_letradm

   
    def __cienmiles(self, numero):

        if (numero == 100000):
            self.__num_letracm = "CIEN MIL"
            return self.__num_letracm

        if (numero >= 100000 and numero <1000000):
            self.__num_letracm = f"{self.__centena(numero/1000)} MIL {self.__centena(numero%1000)}" 
            return self.__num_letracm
        
        if (numero < 100000):
            self.__num_letracm = self.__decmiles(numero)
            return self.__num_letracm

   
    def __millon(self, numero):
        if (numero >= 1000000 and numero < 2000000):
            self.__num_letramm = f"UN MILLON {self.__cienmiles(numero%1000000)}" 
            return self.__num_letramm

        if (numero >= 2000000 and numero <10000000):
            self.__num_letramm =  f"{self.__unidad(numero/1000000)} MILLONES {self.__cienmiles(numero%1000000)}" 
            return self.__num_letramm

        if(numero < 1000000):
            self.__num_letramm = self.__cienmiles(numero)
            return self.__num_letramm

   
    def __decmillon(self, numero):
        if (numero == 10000000):
            self.__num_letradmm = "DIEZ MILLONES"
            return self.__num_letradmm

        if (numero > 10000000 and numero <20000000):
            self.__num_letradmm = f"{self.__decena(numero/1000000)} MILLONES {self.__cienmiles(numero%1000000)} "  
            return self.__num_letradmm

        if (numero >= 20000000 and numero <100000000):     
            self.__num_letradmm = f"{self.__decena(numero/1000000)} MILLONES {self.__millon(numero%1000000)} " 
            return self.__num_letradmm

        if (numero < 10000000):
            self.__num_letradmm = self.__millon(numero)
            return self.__num_letradmm
        

    
    def convertirALetras(self,numero):
        #getcontext().prec = 2
        numeroInt = round(numero,0)
        numeroDec =  (Decimal(numero) - Decimal(numeroInt)) *100
        num = self.__decmillon(numeroInt)
        if (numero % 1000000 == 0.00): 
             return f"{num}DE PESOS {numeroDec}/100 M.N"
        else:
            return f"{num}PESOS {numeroDec}/100 M.N"
           
            
    
    def convertirALetrasDolares(self,numero):
        #getcontext().prec = 2
        numeroInt = round(numero,0)
        numeroDec =  (Decimal(numero) - Decimal(numeroInt)) *100
        num = self.__decmillon(numeroInt)
        if (numero < 1000000): 
            return f"{num}DOLARES AMERICANOS {numeroDec}/100 USD"
        else:
            return f"{num}DE DOLARES AMERICANOS {numeroDec}/100 USD"




    
   
        
