import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

def plot_distance(ax, width1, height1, width2, height2, delta1, delta2, D, base_length1, base_length2, n):
    distance_between_ellipses = height2/2  # Khoảng cách giữa các hình ellipse
    for i in range(n):
        # Tạo hình ellipse
        ellipse1 = Ellipse((width1/2+delta1, i*distance_between_ellipses), width=width1, height=height1, edgecolor='g', facecolor='none')
        ellipse2 = Ellipse((width2/2+delta2, i*distance_between_ellipses), width=width2, height=height2, edgecolor='g', facecolor='none')
        intersection_patch = Ellipse((width1/2+delta1, i*distance_between_ellipses), width=width1, height=height1, edgecolor='none', facecolor='yellow', alpha=0.5)
        ax.add_patch(intersection_patch)
        # Thêm ellipse vào axes
        ax.add_patch(ellipse1)
        ax.add_patch(ellipse2)
        # Đặt tiêu đề và nhãn trục
        ax.set_title('Ellipse')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        # Hiển thị lưới
        ax.grid(True)
        ax.set_xlim([-width1, distance_between_ellipses])  # Assuming maximum range for x-axis is -5 to 5
        ax.set_ylim([-D, distance_between_ellipses*n])
    print("Distance Min: ",height2/2+height1, n*(height1)+(n-1)*height2/2)
    print("Distance Max: ",height1*2.8, height1*2.8*n)
    

def calculate_intersection_area(width1, height1, delta1, width2, height2, delta2):
    # Tính diện tích giao nhau bằng phương pháp tích phân
    def ellipse_eq1(x, y):
        return ((x - delta1) ** 2) / ((width1/2) ** 2) + (y ** 2) / ((height1/2) ** 2) - 1

    def ellipse_eq2(x, y):
        return ((x - delta2 - d) ** 2) / ((width2/2) ** 2) + (y ** 2) / ((height2/2) ** 2) - 1

    # Tích phân hai hàm số trên vùng giao nhau
    def integrand(x, y):
        return 1 if (ellipse_eq1(x, y) <= 0) and (ellipse_eq2(x, y) <= 0) else 0

    # Tính diện tích bằng phương pháp tích phân
    x_min = min(delta1, delta2)
    x_max = max(delta1 + width1, delta2 + width2)
    y_min = -max(height1, height2)
    y_max = max(height1, height2)

    dx = (x_max - x_min) / 1000  # Số lượng điểm chia theo trục x
    dy = (y_max - y_min) / 1000  # Số lượng điểm chia theo trục y

    # Tích phân bằng phương pháp hình chữ nhật
    intersection_area = 0
    for x in np.arange(x_min, x_max, dx):
        for y in np.arange(y_min, y_max, dy):
            intersection_area += integrand(x, y) * dx * dy

    return intersection_area

def plot_ellipse(ax, width1, height1, width2, height2, delta1, delta2, D):
    # Tạo hình ellipse
    ellipse1 = Ellipse((width1/2+delta1, 0), width=width1, height=height1, edgecolor='g', facecolor='none')
    ellipse2 = Ellipse((width2/2+delta2, 0), width=width2, height=height2, edgecolor='g', facecolor='none')
    # Thêm ellipse vào axes
    ax.add_patch(ellipse1)
    ax.add_patch(ellipse2)
    # Tính diện tích giao nhau
    intersection_area = calculate_intersection_area(width1, height1, delta1, width2, height2, delta2)
    # Bôi màu vùng diện tích giao nhau
    intersection_patch = Ellipse((width1/2+delta1, 0), width=width1, height=height1, edgecolor='none', facecolor='yellow', alpha=0.5)
    ax.add_patch(intersection_patch)
    # Đặt giới hạn trục x và y
    ax.set_xlim(-max(width1,width2,height1,height2), max(width1,width2,height1,height2))
    ax.set_ylim(-max(width1,width2,height1,height2), max(width1,width2,height1,height2))
    ax.plot([d, d], [h, -h], 'k--')
    ax.plot([0, 0], [h, -h], 'k--')
    # Đặt tiêu đề và nhãn trục
    ax.set_title('Ellipse')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    # Hiển thị lưới
    ax.grid(True)
    ax.set_xlim([-D, D])  # Assuming maximum range for x-axis is -5 to 5
    ax.set_ylim([-D, D])
    calculate_intersection_width_and_height(width1, height1, delta1, width2, height2, delta2)
    print("Diện tích giao nhau của hai ellipse: ", intersection_area)

def calculate_intersection_width_and_height(width1, height1, delta1, width2, height2, delta2):
    # Tính tọa độ của các điểm cực trị trên ellipse 1
    x1_max = delta1 + width1/2
    x1_min = delta1 - width1/2
    y1_max = height1/2
    y1_min = -height1/2

    # Tính tọa độ của các điểm cực trị trên ellipse 2
    x2_max = delta2 + width2/2
    x2_min = delta2 - width2/2
    y2_max = height2/2
    y2_min = -height2/2

    # Tính khoảng cách giữa các điểm cực trị theo các hướng khác nhau
    intersection_height = min(y1_max, y2_max) - max(y1_min, y2_min)

    print("Độ rộng của vùng giao nhau:", intersection_height)

