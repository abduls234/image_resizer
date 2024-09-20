import time
import cv2

source="me 2.jpg"
destination= "resize50.jpg"
scale_percent = 50

src= cv2.imread(str(source))

#cv2.imshow('image',src)
cv2.waitKey(0)

# Percent by which the image is resized

# Calculate the 50 percent of original dimensions
width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)


# Resize image
output = cv2.resize(src, (width, height))

cv2.imwrite(destination, output)