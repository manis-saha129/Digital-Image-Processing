import cv2
import numpy as np

img = cv2.imread('room.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img,(480,576))
sigma = 1.4  
blurred = cv2.GaussianBlur(img, (5,5), sigma)

lower_threshold = 50 
upper_threshold = 150
edges = cv2.Canny(blurred, lower_threshold, upper_threshold)

cv2.imshow('Canny Edge Detection', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
