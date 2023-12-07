#CREA UN GRÁFICO DE LINEAS CON TODAS LAS COLUMNAS NUMÉRICAS DE UN DATA FRAME

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('company_sales_data.csv')

x = df['month_number']
y = df['bathingsoap']

plt.bar(x, y)

plt.xlabel('Month Number')
plt.ylabel('Sales units in numbers')
plt.title('Bathingsoap Sales Data')
plt.grid(True, linestyle='--')
plt.xticks(x)
plt.savefig('sales_data_of_bathingsoap.png', dpi=150) # ESTA LÍNEA GUARDA LA IMAGEN EN UN ARCHIVO!
plt.show()
