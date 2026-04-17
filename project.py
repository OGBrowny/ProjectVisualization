import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# ===================== CSV DATA =====================
df = pd.read_csv('train.csv')

# -------- BAR GRAPH --------
sales = df.groupby('Category')['Sales'].sum()
sales.plot(kind='bar')
plt.title('Bar Graph - Sales by Category')
plt.xlabel('Category')
plt.ylabel('Sales')
plt.show()

# -------- PIE CHART --------
sales.plot(kind='pie', autopct='%1.1f%%')
plt.title('Pie Chart - Sales Distribution')
plt.ylabel('')
plt.show()

# -------- LINE GRAPH --------
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
sales_time = df.groupby('Order Date')['Sales'].sum()
sales_time.plot()
plt.title('Line Graph - Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.show()

# -------- HISTOGRAM --------
plt.hist(df['Sales'], bins=10)
plt.title('Histogram - Sales Distribution')
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.show()

# ===================== NUMPY DATA =====================
x = np.linspace(1, 10, 50)
y = x**2

# -------- PLOT --------
plt.plot(x, y)
plt.title("Normal Plot")
plt.show()

# -------- SCATTER --------
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.show()

# -------- BAR (NUMPY) --------
plt.bar(x[:10], y[:10])
plt.title("Bar Graph (NumPy Data)")
plt.show()

# -------- LOGLOG --------
plt.loglog(x, y)
plt.title("Log-Log Plot")
plt.show()

# -------- SEMILOGX --------
plt.semilogx(x, y)
plt.title("Semilog X Plot")
plt.show()

# -------- SEMILOGY --------
plt.semilogy(x, y)
plt.title("Semilog Y Plot")
plt.show()

# ===================== SUBPLOTS =====================
plt.figure(figsize=(10,8))

plt.subplot(2,2,1)
sales.plot(kind='bar')
plt.title('Bar')

plt.subplot(2,2,2)
sales.plot(kind='pie', autopct='%1.1f%%')
plt.title('Pie')
plt.ylabel('')

plt.subplot(2,2,3)
plt.hist(df['Sales'], bins=10)
plt.title('Histogram')

plt.subplot(2,2,4)
sales_time.plot()
plt.title('Line')

plt.tight_layout()
plt.show()

# ===================== 3D SCATTER =====================
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x3 = np.linspace(1, 10, 50)
y3 = np.linspace(1, 10, 50)
z3 = x3 * y3

ax.scatter(x3, y3, z3)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.title("3D Scatter Plot")
plt.show()

# ===================== 3D (MESHGRID DATA) =====================
x = np.arange(-5, 5, 0.5)
y = np.arange(-5, 5, 0.5)

X, Y = np.meshgrid(x, y)
Z = np.sin(X) * np.cos(Y)

# -------- SURFACE --------
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z)
plt.title("Surface Plot")
plt.show()

# -------- WIREFRAME --------
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(X, Y, Z)
plt.title("Wireframe Plot")
plt.show()

# -------- CONTOUR --------
plt.contour(X, Y, Z)
plt.title("Contour Plot")
plt.show()