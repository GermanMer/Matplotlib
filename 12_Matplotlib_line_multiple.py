import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos y preparar el DataFrame
df = pd.read_csv(r'D:\Germán\Desktop\Python Files\automobile.csv')
df = df.dropna(axis=0)

# Genera el gráfico
x = df['price']
y1 = df['horsepower']
y2 = df['engine-size']
y3 = df['curb-weight']

plt.plot(x, y1, label='Potencia', color='blue', linestyle='-', marker='o')
plt.plot(x, y2, label='Motor', color='green', linestyle='--', marker='s')
plt.plot(x, y3, label='Peso', color='red', linestyle=':', marker='^')

plt.xlabel('Precio')
plt.ylabel('Variables')
plt.title('Comparación de Múltiples Series de Datos')
plt.legend()
plt.show()
