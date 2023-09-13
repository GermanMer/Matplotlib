import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos y preparar el DataFrame
df = pd.read_csv(r'D:\Germán\Desktop\Python Files\migration.csv')
df = df.dropna(axis=0)
df['Value'] = df['Value'].astype(int)

arg_esp = df[(df['Country of birth/nationality'] == 'Argentina') & (df['Country'] == 'Spain')]
arg_esp = arg_esp.groupby('Year')['Value'].sum().reset_index()

arg_ita = df[(df['Country of birth/nationality'] == 'Argentina') & (df['Country'] == 'Italy')]
arg_ita = arg_ita.groupby('Year')['Value'].sum().reset_index()

arg_usa = df[(df['Country of birth/nationality'] == 'Argentina') & (df['Country'] == 'United States')]
arg_usa = arg_usa.groupby('Year')['Value'].sum().reset_index()

# Preparar datos para el gráfico
años = arg_esp['Year']  # Tomar los años de uno de los DataFrames, ya que deberían ser los mismos
valores_esp = arg_esp['Value']
valores_ita = arg_ita['Value']
valores_usa = arg_usa['Value']

# Genera el gráfico de barras
plt.barh(años, valores_esp, label='Hacia España', color='blue', alpha=0.3)
plt.barh(años, valores_ita, label='Hacia Italia', color='green', alpha=0.3)
plt.barh(años, valores_usa, label='Hacia Estados Unidos', color='red', alpha=0.3)

plt.grid(True)  # Agregar una cuadrícula al gráfico
plt.xlabel('Año')
plt.ylabel('Cantidad de Emigrantes')
plt.title('Emigración Argentina a España, Italia y Estados Unidos')
plt.legend()
plt.tight_layout()  # Ajustar el diseño para evitar recortes en las etiquetas
plt.show()
