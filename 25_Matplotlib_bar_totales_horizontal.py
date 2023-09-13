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
categorias = ['Hacia España', 'Hacia Italia', 'Hacia Estados Unidos']
valores = [arg_esp['Value'].sum(), arg_ita['Value'].sum(), arg_usa['Value'].sum()]

# Genera el gráfico de barras
plt.barh(categorias, valores, color=['blue', 'green', 'red'], alpha=0.3)

plt.ticklabel_format(style='plain', axis='x') # Configura el formato del eje y para evitar la notación científica
plt.grid(True)  # Agregar una cuadrícula al gráfico
plt.xlabel('Destino')
plt.ylabel('Cantidad de Emigrantes')
plt.title('Emigración Argentina a España, Italia y Estados Unidos')
plt.xticks(rotation=45)  # Rotar los valores en el eje x para una mejor legibilidad
plt.tight_layout()  # Ajustar el diseño para evitar recortes en las etiquetas
plt.show()
