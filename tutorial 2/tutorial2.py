import cv2
import random

img = cv2.imread('assets/logo.jpg', -1)

'''
img.shape -> (height, width, #ofValues that represent each pixel)

pixels in opencv are represented as blue,green,red
'''

'''
for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        
'''

'''
Copy and Pasting one part of the image to another
img[slice_of_leftboundrows:rightboundrows, slice_of_leftboundcols:rightboundcols]
'''
tag = img[500:700, 600:900]
img[100:300, 650:950] = tag


cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

