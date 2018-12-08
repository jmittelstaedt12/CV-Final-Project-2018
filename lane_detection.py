import numpy as np
import cv2 as cv
from PIL import Image,ImageGrab
from mss import mss
import time
import window_crop as edge_functions
import math

width = 640
height = 480
def lane_detect(img):
    # return edge_functions.region_of_interest(img)
    edges = cv.Canny(img,100,200,apertureSize = 3)
    edges = cv.GaussianBlur(edges, (7,7), 0)
    roi_edges = edge_functions.region_of_interest(edges)
    lines = cv.HoughLinesP(
        roi_edges,
        rho=6,
        theta=np.pi / 60,
        threshold=160,
        lines=np.array([]),
        minLineLength=50,
        maxLineGap=7
    )
    if lines is not None:
        newLines = []
        for line in lines:
            for x1, y1, x2, y2 in line:
                if(x2 == x1):
                    continue
                slope = (y2 - y1) / (x2 - x1) # <-- Calculating the slope.
                # if math.fabs(slope) < 0.1: # <-- Only consider extreme slope
                #     continue
                if x1 > width / 2 and slope > 0:
                    newLines.append(line)
                if x1 < width / 2 and slope < 0:
                    newLines.append(line)
    # return edge_functions.draw_lines(roi_edges,newLines)
    lines = newLines
    left_line_x = []
    left_line_y = []
    right_line_x = []
    right_line_y = []
    if lines is not None:
        for line in lines:
            for x1, y1, x2, y2 in line:
                if(x2 == x1):
                    continue
                slope = (y2 - y1) / (x2 - x1) # <-- Calculating the slope.
                # if math.fabs(slope) < 0.1: # <-- Only consider extreme slope
                #     continue
                # if x1 < width / 2 and slope <= 0:
                #     continue
                # if x1 > width / 2 and slope >= 0:
                #     continue
                if slope <= 0: # <-- If the slope is negative, left group.
                    left_line_x.extend([x1, x2])
                    left_line_y.extend([y1, y2])
                else: # <-- Otherwise, right group.
                    right_line_x.extend([x1, x2])
                    right_line_y.extend([y1, y2])
    if left_line_x and right_line_x:
        min_y = 0# <-- Just below the horizon
        max_y = int(roi_edges.shape[0])# <-- The bottom of the image
        poly_left = np.poly1d(np.polyfit(
            left_line_y,
            left_line_x,
            deg=1
        ))
        left_x_start = int(poly_left(max_y))
        left_x_end = int(poly_left(min_y))
        poly_right = np.poly1d(np.polyfit(
            right_line_y,
            right_line_x,
            deg=1
        ))
        right_x_start = int(poly_right(max_y))
        right_x_end = int(poly_right(min_y))
        line_image = edge_functions.draw_lines(
            roi_edges,
            [[
                [left_x_start, max_y, left_x_end, min_y],
                [right_x_start, max_y, right_x_end, min_y],
            ]],thickness=5)
        # cv.imshow('test', line_image)
        return line_image
    else:
        return roi_edges
        # cv.imshow('test',roi_edges)
