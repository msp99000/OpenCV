# Manipulating Pixels using OpenCV


# Importing OpenCV library
import cv2
import random

# Using a screenshot of my secondary desktop as an example here
img = cv2.imread("/home/mikee/Documents/Sublime Text 3/OpenCV/2. Image Pixel Manipulation/MyDesktop.png")

# Change first 100 rows to random pixels
for i in range(100):
	for j in range(img.shape[1]):
		img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

# Copy part of image
tag = img[500:700, 600:900]
img[100:300, 650:950] = tag

# Resize the image to half-length and half-width
img = cv2.resize(img, (0,0), fx = 0.5, fy = 0.5)

# Show the image
cv2.imshow('My Desktop', img)

# Wait infinte time
cv2.waitKey(0)
cv2.destroyAllWindows()