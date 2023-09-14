import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos y preparar el DataFrame
df = pd.read_csv(r'D:\Germán\Desktop\Python Files\automobile.csv')
df = df.dropna(axis=0)

# Genera el gráfico
plt.boxplot([df['price'], df['horsepower']], labels=['Precio', 'Potencia'])

# Opcional: Personalizar el gráfico
plt.title('Gráfico de Caja Múltiple')
plt.xlabel('Categorías')
plt.ylabel('Valores')
plt.grid(True)

# Muestra el gráfico
plt.show()
