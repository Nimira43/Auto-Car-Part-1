import cv2

image = cv2.imread('./images/test-1.jpg')

# My Images 

# image = cv2.imread('./images/test-2.jpg')
# image = cv2.imread('./images/test-3.jpg')
# image = cv2.imread('./images/test-4.jpg')
# image = cv2.imread('./images/test-5.jpg')
# image = cv2.imread('./images/test-6.jpg')



cv2.imshow('result', image)
cv2.waitKey(0)

# Notes -
# test-1 image is provide by instructor, the rest by me
# test-4 and test-6 image look useful to look at further
# not sure about test-5, test-3, test-2 images - vehicles in image