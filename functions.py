#############################################################################################
import math
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
        for j in range(len(lista1)):
            if j != i or i != j:
                potencia = math.pow(abs(i - j),2)
                a = math.sqrt(potencia)

    for i in range(len(lista2)):
        for j in range(len(lista2)):
            if j != i or i != j:
                potencia = math.pow(abs(i - j),2)
                b = math.sqrt(potencia)
    return a,b
#############################################################################################

#############################################################################################
#Función que recibe la lista calculada en la función media y devuelve una lista con el resultado

#def silhouette(lista1, lista2):

#############################################################################################
