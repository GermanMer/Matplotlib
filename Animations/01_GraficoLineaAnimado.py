import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Supongamos que tienes un DataFrame llamado df con columnas 'tiempo' y 'valor' que quieres animar.
df = pd.DataFrame({'tiempo': [0, 1, 2, 3, 4, 5],
                   'valor': [10, 12, 8, 15, 11, 9]})

# Configura la figura y el eje
fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'r-', animated=True)

def init():
    ax.set_xlim(0, max(df['tiempo']))
    ax.set_ylim(0, max(df['valor']))
    return ln,

def update(frame):
    xdata.append(df['tiempo'][frame])
    ydata.append(df['valor'][frame])
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames=len(df), init_func=init, blit=True)
plt.show()
