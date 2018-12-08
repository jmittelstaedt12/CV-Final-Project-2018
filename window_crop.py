import numpy as np
import cv2

def region_of_interest(img):
    width = img.shape[1]
    height = img.shape[0]
    # width:0->640
    # height:0->480
    # 260->390
    # 0.406w -> 0.61w
    # 0.417h->0.67h
    region_of_interest_vertices = [
        (0.406*width, 0.417*height),
        (0.406*width, 0.67*height),
        (0.61*width, 0.67*height),
        (0.61*width, 0.417*height),
        # (0, height / 9),
        # (0, (3 * height) / 5),
        # (width / 2, (2 * height) / 5),
        # (width, (3 * height) / 5),
        # (width, height / 9),
    ]
    mask = np.ones_like(img) * 255
    cv2.fillPoly(mask, np.array([region_of_interest_vertices], np.int32), 0)
    masked_image = cv2.bitwise_and(img,mask)
    new_vertices = [
        (0, 0),
        (0, 0.2*height),
        (width, 0.2*height),
        (width, 0),
    ]
    mask = np.ones_like(img) * 255
    cv2.fillPoly(mask, np.array([new_vertices], np.int32), 0)
    masked_image = cv2.bitwise_and(masked_image,mask)

    new_vertices = [
        (0, height),
        (width, height),
        (width, 0.9*height),
        (0, 0.9*height),
    ]
    mask = np.ones_like(img) * 255
    cv2.fillPoly(mask, np.array([new_vertices], np.int32), 0)
    masked_image = cv2.bitwise_and(masked_image,mask)
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
    # Loop over all lines and draw them on the blank image.
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(line_img, (x1, y1), (x2, y2), color, thickness)
    # Merge the image with the lines onto the original.
    img = cv2.addWeighted(img, 0.8, line_img, 1.0, 0.0)
    # Return the modified image.
    return img
