import cv2
import numpy as np
import matplotlib

def canny(image):
  grey = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
  blur = cv2.GaussianBlur(grey, (5, 5), 0)
  canny = cv2.Canny(blur, 50, 150)
  return canny


image = cv2.imread('./images/test-1.jpg')

# My Images 

# image = cv2.imread('./images/test-4.jpg')
# image = cv2.imread('./images/test-6.jpg')

lane_image = np.copy(image)
canny = canny(lane_image)

cv2.imshow('result', canny)
cv2.waitKey(0)
