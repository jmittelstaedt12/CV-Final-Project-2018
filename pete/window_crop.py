import numpy as np
import cv2

def filter_out_car(img):
    width = img.shape[1]
    height = img.shape[0]
    for i in range(int(0.406*width), int(0.61*width)):
        for j in range(int(0.417*height), int(0.67*height)):
            if img[j][i] == 0:
                img[j][i] = 165
    return img

def region_of_interest(img):

    # define width, height
    width = img.shape[1]
    height = img.shape[0]
    # define vertices:
    ROI_top = [ (0,0), (width,0), (width,0.14*height), (0,0.14*height)]
    ROI_car = [
                (0.406*width, 0.417*height),
                (0.406*width, 0.67* height),
                (0.61*width, 0.67*height),
                (0.61*width, 0.417*height) ]
    # ROI_bottom = [ (height,width), (0.9*height,width), (0.9*height, 0), (height, 0)]
    ROI_bottom = [ (width,height), (width, 0.9*height), (0,0.9*height), (0,height)]
    mask = 255*np.ones_like(img)
    cv2.fillPoly(mask, np.array([ROI_top], np.int32), 0)
    cv2.fillPoly(mask, np.array([ROI_car], np.int32), 0)
    cv2.fillPoly(mask, np.array([ROI_bottom], np.int32), 0)

    # apply mask
    masked_image = cv2.bitwise_and(img,mask)
    return masked_image


def draw_lines(img, lines, color=[255, 0, 0], thickness=3):
    # If there are no lines to draw, exit.
    if lines is None:
        return

    # Make a copy of the original image.
    img = np.copy(img) # Create a blank image that matches the original in size.
    line_img = np.zeros(
        (
            img.shape[0],
            img.shape[1],
        ),
        dtype=np.uint8,
    )

    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(line_img, (x1, y1), (x2, y2), color, thickness)

    # Merge the image with the lines onto the original.
    img = cv2.addWeighted(img, 0.8, line_img, 1.0, 0.0)

    # Return the modified image.
    return img
