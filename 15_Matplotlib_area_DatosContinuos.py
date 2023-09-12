import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos y preparar el DataFrame
df = pd.read_csv(r'D:\Germán\Desktop\Python Files\migration.csv')
df = df.dropna(axis=0)
df['Value'] = df['Value'].astype(int)
argentina = df[(df['Country of birth/nationality'] == 'Argentina') & (df['Country'] == 'Spain')]
argentina = argentina.groupby('Year')['Value'].sum().reset_index()

# Genera el gráfico
x = argentina['Year']
y = argentina['Value']
plt.fill_between(x, y, label='De Argentina hacia España', color='blue', alpha=0.3)
plt.grid(True)  # Agregar una cuadrícula al gráfico
plt.xlabel('Año')
plt.ylabel('Cantidad de Emigrantes')
plt.title('Emigración de Argentina a España')
plt.legend()
plt.tight_layout()  # Ajustar el diseño para evitar recortes en las etiquetas
plt.show()
