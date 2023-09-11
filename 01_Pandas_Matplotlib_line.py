#CREA UN GRÁFICO DE LINEAS CON TODAS LAS COLUMNAS NUMÉRICAS DE UN DATA FRAME

import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos y preparar el DataFrame
df = pd.read_csv(r'D:\Germán\Desktop\Python Files\automobile.csv')
df = df.dropna(axis=0)

# Genera un gráfico de líneas con todas las columnas del data frame
df.plot(kind='line')
plt.show()
