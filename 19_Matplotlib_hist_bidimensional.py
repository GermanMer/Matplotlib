import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos y preparar el DataFrame
df = pd.read_csv(r'D:\Germán\Desktop\Python Files\automobile.csv')
df = df.dropna(axis=0)

# Genera el gráfico
x = df['horsepower']
y = df['price']

x_bins = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260]
y_bins = [5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000]

plt.hist2d(x, y, bins=[x_bins, y_bins], cmap='Blues')
plt.xlabel('Potencia')
plt.ylabel('Precio')
plt.title('Histograma Bidimensional')
plt.colorbar(label='Frecuencia')
plt.show()
