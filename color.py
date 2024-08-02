import cv2
import numpy as np

# Màu sắc cần nhận diện (ở đây là màu đỏ)
lower_red = np.array([0, 0, 100])
upper_red = np.array([100, 100, 255])

# Khởi tạo Camera
cap = cv2.VideoCapture(0)

while True:
    # Đọc frame từ Camera
    ret, frame = cap.read()

    # Chuyển đổi từ BGR sang HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Tạo mặt nạ (mask) để nhận diện màu sắc
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Tìm tất cả các pixel có giá trị khác không trên mặt nạ
    non_zero_points = cv2.findNonZero(mask)

    # Hiển thị toạ độ của pixel màu
    if non_zero_points is not None:
        for point in non_zero_points:
            x, y = point[0]
            print(f"Pixel color at coordinate ({x}, {y})")

    # Hiển thị kết quả
    cv2.imshow('Original', frame)
    cv2.imshow('Red Color Detection', mask)

    # Thoát khỏi vòng lặp khi bấm phím 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng tài nguyên
cap.release()
cv2.destroyAllWindows()
