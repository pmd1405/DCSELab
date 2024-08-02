import cv2
import numpy as np

def find_red_coordinates(frame):
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
        cv2.circle(frame, (cX, cY), 1, (0, 0, 255), -1)

    # Vẽ đường nối các điểm trọng tâm
    if len(red_coordinates) >= 2:
        for i in range(len(red_coordinates) - 1):
            cv2.line(frame, red_coordinates[0], red_coordinates[i + 1], (255, 0, 0), 1)

    # Tính và hiển thị góc giữa các điểm trọng tâm
    for i in range(len(red_coordinates) - 2):
        pt2, pt1, pt3 = np.array(red_coordinates[i:i+3])

        vector1 = pt1 - pt2
        vector2 = pt3 - pt2

        cosine_sim = np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))
        angle_rad = np.arccos(np.clip(cosine_sim, -1.0, 1.0))
        angle_deg = np.degrees(angle_rad)

        print("Angle {}: {:.2f} Degree".format(i + 1, angle_deg))

    return red_coordinates

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    coordinates = find_red_coordinates(frame)
    cv2.imshow('Red Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
