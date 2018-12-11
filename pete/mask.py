import numpy as np
import cv2 as cv

def adaptiveROI(img):
    #target = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    #target = cv.cvtColor(img, cv.COLOR_RGB2HSV)
    target = cv.cvtColor(img,cv.COLOR_BGR2RGB)

    # blur taret:
    target = cv.GaussianBlur(target, (7,7), 0)

    # define width, height
    width = img.shape[1]
    height = img.shape[0]

    # Colors: (IN RGB)
    road_upper = np.array([180,180,180])
    road_lower = np.array([155,155,155])
    white_upper = np.array([255,255,255])
    white_lower = np.array([206,210,210])

    testUp = np.array([255,255,255])
    testLo = np.array([127,127,127])

    # Colors (IN HSV):
    # road_upper = np.array([90,5,70])
    # road_lower = np.array([30,5,60])
    # white_upper = np.array([0,0,100])
    # white_lower = np.array([60,2,82])

    # define vertices:
    """
    ROI_top = [ (0,0), (width,0), (width,0.14*height), (0,0.14*height)]
    ROI_car = [ (0.406*width, 0.417*height),
                (0.406*width, 0.67* height),
                (0.61*width, 0.67*height),
                (0.61*width, 0.417*height) ]
    ROI_bottom = [ (height,width), (0.9*height,width), (0.9*height, 0), (height, 0)]
    ROI_bottom = [ (width,height), (width, 0.9*height), (0,0.9*height), (0,height)]
    """

    #mask = np.zeros_like(img)
    #road = cv.inRange(target, road_lower, road_upper)
    mask = cv.inRange(target, road_lower, road_upper)
    #whites = cv.inRange(target, white_lower, white_upper)
    #mask = cv.bitwise_or(road,whites)

    # erode/dilate to fill/magnify holes
    mask = cv.erode(mask, None, iterations=2)
    mask = cv.dilate(mask, None, iterations=2)

    #mask = cv.inRange(target, road_upper, road_lower)
    maskImg = 255*np.ones_like(target)

    #cv2.fillPoly(mask, np.array([ROI_top], np.int32), 0)
    #cv2.fillPoly(mask, np.array([ROI_car], np.int32), 0)
    #cv2.fillPoly(mask, np.array([ROI_bottom], np.int32), 0)

    # apply mask
    masked_image = cv.bitwise_and(target,maskImg,mask=mask)
    return masked_image
