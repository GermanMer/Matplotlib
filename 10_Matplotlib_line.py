import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos y preparar el DataFrame
df = pd.read_csv(r'D:\Germán\Desktop\Python Files\automobile.csv')
df = df.dropna(axis=0)

# Genera el gráfico
x = df['horsepower']
y = df['price']
plt.plot(x, y)
plt.xlabel('Potencia')
plt.ylabel('Precio')
plt.title('Gráfico de Línea')
plt.show()
