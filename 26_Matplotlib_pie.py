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

# Genera el gráfico de torta
colores = ['gold', 'lightskyblue', 'lightgreen']
explode = (0.1, 0, 0)  # El primer valor (0.1) resalta la primera categoría
plt.pie(valores, labels=categorias, autopct='%1.1f%%', startangle=90, colors=colores, explode=explode, shadow=True, wedgeprops={'edgecolor': 'gray'}) # shadow=True, wedgeprops={'edgecolor': 'gray'} agrega sombra y un borde al gráfico
plt.axis('equal') # Hace que el círculo sea una forma perfecta
plt.title('Emigración Argentina a España, Italia y Estados Unidos')
plt.show()
