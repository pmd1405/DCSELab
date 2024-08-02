import matplotlib.pyplot as plt
import numpy as np

# Khởi tạo dữ liệu và tính toán các giá trị
B = 10
E11 = E12 = E13 = 0
SumE11 = SumE12 = SumE13 = 0
theta10 = np.radians(0)
data_tho = [50, 100, 50, 50, 100, 50, 60, 100, 40, 60, 100, 40, 60, 100, 50, 50, 100, 60, 50, 100, 50, 50, 100, 50]
distance = 5
data = []
for value in data_tho:
    data.append(value * distance / np.max(data_tho))
max_values = []
for i in range(0, len(data), 3):
    sub_array = data[i:i+3]
    max_value = max(sub_array)
    max_index = i + sub_array.index(max_value)
    max_values.append((max_value, max_index))
points = []
points_v1 = []

for max_value, max_index in max_values:
    if max_index % 3 == 1:
        point1 = -distance / 2 - data[max_index - 1]
        point2 = distance / 2 + data[max_index + 1]
    elif max_index % 3 == 0:
        point1 = -distance * 1.5
        point2 = -distance / 2 + data[max_index + 1]
    else:
        point1 = distance / 2 - data[max_index - 1]
        point2 = distance * 1.5
    delta_x = (point2 + point1) / 2
    points_v1.append(point2 - point1)
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

    print("E1: ", E11, "E2: ", E12, "E2: ", E13, "Theta: ", theta10, "SumE1: ", SumE11, "SumE2: ",SumE12 ,"SumE3: ", SumE13)

# Vẽ đồ thị delta_x
plt.plot(points, np.array([1,3,5,6,7,10,11,13]), linewidth=10)
plt.title('Delta_x Plot')
plt.xlabel('Index')
plt.ylabel('Delta_x')
plt.grid(True)
plt.show()
