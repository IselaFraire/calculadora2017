class Edad():

    def edad(self, num1):

        if num1 <= 0:
	    return 'No existes'
	elif num1 <= 13:
	    return 'Eres nino'
	elif num1<= 18:
	    return 'Eres adolescente'
	elif num1<= 65:
	    return 'Eres adulto'
	elif num1 <= 120:
	    return 'Eres adulto mayor'
        elif num1 >= 121:
	    return 'Eres Mumma-Ra'
	return ValueError

"""
    def __init__(self):
        self.resultado = 0

    def obtener_resutado(self):
	return self.resultado

    def edad(self, num):
        try:
            self.resultado = num
            if(resultado <= 0):
		return 'No existes'
	    elif(resultado <= 13):
		return 'Eres nino'
	    elif(resultado <= 18):
		return 'Eres adolescente'
	    elif(resultado <= 65):
		return 'Eres adulto'
	    elif(resultado <= 120):
		return 'Eres adulto mayor'
	    elif(resultado >= 121):
		return 'Eres Mumma-Ra'    
        except:
	    return 'Datos incorrectos'
"""
