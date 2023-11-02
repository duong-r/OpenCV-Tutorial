import numpy as np
import cv2 


'''
Acronym Breakdown:
• RGB - Red, Green, Blue
• BGR - Blue, Green, Red
• HSV - Hue, Saturation, Value

Hue        - the dominant color family 
           - Primary & Secondary Colors
Saturation - level of intensity of a color 
           - high saturation is bright colors. 
           - low saturation is muted colors.
Value -    - also called lightness : how light or dark a color is 
'''
'''
BGR_color = np.array([[[255, 0, 0]]])
x = cv2.cvtColor(BGR_color, cv2.COLOR_BGR2HSV)
x[0][0]
'''
cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])
    
    '''
    mask is a portion of the image or 
    portion of the frame
    
    any pixels with colors in the 
    range of the mask will be displayed.
    all others will be blacked out
    '''
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('frame', result)
    
    
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cap.destroyAllWindows()
