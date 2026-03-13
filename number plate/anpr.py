import cv2
import pytesseract

nPlateCascade=cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
minArea=10
count=0
numbers=[]

GREEN=(0,255,0)
BLUE=(0,0,255)

cap=cv2.VideoCapture("video.mp4")
success,img=cap.read()
while success:
    numberPlates=[]
    img=cv2.resize(img,(640,480))
    imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    numberPlates=nPlateCascade.detectMultiScale(imgGray,1.1,10)
    for(x,y,w,h)in numberPlates:
        area=w*h
        if area>minArea:
            cv2.rectangle(img,(x,y),(x+w,y+h),GREEN,2)
            cv2.putText(img,"Number Plate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,BLUE,2)
            imgRoi=img[y:y+h,x:x+w]
            number=pytesseract.image_to_string(imgRoi,lang="eng")
            if number not in numbers:
                numbers.append(number)
                cv2.imshow("ROI",imgRoi)
                cv2.imwrite("NoPlate_"+str(count)+"jpg",imgRoi)

    cv2.imshow('Result',img)

    if cv2.WaitKey(1)==ord("s"):
        cv2.imwrite("Still_"+str(count)+"jpg"+img)
        cv2.rectangle(img,(0,200),(640,300),GREEN,cv2.FILLED)
        cv2.putText(img,"Scan Saved",(150,265),cv2.FONT_HERSHEY_DUPLEX,2,BLUE,2)
        cv2.imshow("Result",img)
        cv2.waitKey(500)
        count+=1
    elif cv2.WaitKey(1)==ord("q"):
        break
    success,img=cap.read()

cv2.destruAllWindows()
cap.release()
