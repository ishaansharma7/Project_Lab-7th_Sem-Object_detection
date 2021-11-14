import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 640) # frame width
cap.set(4, 480) # frame height
cap.set(10, 150) # brightness


mycolors = [
        [5,117,0,19,255,255], # orange
        [57,76,0,80,255,255], # green
        # [133,56,0,159,156,255], # purple
            ]

colorvalues = [
        [51,153,255],
                [0,255,0]
]

def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>500:
            # cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2,y

def drawOnCanvas(myPoints,myColorValues):
    for point in myPoints:
        cv2.circle(imgResult,(point[0],point[1]),10,myColorValues[point[2]],cv2.FILLED)

def findColor(img, mycolors, colorvalues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for color in mycolors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)
        cv2.circle(imgResult,(x,y),10,colorvalues[count],cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count += 1
        # cv2.imshow(str(color[0]), mask)
    return newPoints

myPoints = []

while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img, mycolors, colorvalues)
    if len(newPoints) != 0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints) != 0:
        drawOnCanvas(myPoints, colorvalues)
    cv2.imshow('video', imgResult)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break