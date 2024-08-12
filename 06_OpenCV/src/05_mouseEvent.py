import cv2
import numpy as np

img = np.ones((512,512,3), np.uint8)


def draw_circle(event, x, y, flage, param):
    # "if event == 1" has same meaning.
    # But acording to coding rule, this method is not recomanded.
    if event == cv2.EVENT_FLAG_LBUTTON:
        print(x, y)
        cv2.circle(img, (x,y), 5, (50, 50, 200), -1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        print(x, y)
        cv2.circle(img, (x, y), 5, (200, 50, 50), -1)
    elif event == cv2.EVENT_MBUTTONDOWN:
        print(x, y)
        cv2.circle(img, (x, y), 5, (50, 200, 50), -1)


cv2.namedWindow(winname='my_first_drawing')
cv2.setMouseCallback('my_first_drawing', draw_circle, img)

while True:
    cv2.imshow('my_first_drawing', img)
    
    #wait key(ASCII number)
    if cv2.waitKey(10) == 27:
        break

cv2.destroyAllWindows()