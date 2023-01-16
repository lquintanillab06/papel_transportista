from datetime import datetime,date

class DateUtils():

    CFDI_DATE_FORMAT= "%Y-%m-%dT%H:%M:%S"

    meses ={
        'January':{'nombre': 'Enero', 'clave': 0},
        'February':{'nombre': 'Febrero', 'clave': 1},
        'March':{'nombre': 'Marzo', 'clave': 3},
        'April':{'nombre': 'Abril', 'clave': 4},
    }

    @classmethod
    def getNowFormatted(cls):
        now = datetime.now()
        return now.strftime(cls.CFDI_DATE_FORMAT)
    
    @classmethod
    def cfdiDate(cls,fecha):
        return fecha.strftime(cls.CFDI_DATE_FORMAT)

    @staticmethod 
    def cfdiDateToDate(cfdiDate):
        return datetime.fromisoformat(cfdiDate)

    @classmethod
    def toDate(cls, fecha):
        return date.fromisoformat(fecha)
       
    @classmethod
    def periodoDays(cls,fechaInicial, fechaFinal):
        d1 = datetime.strptime(str(fechaInicial), "%Y-%m-%d")
        d2 = datetime.strptime(str(fechaFinal), "%Y-%m-%d")
        return abs((d2 - d1).days)

    @classmethod
    def getMonth(cls,fecha):
        return f"{cls.meses[fecha.strftime('%B')]['nombre']}"

    @classmethod
    def getCurrentMonth(cls):
        #print("Current mes")
        return f"{cls.meses[date.today().strftime('%B')]['nombre']}"
       
    @classmethod
    def getCurrentMonthYear(cls):
        return f"{cls.meses[date.today().strftime('%B')]['nombre']} - {date.today().strftime('%Y')}"

    @classmethod
    def periodoMonthLabel(cls,fechaInicial, fechaFinal):   
        
	    return f"{cls.meses[fechaInicial.strftime('%B')]['nombre']} - {cls.meses[fechaFinal.strftime('%B')]['nombre']}"

    


