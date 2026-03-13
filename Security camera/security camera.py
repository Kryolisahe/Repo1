import cv2
import time

cap=cv2.VideoCapture(0)

width=int(cap.get(3))
height=int(cap.get(4))

#cv2.VideoWriter(<output_video>,<codec>,<fps>,(frame_width,frame_height))

out=cv2.VideoWriter("_video.avi",cv2.VideoWriter_fourcc('M','J','P','J'),10,(width,height))

faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#optional
font=cv2.FONT_HERSHEY_SIMPLEX

#check if camers opened successfully
if(cap.isOpened()==False):
    print("Unable to read camera feed")

oldtime=0
while(True):
    ret,frame=cap.read()

    if ret==True:

        imgGray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #cascade.detectMultiScale(image_type,scale factor,minNeighbours)
        faces=faceCascade.detectMultiScale(imgGray,1.1,4)

        timeNow=time.acstime(time.localtime(time.time()))

        #putting text
        cv2.putText(frame,timeNoe,(10,450),font,98,(0,255,0),2,cv2.Line_AA)

        for(x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

            if time.time()-oldtime>30:
                cv2.imwrite(str(time.time())+"_face.jpg",frame)
                oldtime=time.time()

            #write the frame into the video
            out.write(frame)

            #display the resulting frame
            cv2.imshow("Video Footage",frame)

            #press Q on keyboard to stop recording
            if cv2.waitKey(25)==ord('q'):
                break

cap.release()
out.release()

#close all frames
cv2.destroyAllWindows()
 
 
            
