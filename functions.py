#############################################################################################
import csv
#############################################################################################

#############################################################################################
#Función que recibe un csv y dvuelve un diccionario

#def read_data(nomcsv):


#############################################################################################

#############################################################################################
#Función que recibe un diccionario y devulve dos disccionarios

def split(dic):
    dic2 = {}
    dic3 = {}

    for key in dic:
        if dic[key]["type"] == "white":
            dic2[key] = dic[key]

    for key2 in dic:
        if dic[key2]["type"] == "red":
            dic3[key2] = dic[key2]

    for key3 in dic2:
        dic2[key3].pop('type')

    for key4 in dic3:
        dic3[key4].pop('type')

    return dic2, dic3
#############################################################################################

#############################################################################################
#Función que recibe un diccionario y un string (atributo) y devulve una lista con los valores del atributo

def reduce(dic, string):
    lista=[]
    for key in dic:
        if dic[key][string]:
            lista.append(dic[key][string])
        else:
            raise ValueError("No existe el atributo en el diccionario")
    return lista
#############################################################################################

#############################################################################################
#Función auxiliar para carcula la media de las dos listas y pasarle la resultante a silhouette

def media(lista1, lista2):
    for i in range(len(lista1)):
        


#############################################################################################

#############################################################################################
#Función que recibe la lista calculada en la función media y devuelve una lista con el resultado

#def silhouette(lista1, lista2):




#############################################################################################
dic={
'dato1' : {'type': 'white',
        'alcohol': '8.8',
        'name': 'Lary'

    },
    'dato2' : {'type': 'white',
        'alcohol': '9',
        'name': 'Rabi'
    },
    'dato3' : {'type': 'red',
        'alcohol': '3.3',
        'name': 'Alex'
    },
    'dato4' : {'type': 'white',
        'alcohol': '4',
        'name': 'Rabi'
    },
    'dato5' : {'type': 'red',
        'alcohol': '7.3',
        'name': 'Alex'
    }
}
string = "alcohol"


dic2, dic3 = split(dic)
print(dic2)
print(dic3)

lista = reduce(dic2, string)
print(lista)

lista2 = reduce(dic3, string)
print(lista2)