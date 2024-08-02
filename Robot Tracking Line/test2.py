import matplotlib.pyplot as plt
import numpy as np

# Data
B = 10
E01 = 0
E11 = 0
E02 = 0
E12 = 0
E13 = 0
E03 = 0
theta00 = theta10 = np.radians(0)
SumE1 = SumE2 = SumE3 = 0
key = 1

data_tho = [50, 100, 50, 50, 100, 50, 50, 100, 50, 50, 100, 50]
delta = [(0, 0, 0), (1, 1, 45), (0, 0, 0), (0, 0, 0)]
data = []
distance = 5

# Calculate values based on distance
for i in range(0, len(data_tho)):
    data.append(data_tho[i] * distance / 100)

# Calculate maximum values and their positions
max_values = []
points = []
points_v1 = []
points_new_draw = []

for i in range(0, len(data), 3):
    sub_array = data[i:i+3]
    max_value = max(sub_array)
    max_index = i + sub_array.index(max_value)
    max_values.append((max_value, max_index))

print("Maximum values and their positions:")
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
    print("Max value:", max_value, "| Position:", max_index)

# Calculate center coordinates of the lines
for i in range(1, len(points)):
    x_new = points[i - 1] * np.cos(np.radians(theta10)) + delta[i - 1][0]
    y_new = points[i - 1] * np.sin(np.radians(theta10)) + delta[i - 1][1]
    points_new_draw.append((x_new, y_new))
    x_new = points[i] * np.cos(np.radians(theta10)) + delta[i][0]
    y_new = points[i] * np.sin(np.radians(theta10)) + delta[i][1]
    points_new_draw.append((x_new, y_new))

    # Line deviation
    if key == 1:
        if points_new_draw[-1][1] != points_new_draw[-2][1]:
            E13 = np.radians(delta[i][2] - delta[i - 1][2]) - theta10
        else:
            E13 = 0  
    else:
        if points_new_draw[-1][0] >= points_new_draw[-2][0]:
            E13 = np.radians(90) - np.arccos(B / points_v1[i]) - theta10
        else:
            E13 = -np.arccos(B / points_v1[i]) - theta10

    # Calculate E1, E2, E3
    E11 = np.cos(np.radians(theta10)) * (points_new_draw[-1][0] - points_new_draw[-2][0]) + \
          np.sin(np.radians(theta10)) * (points_new_draw[-1][1] - points_new_draw[-2][1])
    E12 = -np.sin(np.radians(theta10)) * (points_new_draw[-1][0] - points_new_draw[-2][0]) + \
          np.cos(np.radians(theta10)) * (points_new_draw[-1][1] - points_new_draw[-2][1])

    # Handle NaN values
    E11 = 0 if np.isnan(E11) else E11
    E12 = 0 if np.isnan(E12) else E12
    E13 = 0 if np.isnan(E13) else E13
    theta10 += E13

    # Vehicle position deviation
    E01 = np.cos(np.radians(theta00)) * (delta[i][0] - delta[i - 1][0]) + \
          np.sin(np.radians(theta00)) * (delta[i][1] - delta[i - 1][1])
    E02 = -np.sin(np.radians(theta00)) * (delta[i][0] - delta[i - 1][0]) + \
          np.cos(np.radians(theta00)) * (delta[i][1] - delta[i - 1][1])
    E03 = np.radians(delta[i][2]) - theta00
    theta00 += E03

    # Handle NaN values
    E01 = 0 if np.isnan(E01) else E01
    E02 = 0 if np.isnan(E02) else E02
    E03 = 0 if np.isnan(E03) else E03

    E1 = -E11 + E01
    E2 = -E12 + E02
    E3 = -E13 + E03
    SumE1 += E1
    SumE2 += E2
    SumE3 += E3
    print(E11, E12, E13, SumE1, SumE2, SumE3, E01, E02, E03)
for i in range(len(points_new_draw)):
    plt.scatter(points_new_draw[i][0], points_new_draw[i][1], color='red')

# Draw lines connecting the centers of the lines (points_new) in red
for i in range(len(points_new_draw) - 1):
    plt.plot([points_new_draw[i][0], points_new_draw[i + 1][0]], 
             [points_new_draw[i][1], points_new_draw[i + 1][1]], color='red')

# Draw circles at the vehicle positions (delta) in black
for i in range(len(delta)):
    plt.scatter(delta[i][0], delta[i][1], color='black')

# Draw lines connecting the vehicle positions (delta) in black
for i in range(len(delta) - 1):
    plt.plot([delta[i][0], delta[i + 1][0]], 
             [delta[i][1], delta[i + 1][1]], color='black', linestyle='--')

plt.title('Data Plot with Lines Connecting Centers and Vehicle Positions')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.legend(['Đường line', 'Vị trí xe'], loc='upper left')
plt.show()

