import cv2

print(cv2.__version__)

img = cv2.imread("aat_31a.jpg", -1)
print(img)

cv2.imshow("image", img)
cv2.waitKey(5000) & 0xFF
cv2.destroyAllWindows()