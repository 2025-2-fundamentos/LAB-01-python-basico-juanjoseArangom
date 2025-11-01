"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    valores_por_letra = {}
    ruta_archivo = 'files/input/data.csv'

    with open(ruta_archivo, 'r') as f:
        for linea in f:
            if linea.strip():
                columnas = linea.split('\t')
                letra = columnas[0]
                valor = int(columnas[1])
                if letra in valores_por_letra:
                    maximo, minimo = valores_por_letra[letra]
                    valores_por_letra[letra] = (max(maximo, valor), min(minimo, valor))
                else:
                    valores_por_letra[letra] = (valor, valor)

    resultado = [(letra, maximo, minimo) for letra, (maximo, minimo) in sorted(valores_por_letra.items())]
    return resultado
