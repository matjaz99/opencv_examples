import cv2

print(cv2.__version__)

# read image, -1 means color
img = cv2.imread("lena.jpg", -1)
print(img)

# show image
cv2.imshow("image", img)

# wait for 5 sec, then close the window
cv2.waitKey(5000) & 0xFF
cv2.destroyAllWindows()