def plot_isosceles_triangle(ax, alpha1, h, beta1, alpha2, beta2, d, dmin1, dmin11, dmin111, dmin2, n):
    # Tính độ dài của cạnh đáy
    base_length1 = h * np.tan(np.radians(alpha1/2))
    base_length2 = h * np.tan(np.radians(alpha2/2))
    if h<dmin2/2/np.tan(np.radians(alpha1/2)):
        height1=dmin2
    else:
        height1=2*base_length1
    if h<dmin2/2/np.tan(np.radians(alpha2/2)):
        height2=dmin2
    else:
        height2=2*base_length2

    width1=h * np.tan(np.radians(alpha1/2+beta1))+h * np.tan(np.radians(alpha1/2-beta1))
    width2=h * np.tan(np.radians(alpha2/2-beta2))+h * np.tan(np.radians(alpha2/2+beta2))

    delta1=-h * np.tan(np.radians(alpha1/2-beta1))
    delta2=d-h * np.tan(np.radians(alpha2/2+beta2))
    # Tính các điểm của tam giác
    x1 = np.array([-base_length1, 0, base_length1, -base_length1])
    y1 = np.array([0, h, 0, 0])
    x2 = np.array([d-base_length2, d, d+base_length2, d-base_length2])
    y2 = np.array([0, h, 0, 0])

    xx1 = np.array([-h * np.tan(np.radians(alpha1/2-beta1)), 0, h * np.tan(np.radians(alpha1/2+beta1)), -h * np.tan(np.radians(alpha1/2-beta1))])
    yy1 = np.array([0, h, 0, 0])
    xx2 = np.array([d-h * np.tan(np.radians(alpha2/2+beta2)), d, d+h * np.tan(np.radians(alpha2/2-beta2)), d-h * np.tan(np.radians(alpha2/2+beta2))])
    yy2 = np.array([0, h, 0, 0])

    hx1=(dmin11+dmin111)/np.tan(np.radians(alpha1/2+beta1))
    hx2=(dmin1+dmin11)/np.tan(np.radians(alpha2/2+beta2))
    if h<=hx2 :
        D=6.7
    elif hx2<h<hx1:
        D=6.7+np.tan(np.radians(alpha2/2+beta2))*(h-hx2)
    elif h>=hx1:
        D=6.7+np.tan(np.radians(alpha1/2+beta1))*(h-hx1)+np.tan(np.radians(alpha2/2+beta2))*(h-hx2)
    print("D: ", D)
    print("Dx / dead: ", height1, height2-height1, height1/(height2-height1))
    print("Dx: ", width1, width2)
    print("Dy: ", height1, height2)

    # Vẽ tam giác và ellipse
    ax.plot(xx1, yy1, 'b-')
    ax.fill(xx1, yy1, 'b', alpha=0.3)
    ax.plot(xx2, yy2, 'r-')
    ax.fill(xx2, yy2, 'r', alpha=0.3)

    intersection_width = min(h * np.tan(np.radians(alpha1/2+beta1)), d+h * np.tan(np.radians(alpha2/2-beta2))) - max(-h * np.tan(np.radians(alpha1/2-beta1)), d-h * np.tan(np.radians(alpha2/2+beta2)))
    print("Độ dài của vùng giao nhau:", intersection_width)

    plot_triangle(ax2, alpha1, h, alpha2, D)
    plot_ellipse(ax3, width1, height1, width2, height2, delta1, delta2, D)
    plot_distance(ax4, width1, height1, width2, height2, delta1, delta2, D, base_length1, base_length2, n)
    # Đặt tiêu đề và nhãn trục
    ax.set_title('Isosceles Triangle with Rotation')
    ax.set_xlim([-D, D])  # Assuming maximum range for x-axis is -5 to 5
    ax.set_ylim([-D, D])
    # Hiển thị lưới
    ax.grid(True)

def plot_triangle(ax, alpha1, h, alpha2, D):
    # Tính độ dài của cạnh đáy
    base_length1 = h * np.tan(np.radians(alpha1/2))
    base_length2 = h * np.tan(np.radians(alpha2/2))
    # Tính các điểm của tam giác
    x1 = np.array([-base_length1, 0, base_length1, -base_length1])
    y1 = np.array([0, h, 0, 0])
    x2 = np.array([-base_length2, 0, base_length2, -base_length2])
    y2 = np.array([0, h, 0, 0])

    # Vẽ tam giác và ellipse
    ax.plot(x1, y1, 'b-')
    ax.fill(x1, y1, 'b', alpha=0.3)
    ax.plot(x2, y2, 'r-')
    ax.fill(x2, y2, 'r', alpha=0.3)
    # Đặt tiêu đề và nhãn trục
    ax.set_title('Isosceles Triangle')
    ax.set_xlim([-D, D])  # Assuming maximum range for x-axis is -5 to 5
    ax.set_ylim([-D, D])
    # Hiển thị lưới
    ax.grid(True)

# Tạo figure và axes
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10, 8))

# Góc ở đỉnh và độ cao của tam giác
alpha1 = 32  # Đơn vị: độ
h = 6
beta1 = 13.5

alpha2 = 60  # Đơn vị độ
beta2 = 13.5
d = 2.7
n=3

# Chiều rộng và chiều cao của ellipse
dmin1=2
dmin11=2.7
dmin111=2
dmin2=3.1
# Vẽ tam giác và ellipse
plot_isosceles_triangle(ax1, alpha1, h, beta1, alpha2, beta2, d, dmin1, dmin11, dmin111, dmin2, n)
# Hiển thị figure
plt.show()
