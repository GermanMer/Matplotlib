import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('company_sales_data.csv')

x = df['month_number']
y1 = df['facecream']
y2 = df['facewash']
y3 = df['toothpaste']
y4 = df['bathingsoap']
y5 = df['shampoo']
y6 = df['moisturizer']

plt.plot([],[],color='m', label='face Cream', linewidth=5)
plt.plot([],[],color='c', label='Face wash', linewidth=5)
plt.plot([],[],color='r', label='Tooth paste', linewidth=5)
plt.plot([],[],color='k', label='Bathing soap', linewidth=5)
plt.plot([],[],color='g', label='Shampoo', linewidth=5)
plt.plot([],[],color='y', label='Moisturizer', linewidth=5)

plt.stackplot(x, y1, y2, y3, y4, y5, y6, colors=['m','c','r','k','g','y'])

plt.xlabel('Month Number')
plt.ylabel('Sales units in numbers')
plt.title('All product sales data using stack plot')
plt.legend(loc='upper left')
plt.show()
