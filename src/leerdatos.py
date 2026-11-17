from pathlib import Path

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

raiz = Path(__file__).parent.parent

archivo = raiz / "datos" / "población_extranjera_españa.xlsx"

df = pd.read_excel(archivo, header=None)

# Matriz para coger los datos del excel con filas y las columnas que nos interesan, en este caso la fila 7 y 9 y las columnas de la 1 a la 26
# luego lo cortamos para que nos de el entero, si no nos daria formato float con decimales, el .0 al no tener y que nos de los datos limpios
matriz = np.array([
    df.iloc[7, 1:26],
    df.iloc[9, 1:26]
], dtype=int)

print(matriz)

print ("\nDimensiones:", matriz.shape)


anios = matriz[0]
poblacion = matriz[1]


plt.figure(figsize=(10, 5))
plt.plot(anios, poblacion, marker="o", linestyle="-", label="Población extranjera")
plt.title("Evolución de la población extranjera en España")
plt.xlabel("Año")
plt.ylabel("Población")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()