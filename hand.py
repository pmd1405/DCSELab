import cv2
import mediapipe as mp

# Khởi tạo Camera
cap = cv2.VideoCapture(0)

# Khởi tạo đối tượng Mediapipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

while True:
    # Đọc frame từ camera
    ret, frame = cap.read()

    # Chuyển đổi sang ảnh đen trắng
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Nhận diện cử chỉ vân tay
    results = hands.process(gray)

    # Kiểm tra và vẽ landmarks nếu có
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for lm in hand_landmarks.landmark:
                h, w, _ = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                cv2.circle(frame, (cx, cy), 5, (255, 0, 0), -1)

    # Hiển thị frame
    cv2.imshow('Hand Gestures Recognition', frame)

    # Thoát khỏi vòng lặp khi nhấn 'ESC'
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Giải phóng tài nguyên
cap.release()
cv2.destroyAllWindows()
