"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    suma_columna_5 = {}
    ruta_archivo = 'files/input/data.csv'

    with open(ruta_archivo, 'r') as f:
        for linea in f:
            if linea.strip():
                columnas = linea.split('\t')
                letra = columnas[0]
                valores_columna_5 = columnas[4].split(',')
                suma_valores = sum(int(valor.split(':')[1]) for valor in valores_columna_5)
                if letra in suma_columna_5:
                    suma_columna_5[letra] += suma_valores
                else:
                    suma_columna_5[letra] = suma_valores

    return suma_columna_5
