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
            dic2[key].pop("type")
    for key2 in dic:
        if dic[key2]["type"] == "red":
            dic3[key] = dic[key2]
            dic3[key].pop("type")

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
    }
}
string = "alcohol"

#############################################################################################
dic2, dic3 = split(dic)
print(dic3)

lista = reduce(dic2, string)
#print(lista)