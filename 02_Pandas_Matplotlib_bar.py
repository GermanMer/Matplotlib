#CREA UN GRÁFICO DE BARRAS CON TODAS LAS COLUMNAS NUMÉRICAS DE UN DATA FRAME

import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos y preparar el DataFrame
df = pd.read_csv(r'D:\Germán\Desktop\Python Files\automobile.csv')
df = df.dropna(axis=0)

# Genera un gráfico de barras con todas las columnas del data frame
df.plot(kind='bar')
plt.xticks(rotation=45)  # Rotar los valores en el eje x para una mejor legibilidad
plt.tight_layout()  # Ajustar el diseño para evitar recortes en las etiquetas
plt.show()
