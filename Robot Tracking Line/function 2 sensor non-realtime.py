import matplotlib.pyplot as plt
import numpy as np

# Khởi tạo dữ liệu và tính toán các giá trị
B = 10
theta10 = np.pi/2
v = 10
t = 0.1

data_tho1 = [50, 50, 50, 50, 55, 45, 60, 40, 65, 35, 70, 30, 75, 25, 80, 20, 75, 25, 70, 30, 65, 35, 60, 40, 55, 45, 50, 50, 50, 50]
data_tho = [50, 50, 50, 50, 60, 50, 50, 50, 50, 60, 50, 50]
data_tho1 = [50, 50, 50, 50, 50, 50, 40, 60, 30, 70, 20, 80, 10, 90, 0, 100, 0, 100, 2, 98, 6, 92, 12, 86, 20, 78, 30, 68, 42, 56, 56, 42, 72, 26, 90, 8, 110, -12, 132, -34, 156, -58, 182, -84]
distance = 5
data = [value * distance / 100 for value in data_tho]

point1 = []
point2 = []
L = []
center = []
phr = [np.pi/2]

# Tính toán các giá trị điểm, đường trung tâm và chiều dài
for i in range(0, len(data), 2):
    point1.append( distance/2 - data[i] - B/2) 
    point2.append(B/2 + (data[i+1] - distance/2))
    Line = point2[-1] - point1[-1]
    center.append((B/2 + (data[i+1] - distance/2) - B/2 + (distance/2 - data[i]))/2)
    L.append(Line)
xr = [0]
yr = [0]
E13 = 0
for i in range(1, len(point1)):

    if L[i] > B:
        if center[i]>0:
            E13 = -np.arccos(B / L[i])
        elif center[i]<0:
            E13 = np.arccos(B / L[i])
        else:
            E13 = 0
    else:
        E13 = 0
    y=np.sqrt((v*t)**2 - center[i]**2)
    x=center[i]
    xr.append(x*np.cos(theta10-phr[0]) - y*np.sin(theta10-phr[0]) + xr[i-1])
    yr.append(x*np.sin(theta10-phr[0]) + y*np.cos(theta10-phr[0]) + yr[i-1])
    point1[i]=(point1[i] + B/2)*np.cos(theta10-phr[0]) - y*np.sin(theta10-phr[0]) + point1[i-1]
    point2[i]=(point2[i] - B/2)*np.cos(theta10-phr[0]) - y*np.sin(theta10-phr[0]) + point2[i-1]
    theta10 += E13
    phr.append(theta10)
print(np.degrees(phr))
# Vẽ đồ thị delta_x
plt.figure()  # Create a new figure
  # First subplot for Xr Yr Plot

plt.plot(xr, yr, linewidth=5, color="black", label='Centerline of line tracking')
plt.plot([p1 for p1 in point1], yr, color="blue", linewidth=2, label='Left edge of the line')
plt.plot([p1 for p1 in point2], yr, color="blue", linewidth=2, label='Right edge of the line')
plt.scatter(xr, yr, color="red", linewidth=5, label='Point Value')
# plt.vlines(-distance/2 - B/2, ymin=yr[0], ymax=yr[-1], linestyle='dashed', color='orange', label='Workspace boundary')
# plt.vlines(distance/2 - B/2, ymin=yr[0], ymax=yr[-1], linestyle='dashed', color='orange', label='Workspace boundary')
# plt.vlines(-distance/2 + B/2, ymin=yr[0], ymax=yr[-1], linestyle='dashed', color='orange', label='Workspace boundary')
# plt.vlines(distance/2 + B/2, ymin=yr[0], ymax=yr[-1], linestyle='dashed', color='orange', label='Workspace boundary')
plt.legend()
plt.title('Xr Yr Plot')
plt.xlabel('xr')
plt.ylabel('yr')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)  # Second subplot for phr plot
plt.plot(range(len(phr)), np.degrees(phr), color='green', label='Phr')
plt.scatter(range(len(phr)), np.degrees(phr), color='red', linewidth=5, label='Point Value')
plt.title('Change of Phr')
plt.xlabel('Time step')
plt.ylabel('Phr (degrees)')
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)  # Second subplot for phr plot
plt.plot( range(len(L)),L,  color='green', label='L')
plt.scatter( range(len(L)),L, color="red", linewidth=5, label='Point Value')
plt.title('Change of L')
plt.xlabel('Time step')
plt.ylabel('mm')
plt.legend()
plt.grid(True)

plt.tight_layout()  # Adjust subplots to fit into the figure area without overlapping
plt.show()
