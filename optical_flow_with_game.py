import numpy as np
import cv2 as cv
from PIL import Image,ImageGrab
from mss import mss
import time
from copy import deepcopy

mon = {'top': 50, 'left': 0, 'width': 1280, 'height': 312}
sct = mss()
cv.namedWindow('frame', flags=cv.WINDOW_NORMAL)
cv.moveWindow('frame',0,380)

# params for ShiTomasi corner detection:
feature_params = dict(  maxCorners = 100,
                        qualityLevel = 0.3,
                        minDistance = 7,
                        blockSize = 7 )

# parameters for lucas kanade optical flow:
lk_params = dict(   winSize = (15,15),
                    maxLevel = 2,
                    criteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT,
                                10,0.03) )

color = np.random.randint(0,255,(100,3))

cap = sct.grab(mon)
img = Image.frombytes('RGB', (cap.width, cap.height), cap.rgb).convert('L')
new_frame = np.array(img.resize((int(img.width/2), int(img.height/2))))
p0 = cv.goodFeaturesToTrack(new_frame, mask = None, **feature_params)
mask = np.zeros_like(new_frame)

while 1:
    old_frame = deepcopy(new_frame)
    cap = sct.grab(mon)
    img = Image.frombytes('RGB', (cap.width, cap.height), cap.rgb).convert('L')
    new_frame = np.array(img.resize((int(img.width/2), int(img.height/2))))
    p0 = cv.goodFeaturesToTrack(new_frame, mask = None, **feature_params)
    p1, st, err = cv.calcOpticalFlowPyrLK(old_frame, new_frame, p0, None,
                                           **lk_params)
    good_new = p1[st==1]
    good_old = p0[st==1]

    for i,(new,old) in enumerate(zip( good_new, good_old)):
        a,b = new.ravel()
        c,d = old.ravel()
        mask = cv.line(mask, (a,b), (c,d), color[i].tolist(), 2)
        frame = cv.circle(new_frame,(a,b),5,color[i].tolist(),-1)
    img = cv.add(frame,mask)
    cv.imshow('frame',img)
    # screen = np.array(ImageGrab.grab(bbox=(0,0,2800,1000)))
    # first dimension is height, second dimension is width
    # edges = cv.Canny(window,100,200)
    # something = np.zeros((edges.shape[0],edges.shape[1]))
    # leftValues = np.zeros((2,32))
    # rightValues = np.zeros((2,32))
    # for y in range(280,312):
    #     leftValues[1][y-280] = y
    #     rightValues[1][y-280] = y
    #     for x in range(545,-1,-1):
    #         if (x < 426 or x > 428) and edges[y][x-1] - edges[y][x] > 10:
    #             something[y][x] = 255
    #             leftValues[0][y-280] = x
    #             break
    #     for x in range(740,1280):
    #         if (x < 852 or x > 854) and edges[y][x-1] - edges[y][x] > 10:
    #             something[y][x] = 255
    #             rightValues[0][y-280] = x
    #             break
    # cv.imshow('test', edges)
    if cv.waitKey(25) & 0xFF == ord('q'):
        cv.destroyAllWindows()
        break
