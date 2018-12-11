import pyautogui
from enum import Enum
import time
class Direction(Enum):
    left = 1
    right = 2

def determine_direction(left_line, right_line, height, width, counter):
    # (left_x_max, max_y, left_x_min, min_y),(right_x_max, max_y, right_x_min, min_y)
    line1 = ((left_line[2], left_line[1]),(left_line[0], left_line[3]))
    line2 = ((right_line[2], right_line[1]),(right_line[0], right_line[3]))
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (height, height) #Typo was here
    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]
    div = det(xdiff, ydiff)
    if div == 0:
       raise Exception('lines do not intersect')
    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    # if counter % 30:
    if x < ((2 * width) / 5):
        print(x,'left')
        # pyautogui.keyUp("z")
        pyautogui.keyDown("left")
        time.sleep(0.34)
        pyautogui.keyUp("left")
        pyautogui.keyDown("z")
    elif x > ((3 * width) / 5):
        print(x,'right')
        # pyautogui.keyUp("z")
        pyautogui.keyDown("right")
        time.sleep(0.34)
        pyautogui.keyUp("right")
        pyautogui.keyDown("z")
    else:
        print(x,"straight")
        pyautogui.keyDown("z")
        time.sleep(0.18)
        pyautogui.keyUp("z")
    return x

def input(input_direction):
    if input_direction == Direction.left:
        pyautogui.keyDown('left')
    if input_direction == Direction.right:
        pyautogui.keyDown('right')
