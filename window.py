import numpy as np
import cv2 as cv
from PIL import Image
from mss import mss

def selectWindow(MAX_WIDTH=2560,MAX_HEIGHT=1440,PAD=45):
    # GLOBAL VARIABLES, SYSTEM DEPENDENT:
    # PAD = 45
    # MAX_WIDTH = 2560
    # MAX_HEIGHT = 1440

    # init screen cap:
    sct = mss()
    dims = {'top':PAD,'left':0,'width':MAX_WIDTH,'height':MAX_HEIGHT}

    # capture screen
    cap = sct.grab(dims)
    img = Image.frombytes('RGB', (cap.width, cap.height), cap.rgb)

    # display the full screen
    properties = (cv.WINDOW_NORMAL | cv.WINDOW_GUI_NORMAL | cv.WINDOW_FULLSCREEN )

    cv.namedWindow('ROI',properties)
    cv.moveWindow('ROI',0,0)
    cv.imshow('ROI', cv.cvtColor(np.array(img), cv.COLOR_BGR2RGB))

    ROI = cv.selectROI('ROI', np.array(img),True) 

    cv.destroyWindow('ROI')
    return ROI
