"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    valores_por_clave = {}
    ruta_archivo = 'files/input/data.csv'

    with open(ruta_archivo, 'r') as f:
        for linea in f:
            if linea.strip():
                columnas = linea.split('\t')
                diccionario_str = columnas[4]
                pares = diccionario_str.split(',')
                for par in pares:
                    clave, valor_str = par.split(':')
                    valor = int(valor_str)
                    if clave in valores_por_clave:
                        minimo, maximo = valores_por_clave[clave]
                        valores_por_clave[clave] = (min(minimo, valor), max(maximo, valor))
                    else:
                        valores_por_clave[clave] = (valor, valor)

    resultado = [(clave, minimo, maximo) for clave, (minimo, maximo) in sorted(valores_por_clave.items())]
    return resultado
