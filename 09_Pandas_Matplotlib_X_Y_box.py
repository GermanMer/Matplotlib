#CREA UN GRÁFICO DE CAJA CON UNA COLUMNA COMO EJE X Y OTRA COMO EJE Y

import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos y preparar el DataFrame
df = pd.read_csv(r'D:\Germán\Desktop\Python Files\automobile.csv')
df = df.dropna(axis=0)

# Gráfico de caja
df.plot(x='horsepower', y='price', kind='box')
plt.show()
