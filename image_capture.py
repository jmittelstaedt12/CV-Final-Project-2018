import numpy as np
import cv2
from PIL import Image
from mss import mss
import time

mon = {'top': 0, 'left': 0, 'width': 320, 'height': 200}
sct = mss()
last_time = time.time()
cv2.namedWindow('test')
cv2.moveWindow('test',0,300)
while 1:
    cap = sct.grab(mon)
    img = Image.frombytes('RGB', (cap.width, cap.height), cap.rgb)
    cv2.imshow('test', cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB))
    # print('Loop time took {} seconds'.format(time.time() - last_time))
    last_time = time.time()
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
