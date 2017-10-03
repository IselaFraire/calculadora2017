def mesANumero(string):

    m = {
        'enero': "01",
        'febrero': "02",
        'marzo': "03",
        'abril': "04",
        'mayo': "05",
        'junio': "06",
        'julio': "07",
        'agosto': "08",
        'septiembre': "09",
        'octubre': "10",
        'noviembre': "11",
        'diciembre': "12"
        }

    fecha = string\\.split("-")
    dia =  fecha[0]
    mes =  fecha[1]
    anio = fecha[2]

    try:
        out = str(m[mes.lower()])
        print dia + "-" +  out + "-" + anio
    except:
        raise ValueError('No es un mes')
>>


"""d=int(input("ingresa dia\n"))"""
"""m=int(input("ingresa mes\n"))"""
"""a=int(input("ingresa año\n"))
sentence = (str(d)+" de "+str(Mes[m-1])+" del "+str(a))
print sentence
