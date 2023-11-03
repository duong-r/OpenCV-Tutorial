import numpy as np
import cv2

img = cv2.imread('assets/soccer_practice.jpg', 0)
template = cv2.imread('assets/shoe.PNG', 0)
h, w = template.shape

'''
6 main methods of doing template matching. Whats recommended is to try all 6 methods first, 
then continue using the one that gives you the best result 
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
            
cv2.matchTemplate(BaseImage, Template, Method): performs a convolution, 
where the template image is slid across all parts of the base
and seeing how much of a match there is in each region of the base.

dimensions of this result will be of size
(W - w + 1, H - h + 1)
W : width of base image
w : width of template

if base image was
[[255, 255, 255, 255],
 [255, 255, 255, 255],
 [255, 255, 255, 255],
 [255, 255, 255, 255]]

and template image was
[[255, 255],
 [255, 255]]

result would be
[[1, 1, 1],
 [1, 1, 1],
 [1, 1, 1]]
 
 
 Say there was a result that looked like
 [[0, 0, 0],
  [0, 1, 0],
  [0, 0, 0]]
We would want to find the area that's responsible for the 1, as that is the area where our template matches the base.
What we can do is use some math to determine what coordinates correspond to that area of the image, then draw a rectandle around it.

min_val, max_val, min_loc, max_loc = minMaxLoc(result_array)
returns the min and max value in the array, and min and max location of the array.

NOTE: If we use [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED] methods, we want to take the min.
      Otherwise, we take the max

'''

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()
    
    result = cv2.matchTemplate(img, template, method)
    
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc
    bottom_right = (location[0] + w, location[1] + h)
    
    img2 = cv2.rectangle(img2, location, bottom_right, 255, 5)
    cv2.imshow('Match', img2)
    cv2.waitKey()
    cv2.destroyAllWindows()