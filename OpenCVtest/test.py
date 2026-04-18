import cv2
import os
# import time
# import uuid
# from deepface import DeepFace
# from matplotlib import pyplot as plt
import pathlib

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
cv2.waitKey(0) 

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
cv2.waitKey(0)  '''

# face detection with opencv
the_path = pathlib.Path(cv2.__file__).parent.absolute() / \
    "data/haarcascade_frontalface_default.xml"
clf = cv2.CascadeClassifier(str(the_path))
# for webcam especially with 1 camera, if more, change to 1,2,3 etc,
cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture("") # taking or capturing faces from a video

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = clf.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=3,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    for (x, y, width, height) in faces:
        cv2.rectangle(frame, (x, y), (x+width, y+height), (255, 255, 0), 2)

    cv2.imshow("Faces", frame)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
