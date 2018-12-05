import numpy as np
import cv2 as cv

cap = cv.VideoCapture('TX-Racing.mp4')

while(cap.isOpened()):
    ret,frame = cap.read()

    # check end of file:
    if ret:
        edges = cv.Canny(frame,100,200)
        edgeWin = cv.imshow('Edges.mp4',edges)
        origWin = cv.imshow('Risto.mp4',frame)

    # check for 'q'
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# release video file, destroy window
cap.release()
cv.destroyAllWindows()
