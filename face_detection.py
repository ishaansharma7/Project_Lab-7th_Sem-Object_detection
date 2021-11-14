import cv2
from mystack import stackImages
from dialogbox import loc_browser
 
faceCascade= cv2.CascadeClassifier("resources/haarcascades/haarcascade_frontalface_alt2.xml")

location = loc_browser()

img = cv2.imread(location)
# cv2.imshow("Result", img)

rect_width = 2
myscale = 1
ratio = 1
if img.shape[0] > 1000:
    rect_width = 8
    myscale = 3
    ratio = .3
elif img.shape[1] > 2000:
    rect_width = 8
    myscale = 3
    ratio = .3


imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 
faces = faceCascade.detectMultiScale(imgGray,1.1,4)
face_count = 0

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),rect_width)
    face_count += 1

#                                                         position x,y                 font-style             scale       color         thickness
cv2.putText(img, f'F:{face_count}', (int(img.shape[1]/25), int(img.shape[1]/25)), cv2.FONT_HERSHEY_TRIPLEX,  myscale,   (0,255,255),   rect_width)

img_stack = stackImages(ratio, ([img]))
cv2.imshow('stacked images', img_stack)
cv2.waitKey(0)