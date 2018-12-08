import numpy as np
import cv2 as cv
from mss import mss
from PIL import Image
from window import selectWindow

ROI = selectWindow()

fullWinProperties = (cv.WINDOW_NORMAL | cv.WINDOW_GUI_NORMAL | cv.WINDOW_FULLSCREEN)
autopilot = False

x0 = ROI[0]
y0 = ROI[1]
width = ROI[2]
height = ROI[3]
x1 = ROI[0]+ROI[2]
y1 = ROI[1]+ROI[3]

sct = mss()
dims = {'top':y0,'left':x0,'width':width,'height':height}

cv.namedWindow('GamePlay')
cv.moveWindow('GamePlay',y1+1,x0)

# Colors for visualizing optical flow
colors = [  (255,0,0),(255,127,0),(255,255,0),
            (127,255,0),(0,255,0),(0,255,127),
            (0,255,255),(0,127,255),(0,0,255),
            (127,0,255),(255,0,255),(255,0,127) ]

while(1):
    cap = sct.grab(dims)
    gameDisplay = np.array(Image.frombytes('RGB',(cap.width, cap.height), cap.rgb))

    cv.imshow('GamePlay', cv.cvtColor(gameDisplay, cv.COLOR_BGR2RGB))
    
    # get input for quitting, running autopilot, etc
    key = cv.waitKey(1)
    if key == ord('q'):
        break
    if key == ord('d'):
        autopilot = not autopilot
        # TODO: Call autopilot function here


cv.destroyAllWindows()
