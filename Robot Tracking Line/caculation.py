import numpy as np
import matplotlib.pyplot as plt

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

def calculate_radius(x_positions, y_positions):
    center_x = np.mean(x_positions)
    center_y = np.mean(y_positions)
    
    radii = np.sqrt((x_positions - center_x)**2 + (y_positions - center_y)**2)
    
    return np.mean(radii)

def main():
    d = 65  # Đường kính bánh xe
    dt = 0.1  # Bước thời gian
    total_time = 2  # Thời gian tổng cộng để di chuyển
    
    time = np.arange(0, total_time, dt)

    x = 0.0
    y = 0.0
    theta = 0.0

    response_time=1
    R=500
    wR = 15
    wL = 15
    a1 = 0  # Gia tốc cho bánh phải
    a2 = 0  # Gia tốc cho bánh trái
    L = 100
    distance=R*R-(response_time*d*(wR+a1*response_time+wL+a2*response_time)/4)**2
    if distance<0:
        print("Nên giảm vận tốc: ", 2*R/response_time/d)
    else:
        print("Distance Min: ", np.sqrt(distance), np.sqrt(distance)*1.1)
    
    x_positions = [x]
    y_positions = [y]
S
    for i in range(len(time)):
        x, y, theta, wR, wL = update_position(x, y, theta, d, wR, wL, a1, a2, dt, L)
        x_positions.append(x)
        y_positions.append(y)
    
    plt.figure(figsize=(8, 6))
    plt.plot(x_positions, y_positions, label='Quỹ đạo đi của mobile robot')
    plt.scatter(x_positions[0], y_positions[0], color='green', label='Vị trí ban đầu')
    plt.scatter(x_positions[-1], y_positions[-1], color='red', label='Vị trí cuối cùng')
    circle = plt.Circle((0, -R), R, color='blue', fill=False, linestyle='--', linewidth=2)
    plt.gca().add_patch(circle)
    plt.title('Quỹ đạo đi của mobile robot')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.axis('square')
    plt.legend()
    plt.grid(True)
    plt.show()

    radius = calculate_radius(np.array(x_positions), np.array(y_positions))

    print("Bán kính của quỹ đạo:", radius)

if __name__ == "__main__":
    main()
