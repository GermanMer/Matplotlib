import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos y preparar el DataFrame
df = pd.read_csv(r'D:\Germán\Desktop\Python Files\automobile.csv')
df = df.dropna(axis=0)

# Genera el gráfico con personalización
x = df['horsepower']
y = df['price']

# Personalización del gráfico
plt.scatter(x, y, c='b', marker='o', alpha=0.7, s=50, label='Datos')  # Personaliza puntos (color, forma, transparencia, sombra y etiqueta)
plt.xlabel('Potencia (HP)', fontsize=12)  # Etiqueta del eje x
plt.ylabel('Precio ($)', fontsize=12)  # Etiqueta del eje y
plt.title('Relación entre Potencia y Precio', fontsize=16)  # Título del gráfico
plt.grid(True, linestyle='--', alpha=0.5)  # Agrega una cuadrícula punteada

# Agrega una leyenda
plt.legend(loc='upper right', fontsize=10)

# Muestra el gráfico
plt.show()
