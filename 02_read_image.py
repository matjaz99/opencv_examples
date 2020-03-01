import cv2

img = cv2.imread("lena.jpg", 0)
print(img)

cv2.imshow("window title", img)
k = cv2.waitKey(0) & 0xFF
if k == 27:
    # exit when esc key is pressed
    cv2.destroyAllWindows()
elif k == ord("s"):
    # save the image and exit if s key is pressed
    cv2.imwrite("lena_copy.png", img)
    cv2.destroyAllWindows()
