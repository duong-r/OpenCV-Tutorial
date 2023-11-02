import numpy as np
import cv2

'''
Talking about cameras and how to use 
cameras/our webcam
'''

'''
IF YOU HAVE MULTIPLE CAMS, 
THE NUMBER REPRESENTS WHICH SPECIFIC CAM
cv2.VideoCapture(#Cam)
'''
cap = cv2.VideoCapture(0)

'''
While true, 
we will read from our camera (read an image)
frame is the image itself (numpy array that reps the img)
ret tells you if the capture worked properly
'''
while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    
    '''
    Drawing Lines 
    --  Source Image, 
        the starting coord, (w,h) 
        the ending coord,   (w,h)
        Color of line,
        Thickness of line
    '''
    img = cv2.line(frame, (0, 0), (width, height), (0, 255, 255), 10)
    img = cv2.line(img, (width, 0), (0, height), (125, 0, 255), 10)
    
    '''
    Drawing Rectangles 
    --  Source Image, 
        the starting coord : top left of the rect, (w,h) 
        the ending coord : bottom right of the rect(w,h)
        Color of line,
        Thickness of line or the Fill
    '''
    
    # Rectangle with boarders of 19px thickness
    img = cv2.rectangle(img, (100, 100), (400, 400), (125, 177, 255), 19)
    
    # Filled in Rectangle : -1
    img = cv2.rectangle(img, (100, 100), (400, 400), (125, 177, 255), -1)

    '''
    Drawing Rectangles 
    --  Source Image, 
        coord of center of circle : (w,h) 
        radius length : #px
        Color of circle : (b,g,r)
        Thickness of line or the Fill : -1 for fill
    '''
    img = cv2.circle(img, (300, 300), 60, (0, 0, 255), -1)
    
    '''
    First create font:
    font = cv2.CHOOSE_YOUR_FONT : cv2.FONT_HERSHEY_SIMPLEX
    Drawing Text:
    -- Source Image,
        Text : 'String'
        Bottomleft hand corner : (w,h)
        Font
        scale of the text
        color
        thickness of lines
        line_type -- optional valie -- recommended cv2.LINE_AA
    '''
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, 'Ryan is cool', (200, height - 40), font, 4, (123,123,123), 5, cv2.LINE_AA)
    cv2.imshow('frame', img)

    
    #waits 1ms for us to type a key in case we want to break
    #if we dont press a key in that time, we will move on
    #ord is the ascii number value thats associated with a particular key
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
    