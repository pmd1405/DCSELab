import matplotlib.pyplot as plt
import numpy as np

# Khởi tạo dữ liệu và tính toán các giá trị
B = 10
E11 = E12 = E13 = 0
SumE11 = SumE12 = SumE13 = 0
theta10 = np.radians(0)

data_tho = [50, 50, 50, 50, 60, 40, 40, 60, 50, 50, 50, 50]
distance = 5
data = []
for value in data_tho:
    data.append(value * distance / 100)
points = []
points_v1 = []

for i in range(0, len(data)-1, 2):
    point1 =  (distance/2 - data[i])
    point2 = (distance/2 - data[i + 1])
    delta_x = (point2 - point1) / 2
    Line = point2 + point1 + B

    points_v1.append(Line)
    points.append(delta_x)

# Tính toán các giá trị E11, E12, E13 và tính tổng
E11_list = []
E12_list = []
E13_list = []

for i in range(1, len(points)):
    E11 = np.cos(theta10) * (points[i] - points[i-1]) + np.sin(theta10) * (points[i] - points[i-1])
    E12 = 0

    if points[i] >= points[i-1]:
        E13 = np.arccos(B / points_v1[i]) - theta10
    else:
        E13 = -np.arccos(B / points_v1[i]) - theta10

    E11 = 0 if np.isnan(E11) else E11
    E12 = 0 if np.isnan(E12) else E12
    E13 = 0 if np.isnan(E13) else E13
    theta10 += E13
    SumE11 += E11
    SumE12 += E12
    SumE13 += E13

    E11_list.append(E11)
    E12_list.append(E12)
    E13_list.append(E13)

    print("E1: ", E11, "E2: ", E12, "E3: ", E13, "Theta: ", theta10, "SumE1: ", SumE11, "SumE2: ",SumE12 ,"SumE3: ", SumE13)

# Vẽ đồ thị delta_x
plt.plot(points, range(0, len(points)), linewidth=10)
plt.title('Delta_x Plot')
plt.xlabel('Index')
plt.ylabel('Delta_x')
plt.grid(True)
plt.show()
