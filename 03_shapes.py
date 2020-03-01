import numpy as np
import cv2

#img = cv2.imread("lena.jpg", 1)

# create an empty image
img = np.zeros([512, 512, 3], np.uint8)
img = cv2.line(img, (0,0), (100,100), (0,255,0), 10)
img = cv2.arrowedLine(img, (50,0), (150,150), (255,0,0), 15)
img = cv2.rectangle(img, (384, 63), (439,44), (255,0,0), 5)
img = cv2.circle(img, (347,325), 63, (255,0,255), -1)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, "OpenCV", (10,500), font, 4, (255,255,255),10, cv2.LINE_AA)

cv2.imshow("window title", img)
k = cv2.waitKey(5000)
cv2.destroyAllWindows()

