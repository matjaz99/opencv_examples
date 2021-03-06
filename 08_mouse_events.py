import numpy as np
import cv2

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # left mouse button action - show coordinates
        print(x, ", ", y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = str(x) + ", " + str(y);
        cv2.putText(img, text, (x, y), font, .5, (255, 255, 0), 2, cv2.LINE_AA)
        cv2.imshow("image", img)
    if event == cv2.EVENT_RBUTTONDOWN:
        # right mouse button action - show rgb channels
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = str(blue) + ", " + str(green) + ", " + str(red)
        cv2.putText(img, text, (x, y), font, .5, (0, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow("image", img)

#img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread("lena.jpg")
cv2.imshow("image", img)

cv2.setMouseCallback("image", click_event)

# press q to exit
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
