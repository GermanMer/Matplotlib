import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos y preparar el DataFrame
df = pd.read_csv(r'D:\Germán\Desktop\Python Files\automobile.csv')
df = df.dropna(axis=0)

# Genera el gráfico
data = df['price']
bins = [5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000] #Acá se ponen los valores para los límites de los bins
plt.hist(data, bins=bins, edgecolor='black')
plt.xlabel('Precio')
plt.ylabel('Frecuencia')
plt.title('Histograma')
plt.show()
