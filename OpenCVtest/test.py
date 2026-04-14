import cv2
import os

'''
# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
# Build the path to the image file
image_path = os.path.join(script_dir, "Resources", "IMG_3269.JPG")

mine = cv2.imread(image_path)
mine = cv2.resize(mine, (600, 500))

cv2.imshow("Jovi", mine)
cv2.waitKey(0) '''

frameWidth = 360
frameHeight = 640


cap = cv2.VideoCapture("OpenCVtest\Resources\IMG_5789.MOV")  # (0) for webcam
cap.set(3, frameWidth)  # 3 for default width
cap.set(4, frameHeight)  # 4 for a default height


# video to keep playing

while True:
    success, img = cap.read()
    cv2.imshow("video", img)
    img = cv2.resize(img, (frameWidth, frameHeight))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
