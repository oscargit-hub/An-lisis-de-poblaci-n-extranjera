# Importamos todas las herramientas que previamente hemos instalado con el comando pip
from pathlib import Path

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

raiz = Path(__file__).parent.parent

archivo = raiz / "datos" / "población_extranjera_españa.xlsx"

df = pd.read_excel(archivo, header=None)

# Matriz para coger los datos del excel con filas y las columnas que nos interesan utilizando el numpy, en este caso la fila 7 y 9 y las columnas de la 1 a la 26
# luego lo cortamos para que nos de el entero, si no nos daria formato float con decimales, el .0 al no tener y que nos de los datos limpios
matriz = np.array([
    df.iloc[7, 1:26],
    df.iloc[9, 1:26]
], dtype=int)

# Print para comprobar que ha cogido bien los datos del excel
print(matriz)

print ("\nDimensiones:", matriz.shape)

# Cogemos las dos partes de la matriz y las separamos en 2 arrays para poder hacer la grafica
anios = matriz[0]
poblacion = matriz[1]

# Creamos la gráfica con los datos recogidos y ponemos como queremos la gráfica, tamaño, cantidad de datos, etc
plt.figure(figsize=(15, 5))
plt.plot(anios, poblacion, marker="o", linestyle="-", label="Población extranjera")
plt.xticks(anios, rotation=45)
plt.title("Evolución de la población extranjera en España")
plt.xlabel("Año")
plt.ylabel("Población")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()