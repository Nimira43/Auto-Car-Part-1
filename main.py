import cv2
import numpy as np

# image = cv2.imread('./images/test-1.jpg')

# My Images 
# image = cv2.imread('./images/test-2.jpg')
# image = cv2.imread('./images/test-3.jpg')
# image = cv2.imread('./images/test-4.jpg')
# image = cv2.imread('./images/test-5.jpg')
image = cv2.imread('./images/test-6.jpg')

lane_image = np.copy(image)
grey = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)
blur = cv2.GaussianBlur(grey, (5, 5), 0)

cv2.imshow('result', blur)
cv2.waitKey(0)
