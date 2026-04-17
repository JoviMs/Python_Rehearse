import cv2
import os

'''
#for images

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
# Build the path to the image file
image_path = os.path.join(script_dir, "Resources", "IMG_3269.JPG")

mine = cv2.imread(image_path)
mine = cv2.resize(mine, (600, 500))

cv2.imshow("Jovi", mine)
cv2.waitKey(0)

#for videos
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

#Basic function (know different way to show the colour of an image)
kernel = np.ones((5, 5), np.uint8)
# print(kernel)

# Basic function (know different way to show the colour of an image)
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "Resources", "IMG_3269.JPG")

mine = cv2.imread(image_path)  # include 0 to be shown as gray colour
mine = cv2.resize(mine, (600, 500))
# showing the gray colour of the pic
gray = cv2.cvtColor(mine, cv2.COLOR_BGR2GRAY)
bluring = cv2.GaussianBlur(gray, (7, 7), 0)
canny = cv2.Canny(bluring, 100, 100)
dilation = cv2.dilate(canny, kernel, iterations=1)

cv2.imshow("Laala", gray)
cv2.imshow("Cann",  canny)
cv2.imshow("Blur", bluring)
cv2.imshow("mine", mine)
cv2.imshow("lola", dilation)
cv2.waitKey(0) '''

# Cropping and Resizing images
script_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(script_dir, "Resources", "Road_in_Norway.jpg")

img = cv2.imread(path)
# print(img.shape) ---Gives you the shape of your image (height,width,number of channel bgr)
img = cv2.resize(img, (600, 500))
# corpping in a car shape view, viewing at lanes (height, width)
imgCrop = img[300:440, 210:470]  # staying on lane


cv2.imshow('Road', img)
cv2.imshow('Roadcrop', imgCrop)
cv2.waitKey(0)
