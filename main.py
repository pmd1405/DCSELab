import cv2
import pandas as pd

cap = cv2.VideoCapture(0)

cap.set(3, 720)
cap.set(4, 1280)

b, g, r = 0, 0, 0

def draw_square(img, x, y):
    YELLOW = (0, 255, 255)
    BLUE = (255, 225, 0)

    points = [
        (x - 150, y - 150), (x - 100, y - 150),
        (x - 150, y - 150), (x - 150, y - 100),
        (x + 150, y - 150), (x + 100, y - 150),
        (x + 150, y - 150), (x + 150, y - 100),
        (x + 150, y + 150), (x + 100, y + 150),
        (x + 150, y + 150), (x + 150, y + 100),
        (x - 150, y + 150), (x - 100, y + 150),
        (x - 150, y + 150), (x - 150, y + 100)
    ]

    for i in range(0, len(points), 2):
        cv2.line(img, points[i], points[i + 1], YELLOW, 2)
    
    cv2.circle(img, (x, y), 5, (255, 255, 153), -1)

# Reading the csv file with pandas and giving names to each column
index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv("colors.csv", names=index, header=None)

# Function to get BGR values from the camera
def get_bgr(x, y):
    global b, g, r
    b, g, r = img[y, x]
    b, g, r = int(b), int(g), int(r)
    return b, g, r

# Function to calculate the minimum distance from all colors and return the most matching color
def get_color_name(b, g, r):
    minimum = 1000 
    for i in range(len(csv)):
        d = abs(b - int(csv.loc[i, "B"])) + abs(g - int(csv.loc[i, "G"])) + abs(r - int(csv.loc[i, "R"]))
        if d <= minimum:
            minimum = d
            cname = csv.loc[i, "color_name"]
    return cname

# Put text on the image
def put_text(img, x, y):
    cv2.rectangle(img, (x - 150, y - 220), (x + 300, y - 170), (b,g,r), -1)
    text = get_color_name(b, g, r) + f" | R={r} G={g} B={b}"
    cv2.putText(img, text, (x - 140, y - 190), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 255, 255), 2)

while True:
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    x, y = int(img.shape[1] / 2), int(img.shape[0] / 2)
    
    get_bgr(x, y)
    get_color_name(b, g, r)
    
    draw_square(img, x, y)
    put_text(img, x, y)
    
    cv2.imshow('Color Detector', img)
    
    key = cv2.waitKey(1)
    if key == 27:  # 27 is the ASCII code for the ESC key
        break

cap.release()
cv2.destroyAllWindows()
