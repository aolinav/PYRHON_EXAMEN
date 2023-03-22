
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

#############################################################################################
dic2, dic3 = split(dic)
print(dic2)
print(dic3)

lista = reduce(dic2, string)
print(lista)

lista2 = reduce(dic3, string)
print(lista2)