import cv2
import numpy as np

img = cv2.imread('room.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img,(480,576))

sigma = 1.4  
blurred = cv2.GaussianBlur(img, (5,5), sigma)
laplacian = cv2.Laplacian(blurred, cv2.CV_64F)

laplacian_abs = np.uint8(np.absolute(laplacian))

_, edges = cv2.threshold(laplacian_abs, 30, 255, cv2.THRESH_BINARY)

cv2.imshow('Marr-Hildreth Edge Detection', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
