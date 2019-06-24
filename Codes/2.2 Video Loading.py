import cv2

camera=cv2.VideoCapture('Samples 1/sample_video.MP4')

#0-default camera(webcam)
#usb cameras 1,2
#ip address of a camera
#path to a video file

while(True):

    ret,frame=camera.read()

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('LIVE',frame)
    cv2.imshow('GRAY',gray)
    
    cv2.waitKey(1)  #1ms delay
