import numpy as np
import cv2 as cv
from PIL import Image,ImageGrab
from mss import mss
import time

mon = {'top': 50, 'left': 0, 'width': 1280, 'height': 312}
sct = mss()
cv.namedWindow('test', flags=cv.WINDOW_NORMAL)
cv.moveWindow('test',0,380)
while 1:
    # screen = np.array(ImageGrab.grab(bbox=(0,0,2800,1000)))
    cap = sct.grab(mon)
    img = Image.frombytes('RGB', (cap.width, cap.height), cap.rgb).convert('L')
    window = np.array(img.resize((int(img.width/2), int(img.height/2))))
    # first dimension is height, second dimension is width
    edges = cv.Canny(window,100,200)
    something = np.zeros((edges.shape[0],edges.shape[1]))
    leftValues = np.zeros((2,32))
    rightValues = np.zeros((2,32))
    for y in range(280,312):
        leftValues[1][y-280] = y
        rightValues[1][y-280] = y
        for x in range(545,-1,-1):
            if (x < 426 or x > 428) and edges[y][x-1] - edges[y][x] > 10:
                something[y][x] = 255
                leftValues[0][y-280] = x
                break
        for x in range(740,1280):
            if (x < 852 or x > 854) and edges[y][x-1] - edges[y][x] > 10:
                something[y][x] = 255
                rightValues[0][y-280] = x
                break
    cv.imshow('test', something)
    if cv.waitKey(25) & 0xFF == ord('q'):
        cv.destroyAllWindows()
        break
