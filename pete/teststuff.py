import numpy as np
import cv2 as cv
from PIL import Image,ImageGrab
from mss import mss
import time
import lane_detection
import keyboard_control
# from keyboard_control import Direction,input

width = 640
height = 480
displayWidth = 1280
mon = {'top': 50, 'left': 0, 'width': width, 'height': height}
sct = mss()
# cv.namedWindow('test', flags=cv.WINDOW_NORMAL | cv.WINDOW_GUI_NORMAL | cv.WINDOW_FULLSCREEN)
cv.namedWindow('test1', flags=cv.WINDOW_NORMAL | cv.WINDOW_GUI_NORMAL | cv.WINDOW_FULLSCREEN)
cv.namedWindow('test2', flags=cv.WINDOW_NORMAL | cv.WINDOW_GUI_NORMAL | cv.WINDOW_FULLSCREEN)
cv.namedWindow('test3', flags=cv.WINDOW_NORMAL | cv.WINDOW_GUI_NORMAL | cv.WINDOW_FULLSCREEN)
# cv.moveWindow('test',650,0)
cv.moveWindow('test1',650,0)
cv.moveWindow('test2',0,490)
cv.moveWindow('test3',650,490)
counter = 1
while 1:
    old_time = time.time()
    counter = counter + 1
    cap = sct.grab(mon)
    img = Image.frombytes('RGB', (cap.width, cap.height), cap.rgb)
    window = np.array(img.resize((int(img.width/2), int(img.height/2))))
    gameWindow = cv.cvtColor(window, cv.COLOR_BGR2RGB)
    # cv.imshow('test',gameWindow)
    # cv.imshow('test1', lane_detection.lane_detect(window,counter))
    cv.imshow('test1', lane_detection.lane_detect(window,counter)[0])
    cv.imshow('test2', lane_detection.lane_detect(window,counter)[1])
    cv.imshow('test3', lane_detection.lane_detect(window,counter)[2])

    if cv.waitKey(25) & 0xFF == ord('q'):
        cv.destroyAllWindows()
        break
    new_time = time.time()
    print(1/(new_time-old_time))
