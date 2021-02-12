# Reading & Applying Basic Image Operations using OpenCV library


# Importing OpenCV library
import cv2

# Using a screenshot of my secondary desktop as an example here
img = cv2.imread("Screenshot.png")

# Resize Image to half-length and half-width
img = cv2.resize(img, (0,0), fx = 0.5, fy = 0.5)

# Use 'imshow' to display Image, the 1st parameter is the window name, 2nd is variable itself
cv2.imshow('MyScreenshot', img)

# Use waitKey(0) for infinite time
cv2.waitKey(0)

# Remember to close all windows
cv2.destroyAllWindows()


