import numpy as np
import cv2 as cv

def adaptiveROI(img):
    target = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    # define width, height
    width = img.shape[1]
    height = img.shape[0]

    # Colors: (IN RGB)
    # road_upper = np.array([168,176,172])
    # road_lower = np.array([156,160,164])
    # white_upper = np.array([255,255,255])
    # white_lower = np.array([206,210,210])

    # Colors (IN HSV):
    road_upper = np.array([90,5,70])
    road_lower = np.array([30,5,60])
    white_upper = np.array([0,0,100])
    white_lower = np.array([60,2,82])

    """
    road_upper = cv.cvtColor(gray1, cv.COLOR_BGR2HSV )
    road_lower = cv.cvtColor(gray2, cv.COLOR_BGR2HSV )
    white_upper = cv.cvtColor(white1, cv.COLOR_BGR2HSV )
    white_lower = cv.cvtColor(whit2, cv.COLOR_BGR2HSV )
    """
    
    # define vertices:
    ROI_top = [ (0,0), (width,0), (width,0.14*height), (0,0.14*height)]
    ROI_car = [ (0.406*width, 0.417*height),
                (0.406*width, 0.67* height),
                (0.61*width, 0.67*height),
                (0.61*width, 0.417*height) ]
    ROI_bottom = [ (height,width), (0.9*height,width), (0.9*height, 0), (height, 0)]
    ROI_bottom = [ (width,height), (width, 0.9*height), (0,0.9*height), (0,height)]

    #mask = np.zeros_like(img)
    mask = cv.inRange(target, white_upper, road_lower)
    mask = cv.erode(mask, None, iterations=2)
    mask = cv.dilate(mask, None, iterations=2)
    #whites = cv.inRange(img, white_upper, white_lower)
    
    #mask = cv.bitwise_or(mask, grays)
    #mask = cv.bitwise_or(mask, whites)

    #cv2.fillPoly(mask, np.array([ROI_top], np.int32), 0)
    #cv2.fillPoly(mask, np.array([ROI_car], np.int32), 0)
    #cv2.fillPoly(mask, np.array([ROI_bottom], np.int32), 0)
    
    # apply mask
    masked_image = cv.bitwise_and(target,mask)
    return masked_image

