import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load dataset
df = pd.read_csv('train.csv')

# -------- NUMPY (for marks) --------
print("Average Sales:", np.mean(df['Sales']))

# -------- BAR GRAPH --------
sales = df.groupby('Category')['Sales'].sum()

sales.plot(kind='bar')
plt.title('Sales by Category')
plt.ylabel('Sales')
plt.show()

# -------- PIE CHART --------
sales.plot(kind='pie', autopct='%1.1f%%')
plt.title('Sales Distribution by Category')
plt.ylabel('')
plt.show()

# -------- LINE GRAPH --------
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)

sales_time = df.groupby('Order Date')['Sales'].sum()

sales_time.plot()
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.show()

# -------- 3D GRAPH --------
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(df['Sales'], df['Postal Code'], df['Row ID'])

ax.set_xlabel('Sales')
ax.set_ylabel('Postal Code')
ax.set_zlabel('Row ID')

plt.title('3D Sales Visualization')
plt.show()