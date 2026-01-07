import cv2
import numpy as np

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

myColors =  [[10, 25, 100, 255, 100, 255],   # Orange
             [35, 85, 50, 255, 50, 255],     # Green
             [100, 130, 150, 255, 50, 255],  # Blue
             [0, 179, 0, 30, 200, 255],      # White
             [20, 30, 100, 255, 100, 255],   # Yellow
             [35, 85, 50, 255, 50, 255]]     # Green




def findColour(img, myColors):
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    lower = np.array(myColors[0][0:3])
    upper = np.array(myColors[0][3:6])
    mask = cv2.inRange(imgHsv, lower, upper)
    cv2.imshow("Img", mask)

while True:
    success, img = cap.read()
    if not success:
        break
    findColour(img, myColors)  
    cv2.imshow("Result", img)  #
    if cv2.waitKey(1) & 0xFF == ord("s"):
        break

cap.release()
cv2.destroyAllWindows()
