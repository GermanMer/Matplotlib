import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos y preparar el DataFrame
df = pd.read_csv(r'D:\Germán\Desktop\Python Files\automobile.csv')
df = df.dropna(axis=0)

# Genera el gráfico
plt.boxplot(df['price'])

# Opcional: Personalizar el gráfico
plt.title('Distribución del Precio de los Automóbiles')
plt.xlabel('Automóbiles')
plt.ylabel('Precio')
plt.grid(True)

# Muestra el gráfico
plt.show()
