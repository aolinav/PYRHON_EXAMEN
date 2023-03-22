

#############################################################################################
#############################################################################################
""""
Función que recibe un csv y dvuelve un diccionario
"""""
dic = {}

#############################################################################################
""""
Función que recibe un diccionario y devulve dos disccionarios
"""""

def split(dic):
    dic2 = {}
    dic3 = {}

    for key in dic:
        if dic[key]["type"] == "white":
            dic2 = dic[key]

    for key2 in dic:
        if dic[key2]["type"] == "red":
            dic3 = dic[key2]
    return dic2, dic3

#############################################################################################

#############################################################################################
""""
Función que recibe un diccionario y un string (atributo) y devulve una lista con los valores del atributo
"""""
def reduce(dic, string):
    lista=[]
    for key in dic:
        if dic[key][string] == True:
            print(dic[key][string])
            print("hola")

#############################################################################################

dic={
1 : {'id': 1,
        'success': True,
        'name': 'Lary'
    },
    2 : {'id': 2,
        'success': False,
        'name': 'Rabi'
    },
    3 : {'id': 3,
        'success': False,
        'name': 'Alex'
    }
}
string = "success"

reduce(dic, string)