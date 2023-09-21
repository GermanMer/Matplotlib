import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Cargar los datos de emigración desde el archivo CSV
df = pd.read_csv(r'D:\Germán\Desktop\Python Files\migration.csv')
df = df.dropna(axis=0)
df['Value'] = df['Value'].astype(int)

# Filtrar y procesar los datos para cada uno de los 3 países
arg_esp = df[(df['Country of birth/nationality'] == 'Argentina') & (df['Country'] == 'Spain')]
arg_esp = arg_esp.groupby('Year')['Value'].sum().reset_index()

arg_ita = df[(df['Country of birth/nationality'] == 'Argentina') & (df['Country'] == 'Italy')]
arg_ita = arg_ita.groupby('Year')['Value'].sum().reset_index()

arg_usa = df[(df['Country of birth/nationality'] == 'Argentina') & (df['Country'] == 'United States')]
arg_usa = arg_usa.groupby('Year')['Value'].sum().reset_index()

# Combinar los datos de los tres destinos en un solo DataFrame
combined_data = pd.concat([arg_esp, arg_ita, arg_usa], keys=['España', 'Italia', 'Estados Unidos'])

# Obtener la lista de años únicos desde los datos de emigración
available_years = combined_data['Year'].unique()

# Configura la figura y el eje con tamaño personalizado
fig, ax = plt.subplots(figsize=(10, 6))  # Ancho: 10 pulgadas, Alto: 6 pulgadas
ln1, = plt.plot([], [], 'r-', animated=True, label='Hacia España')
ln2, = plt.plot([], [], 'b-', animated=True, label='Hacia Italia')
ln3, = plt.plot([], [], 'g-', animated=True, label='Hacia Estados Unidos')

lines = [ln1, ln2, ln3]

def init():
    ax.set_xlim(available_years.min(), available_years.max())
    ax.set_ylim(0, combined_data['Value'].max())
    ax.set_xlabel('Año')
    ax.set_ylabel('Cantidad de Emigrantes')
    ax.set_title('Emigración de Argentina a España, Italia y Estados Unidos')
    ax.set_xticks(range(int(available_years.min()), int(available_years.max()) + 1))  # Establecer ticks de uno en uno
    ax.legend(loc='upper left')  # Agregar leyenda
    return lines

def update(frame):
    if frame == len(available_years) - 1:
        ani.event_source.stop()  # Detener la animación en el último frame
    for line, country in zip(lines, ['España', 'Italia', 'Estados Unidos']):
        data = combined_data.xs(country, level=0)
        xdata = data['Year'][:frame+1]
        ydata = data['Value'][:frame+1]
        line.set_data(xdata, ydata)
    return lines

ani = FuncAnimation(fig, update, frames=len(available_years), init_func=init, blit=True)

# Personalizar el aspecto visual
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

plt.show()
