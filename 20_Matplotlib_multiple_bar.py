import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('company_sales_data.csv')

x = df['month_number']
y1 = df['facecream']
y2 = df['facewash']

plt.bar([a-0.25 for a in x], y1, width= 0.25, label='Facecream Sales Data', color='c', align='edge')
plt.bar([a+0.25 for a in x], y2, width= -0.25, label='Facewash Sales Data', color='orange', align='edge')

plt.xlabel('Month Number')
plt.ylabel('Sales units in numbers')
plt.title('Facecream and Facecream Sales Data')
plt.legend(loc='upper left')
plt.grid(True, linestyle='--')
plt.xticks(x)
plt.show()
