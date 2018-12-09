import numpy as np
import cv2 as cv
from mss import mss
from PIL import Image
from window import selectWindow

# Jacob's Functions
from lane_detection import lane_detect

ROI = (0,0,0,0)
PAD = 45    # Default Paddimg (unchanged Above)

# simple check if selection is valid:
while ROI == (0,0,0,0):
    ROI = selectWindow()

# Needed Variables
fullWinProperties = (cv.WINDOW_NORMAL | cv.WINDOW_GUI_NORMAL | cv.WINDOW_FULLSCREEN)
autopilot = False

# ROI Window variables
x0 = ROI[0]
y0 = ROI[1]
width = ROI[2]
height = ROI[3]

sct = mss()
dims = {'top':y0+PAD,'left':x0,'width':width,'height':height}

cv.namedWindow('GamePlay')
cv.moveWindow('GamePlay',x0,y0+height+PAD)

# Edge detection windows
cv.namedWindow('Edge')
cv.moveWindow('Edge',x0-width,y0+height+PAD)

# Colors for visualizing optical flow
colors = [  (255,0,0),(255,127,0),(255,255,0),
            (127,255,0),(0,255,0),(0,255,127),
            (0,255,255),(0,127,255),(0,0,255),
            (127,0,255),(255,0,255),(255,0,127) ]

while(1):
    cap = sct.grab(dims)
    gameCap = np.array(Image.frombytes('RGB',(cap.width, cap.height), cap.rgb))

    cv.imshow('GamePlay', cv.cvtColor(gameCap, cv.COLOR_BGR2RGB))

    cv.imshow('Edge', lane_detect(gameCap))
    
    # get input for quitting, running autopilot, etc
    key = cv.waitKey(1)
    if key == ord('q'):
        break
    if key == ord('d'):
        autopilot = not autopilot
        # TODO: Call autopilot function here


cv.destroyAllWindows()
