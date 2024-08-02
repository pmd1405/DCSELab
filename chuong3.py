import matplotlib.pyplot as plt

# Dữ liệu X và Y
X = [2, 3, 4, 5, 6, 7, 8]
Y = [11.698, 8.812, 7.648, 7.025, 6.638, 6.374, 6.184]

# Vẽ biểu đồ phân tán
plt.figure(figsize=(8, 6))
plt.scatter(X, Y, color='blue')
plt.title('Biểu đồ phân tán của X và Y')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
