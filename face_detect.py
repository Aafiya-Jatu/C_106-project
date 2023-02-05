import cv2
image = cv2.imread('boy.jpg')
greyImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#loadclassifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face = face_cascade.detectMultiScale(greyImage)
for x,y,w,h in face:
       cv2.rectangle(image,(x,y),(x+w,y+h),(225,0,0),2)
       #crop the image to save the face image
       roi = image[y:y+h, x:x+w]
       cv2.imwrite('boyimage.jpg', roi)
cv2.imshow('image',image)
cv2.waitKey(0)