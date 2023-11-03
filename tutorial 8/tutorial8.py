import numpy as np
import cv2

'''
haarcascades = pre-trained classifiers that detect the presence of distinct features in an image.
    each cascade is responsible for a certain type of feature face, eyes, nose, nails, hands etc.
    
Steps:
1. load in the cascade we want
XXXX_cascade = = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_XXXX_default.xml')

2. turn our image into a grayscale
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

3. use the cascade to determine the positons of the detectable instances of the feature-of-interest
XXXXs = XXXX_cascade.detectMultiScale(image, scaleFactor, minNeighbors, minSize, maxSize)
scaleFactor:
    NOTE: we may not know the size of our image, and therefore the size of the features. So, it's
      possible that the cascade was not trained on features of a particular size (maybe too big/small)
      for example, if we pass in an image of size 10k x 10k, our features would likely be much larger than
      what the cascade was expecting. So, the `scaleFactor` is the scale by how much we resize an image until
      we reach the size expected by the cascade. 1.05 is a good possible value.
      lower scaleFactor = higher accuracy, lower performance
minNeighbors: how many neighbors each candidate should have to retain it.
      higher minNeighbors = higher quality, lower performance. 3-6 is good
minSize: Minimum possible object size object smaller than this are ignored [30, 30]
maxSize: Maximum possible object size object larger than this are ignored



'''
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eyes_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
while True:
    ret, frame = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        
        eyes = eyes_cascade.detectMultiScale(roi_gray, 1.3, 5)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()