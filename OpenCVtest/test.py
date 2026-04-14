import cv2
import os

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
# Build the path to the image file
image_path = os.path.join(script_dir, "Resources", "IMG_3269.JPG")

mine = cv2.imread(image_path)
mine = cv2.resize(mine, (600, 500))

cv2.imshow("Jovi", mine)
cv2.waitKey(0)
