"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    resultado = []
    ruta_archivo = 'files/input/data.csv'

    with open(ruta_archivo, 'r') as f:
        for linea in f:
            if linea.strip():
                columnas = linea.split('\t')
                letra = columnas[0]
                col4 = columnas[3].strip()
                col5 = columnas[4].strip()

                # Contar elementos en columna 4
                if col4:
                    elementos_col4 = col4.split(',')
                    cantidad_col4 = len(elementos_col4)
                else:
                    cantidad_col4 = 0

                # Contar elementos en columna 5
                if col5:
                    elementos_col5 = col5.split(',')
                    cantidad_col5 = len(elementos_col5)
                else:
                    cantidad_col5 = 0

                resultado.append((letra, cantidad_col4, cantidad_col5))

    return resultado
