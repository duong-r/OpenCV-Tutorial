import cv2

'''
-1, cv2.IMREAD_COLOR : Loads a color image. Any transparency will be neglecte. It is the default flag
0, cv2.IMREAD_GREYSCALE : Loads image in greyscale mode
1, cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel
'''
img = cv2.imread('assets/logo.jpg', -1)
cv2.imshow('Image', img)

'''
How to Resize Image
cv2.resize(image, (height, width))
cv2.resize(image, (0, 0), fx= desired_scale_for_x, desired_scale_for_y)
'''
img2 = cv2.resize(img, (400, 400)) 

'''
How to Rotate Image
cv2.rotate(image, cv2.ROTATE*)
'''
img3 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE) 

'''
How to write an Image
cv2.imwrite('new_img.jpg', image)
'''
cv2.imwrite('assets/new_img.jpg', img3)

cv2.waitKey(0)
cv2.destroyAllWindows()

