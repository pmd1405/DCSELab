import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def update_position(x, y, theta, d, wR, wL, a1, a2, dt, L):
    theta_dot = d * (wR - wL) / 2 / L
    V = d * (wR + wL) / 4

    # Tính toán vị trí mới
    x_new = x + V * np.cos(theta) * dt
    y_new = y + V * np.sin(theta) * dt
    theta_new = theta + theta_dot * dt
    
    # Tính toán vận tốc mới và giới hạn trong khoảng [-w_max, w_max]
    w_max = 100  # Vận tốc góc tối đa
    wR_new = np.clip(wR + a1 * dt, -w_max, w_max)
    wL_new = np.clip(wL + a2 * dt, -w_max, w_max)
    
    return x_new, y_new, theta_new, wR_new, wL_new

def animate(frame):
    global x, y, theta, wR, wL
    
    x, y, theta, wR, wL = update_position(x, y, theta, d, wR, wL, a1, a2, dt, L)
    x_positions.append(x)
    y_positions.append(y)
    
    # Xóa các frame cũ để vẽ frame mới
    plt.cla()
    
    # Vẽ quỹ đạo đi của robot
    plt.plot(x_positions, y_positions, label='Quỹ đạo đi của mobile robot')
    plt.scatter(x_positions[0], y_positions[0], color='green', label='Vị trí ban đầu')
    plt.scatter(x_positions[-1], y_positions[-1], color='red', label='Vị trí cuối cùng')
    
    # Tính toán tâm trục nối hai bánh
    center_x = (x_positions[-1] + x_positions[-2]) / 2
    center_y = (y_positions[-1] + y_positions[-2]) / 2
    
    # Tính toán chiều dài và chiều rộng của hình chữ nhật (bánh xe)
    length = d / 2
    width = 10
    
    # Tính toán góc quay của hình chữ nhật (bánh xe) thứ nhất
    rect_angle = np.arctan2(y_positions[-1] - y_positions[-2], x_positions[-1] - x_positions[-2]) * 180 / np.pi

    # Vẽ hình chữ nhật (bánh xe) thể hiện mobile robot
    rectangle1 = plt.Rectangle((center_x + L/2 * np.cos(np.deg2rad(rect_angle + 90)), 
                                center_y + L/2 * np.sin(np.deg2rad(rect_angle + 90))),
                               length, width, angle=rect_angle, edgecolor='blue', facecolor='none')
    plt.gca().add_patch(rectangle1)
    
    # Tính toán góc quay của hình chữ nhật (bánh xe) thứ hai
    rect_angle2 = rect_angle + 180

    # Vẽ hình chữ nhật (bánh xe) thứ hai
    rectangle2 = plt.Rectangle((center_x - L/2 * np.cos(np.deg2rad(rect_angle + 90)), 
                                center_y - L/2 * np.sin(np.deg2rad(rect_angle + 90))),
                               -length, width, angle=rect_angle2, edgecolor='red', facecolor='none')
    plt.gca().add_patch(rectangle2)
    
    plt.title('Quỹ đạo đi của mobile robot')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.axis('square')
    plt.legend(loc='upper right')  # Cố định khung chú thích ở góc trên bên phải
    plt.grid(True)

    return []


def main():
    global x, y, theta, wR, wL, d, a1, a2, dt, L
    
    d = 65  # Đường kính bánh xe
    dt = 0.05  # Bước thời gian
    total_time = 1  # Thời gian tổng cộng để di chuyển
    
    time = np.arange(0, total_time, dt)

    x = 0.0
    y = 0.0
    theta = 0.0

    wR = 15
    wL = 10
    a1 = -1  # Gia tốc cho bánh phải
    a2 = -1  # Gia tốc cho bánh trái
    L = 100

    global x_positions, y_positions
    x_positions = [x]
    y_positions = [y]

    fig, ax = plt.subplots(figsize=(8, 6))
    ani = FuncAnimation(fig, animate, frames=range(len(time)), interval=1, blit=True)
    plt.show()

if __name__ == "__main__":
    main()
