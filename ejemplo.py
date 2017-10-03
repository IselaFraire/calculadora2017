# -*- coding: utf-8 -*-
from num2words import num2words

class Fecha():

def fecha(self,fecha):

    Mes={'01':"Enero",'02':"Febrero",'03':"Marzo",'04':"Abril",'05':"Mayo",'06':"Junio",'07':"Julio",'08':"Agosto",'09':"Septiembre",'10':"Octubre", '11':"Noviembre",'12':"Diciembre"}

    Dia={'01':"Uno",'02':"Dos",'03':"Tres",'04':"Cuatro",'05':"Cinco",'06':"Seis",'07':"Siete",'08':"Ocho",
'09':"Nueve",'10':"Diez",'11':"Once",'12':"Doce",'13':"Trece",'14':"Catorce",'15':"Quince",'16':"Dieciseis",
'17':"Diecisiete",'18':"Dieciocho",'19':"Diecinueve", '20':"Veinte",'21':"Veintiuno",'22':"Veintidos",
'23':"Veintitres",'24':"Veinticuatro", '25':"Veinticinco", '26':"Veintiseis", '27': "Veintisiete", '28' :"Veintiocho",'29':"Veintinueve",'30':"Treinta",'31':"Treinta y uno"}

    fecha_texto = fecha.split("/")
    dia =  fecha_texto[0]
    mes =  fecha_texto[1]
    anio = int(fecha_texto[2])

    dia_letra = (Dia[dia])
    mes_letra = (Mes[mes])
    anio_letra = num2words(anio, lang='es')

    return dia_letra + " de " +  mes_letra + " del " + anio_letra

