import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Cargar los datos de emigración desde el archivo CSV
df = pd.read_csv(r'D:\Germán\Desktop\Python Files\migration.csv')

# Filtrar y procesar los datos para Argentina a España
argentina_spain = df[(df['Country of birth/nationality'] == 'Argentina') & (df['Country'] == 'Spain')]
argentina_spain = argentina_spain.groupby('Year')['Value'].sum().reset_index()

# Obtener la lista de años únicos desde los datos de emigración
available_years = argentina_spain['Year'].unique()

# Configura la figura y el eje con tamaño personalizado
fig, ax = plt.subplots(figsize=(10, 6))  # Ancho: 10 pulgadas, Alto: 6 pulgadas
xdata, ydata = [], []
ln, = plt.plot([], [], 'r-', animated=True)

def init():
    ax.set_xlim(available_years.min(), available_years.max())
    ax.set_ylim(0, argentina_spain['Value'].max())
    ax.set_xlabel('Año')
    ax.set_ylabel('Cantidad de Emigrantes')
    ax.set_title('Emigración de Argentina a España')
    ax.set_xticks(range(int(available_years.min()), int(available_years.max()) + 1))  # Establecer ticks de uno en uno
    return ln,

def update(frame):
    if frame == len(available_years) - 1:
        ani.event_source.stop()  # Detener la animación en el último frame
    xdata.append(available_years[frame])
    ydata.append(argentina_spain['Value'].iloc[frame])
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames=len(available_years), init_func=init, blit=True)

# Personalizar el aspecto visual
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

plt.show()
