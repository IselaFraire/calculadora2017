class Cadena():

    def cadena(self,texto):

        dic={}
        
        for linea in texto.split():
	    if linea not in dic:
		dic[linea]=1
            else:
	        dic[linea] = dic[linea] +1
        return dic
