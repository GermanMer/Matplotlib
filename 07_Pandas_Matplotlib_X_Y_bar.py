#CREA UN GRÁFICO DE BARRAS CON UNA COLUMNA COMO EJE X Y OTRA COMO EJE Y

import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos y preparar el DataFrame
df = pd.read_csv(r'D:\Germán\Desktop\Python Files\automobile.csv')
df = df.dropna(axis=0)

# Gráfico de barras
df.plot(x='horsepower', y='price', kind='bar')
plt.xticks(rotation=45)  # Rotar los valores en el eje x para una mejor legibilidad
plt.tight_layout()  # Ajustar el diseño para evitar recortes en las etiquetas
plt.show()
