from random import randrange, uniform
import random

names = ['AGUILAR PARRA STEVEN',
        'ALZATE ADRIAN CAMILO',
        'ARENAS MUNERA DANIEL',
        'BARAJAS SANCHEZ SANTIAGO',
        'BEDOYA SEPULVEDA JUAN CAMILO',
        'BUSTAMANTE CARO CRISTIAN ANDRES',
        'COLORADO ALVAREZ JUAN DAVID',
        'CORREA HERNÁNDEZ LUIS MIGUEL',
        'GARCÍA FLÓREZ ITALIA ANDREA',
        'HENAO MEJIA DAVID',
        'KARUT DE LA ROSA FAUZY',
        'LOPEZ PULGARIN DAVID ALEJANDRO',
        'MOLANO VARGAS JUAN ESTEBAN',
        'MONCAYO PARRA JAIME ANDRES',
        'MUÑOZ ZAPATA YERALDIN',
        'ORTIZ SANTANA PAULA ALEJANDRA',
        'OSPINA ARANGO SEBASTIÁN',
        'PEREZ DOMINGUEZ CAMILO ANDRES',
        'PULGARÍN LOAIZA ANDRÉS FELIPE',
        'RENDÓN CHAVERRA DIDIER ALEXANDER',
        'RIVERA AGUILAR MANUEL DAVID',
        'RIVERA NARANJO SEBASTIAN',
        'SANCHEZ ARBOLEDA JOSE DANIEL',
        'TAMAYO MONTOYA YOJAN',
        'VALENCIA TABARES CAMILO',
        'ZULUAGA OSORIO ANDRES FELIPE',
        ]

practica = ["Prueba 1",
            "Prueba 2",
            "Prueba 3",
            "Prueba 4",
            "Prueba 5",
            "Prueba 6",
            "Prueba 7",
            "Prueba 8",
            "Prueba 9",
            "Prueba 10",
            "Prueba 11",
            "Prueba 12",
            "Prueba 13",
            "Prueba 14",
            "Prueba 15",
            "Prueba 16",
            "Prueba 17",
            "Prueba 18",
            "Prueba 19",
            "Prueba 20",
            "Prueba 21",
            "Prueba 22",
            "Prueba 23",
            "Prueba 24",
            "Prueba 25",
            "Prueba 26"]

used = []
val = random.sample(practica, 26)

for i in range(0, 26):
    print(names[i] + " = " + val[i])
