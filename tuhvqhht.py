import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns  # Thêm dòng này để nhập thư viện Seaborn
from scipy.stats import norm

# Dữ liệu đo được
d_values = np.array([17.418, 17.591, 17.569, 17.396, 17.479, 17.726, 17.498, 17.347, 17.656, 17.553,
                    17.547, 17.501, 17.520, 17.322, 17.560, 17.269, 17.525, 17.428, 17.495, 17.364,
                    17.580, 17.364, 17.672, 17.425, 17.337, 17.584, 17.550, 17.595, 17.666, 17.452,
                    17.303, 17.252, 17.308, 17.242, 17.658, 17.536, 17.557, 17.971, 17.405, 17.325,
                    17.405, 17.801, 17.351, 17.872, 17.338, 17.277, 17.566, 17.557, 17.545, 17.549,
                    17.611, 17.387, 17.810, 17.355, 17.572, 17.341, 17.410, 17.691, 17.677, 17.431])

# Tính giá trị trung bình và độ lệch chuẩn
mean_d = np.mean(d_values)
std_d = np.std(d_values)

print("a) gia tri duong kinh cua d:", mean_d)
print("   do lech chuan cua d:", std_d)

confidence_interval = norm.interval(0.95, loc=mean_d, scale=std_d/np.sqrt(len(d_values)))
number_of_experiments = (norm.ppf(0.975) * std_d / (0.02 * mean_d))**2

print("c) Khoang tin cay ki vong (95%):", confidence_interval)
print("   So thi nghiem lap:", int(np.ceil(number_of_experiments)))

first_20_values = d_values[:20]
last_20_values = d_values[-20:]

mean_first_20 = np.mean(first_20_values)
std_first_20 = np.std(first_20_values)

mean_last_20 = np.mean(last_20_values)
std_last_20 = np.std(last_20_values)

print("d) Gia tri trung binh cua 20 gia tri dau:", mean_first_20)
print("   Do lech chuan cua 20 gia tri dau:", std_first_20)
print("   Gia tri trung binh cua 20 gia tri cuoi:", mean_last_20)
print("   Do lech chuan cua 20 gia tri cuoi:", std_last_20)

first_10_values = d_values[:10]
last_40_values = d_values[-40:]

mean_first_10 = np.mean(first_10_values)
std_first_10 = np.std(first_10_values)

mean_last_40 = np.mean(last_40_values)
std_last_40 = np.std(last_40_values)

print("e) Gia tri trung binh cua 10 gia tri dau:", mean_first_10)
print("   Do lech chuan cua 10 gia tri dau:", std_first_10)
print("   Gia tri trung binh cua 40 gia tri cuoi:", mean_last_40)
print("   Do lech chuan cua 40 gia tri cuoi:", std_last_40)

min_value = np.min(d_values)
max_value = np.max(d_values)

print("f) So nho nhat:", min_value)
print("   Lon nhat:", max_value)

import numpy as np
from scipy.stats import describe, shapiro

# Sử dụng describe để có cái nhìn tổng quan về phân phối
desc_stats = describe(d_values)
print("describe:")
print(desc_stats)

# Kiểm tra phân phối của sai số thô sử dụng kiểm định Shapiro-Wilk
shapiro_test_statistic, shapiro_p_value = shapiro(d_values)
print("Shapiro-Wilk:")
print("Statistic:", shapiro_test_statistic)
print("p-value:", shapiro_p_value)

# Vẽ đồ thị hàm mật độ phân phối
plt.figure(figsize=(10, 6))
sns.histplot(d_values, kde=True, color='blue', bins=20)
plt.title('Ham mat do phan phoi d')
plt.xlabel('d (gia tri duong kinh)')
plt.ylabel('f(d)')
plt.show()

