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
    image = np.zeros(frame.shape, np.uint8)
    width = int(cap.get(3))
    height = int(cap.get(4))
    
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[height//2:, :width//2] = smaller_frame
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[height//2:, width//2:] = smaller_frame
    
    cv2.imshow('frame', image)
    
    #waits 1ms for us to type a key in case we want to break
    #if we dont press a key in that time, we will move on
    #ord is the ascii number value thats associated with a particular key
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
    