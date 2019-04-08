import cv2

face_cascade=cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

cap=cv2.VideoCapture(0)##create a videocapture object with path to the webcam(usually its 0,-1,2),can be changed to videopath if required 
#but make sure to have the video in the current working directory

count=0
print("Pess on ESC to close,make sure to select the video-feed")
while True:
    (ret,img)=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#convert image or frame to graycale
    faces=face_cascade.detectMultiScale(gray,1.2,10)#the function returns list of tuples (left,down,right,top) corresponding to each face in an image i.e img
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(120,255,0),2)#draw rectangular bounding box
        cropped=img[y:y+h,x:x+w]#(optional)
        cv2.imshow('cropped',cropped)#(optional)
        count=count+1#(optional)
        cv2.imwrite('cropped/'+str(count)+'.jpg',cropped) #save the detected faces int the directory named cropped(optional)

    cv2.imshow('img',img)
    k=cv2.waitKey(30) & 0xff
    if k==27:
        break

cap.release()
cv2.destroyAllWindows()
