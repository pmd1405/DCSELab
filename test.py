import cv2
import numpy as np

def find_red_coordinates(frame, tracker, old_red_coordinates):
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Chuyển đối tất cả các pixel không phải là màu đỏ thành màu trắng
    mask = cv2.inRange(hsv_frame, np.array([0, 100, 100]), np.array([255, 255, 255]))
    hsv_frame[np.where(mask == 0)] = [0, 0, 255]

    # Tìm contours trên mặt phẳng XY
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Lọc contours dựa trên diện tích để giảm nhiễu
    filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 10]

    # Sắp xếp contours theo diện tích giảm dần
    filtered_contours.sort(key=cv2.contourArea, reverse=True)

    # Lấy tọa độ của ba điểm có diện tích lớn nhất
    red_coordinates = []
    for contour in filtered_contours[:3]:
        x, y, w, h = cv2.boundingRect(contour)
        cX = x + w // 2
        cY = y + h // 2
        red_coordinates.append((cX, cY))

    # Cập nhật tracker với tọa độ mới của đối tượng
    if len(red_coordinates) >= 3:
        success = tracker.init(frame, tuple(red_coordinates[0] + red_coordinates[1] + red_coordinates[2]))

    # Theo dõi đối tượng bằng thuật toán KCF
    success, boxes = tracker.update(frame)
    if success:
        # Vẽ bounding box của đối tượng theo dõi
        for box in boxes:
            x, y, w, h = [int(v) for v in box]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Hiển thị frame
    cv2.imshow('Red Detection', frame)

    return red_coordinates

# Tạo object tracker
tracker = cv2.TrackerKCF_create()

# Mở camera
cap = cv2.VideoCapture(0)

# Đọc frame từ camera
ret, frame = cap.read()

# Chọn ROI để theo dõi
roi = cv2.selectROI(frame, False)
tracker.init(frame, roi)

while True:
    # Đọc frame từ camera
    ret, frame = cap.read()

    # Theo dõi đối tượng và tìm điểm đỏ
    coordinates = find_red_coordinates(frame, tracker, None)

    # Thoát khi nhấn phím 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng camera và đóng cửa sổ
cap.release()
cv2.destroyAllWindows()
