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

# Genera el gráfico
x = arg_esp['Year']
y1 = arg_esp['Value']
y2 = arg_ita['Value']
y3 = arg_usa['Value']

plt.plot(x, y1, label='Hacia España', color='blue', linestyle='-', marker='o')
plt.plot(x, y2, label='Hacia Italia', color='green', linestyle='--', marker='s')
plt.plot(x, y3, label='Hacia Estados Unidos', color='red', linestyle=':', marker='^')

plt.grid(True)  # Agregar una cuadrícula al gráfico
plt.xlabel('Año')
plt.ylabel('Cantidad de Emigrantes')
plt.title('Emigración Argentina a España, Italia y Estados Unidos')
plt.legend()
plt.tight_layout()  # Ajustar el diseño para evitar recortes en las etiquetas
plt.show()
