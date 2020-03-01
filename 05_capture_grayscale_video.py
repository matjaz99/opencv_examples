import cv2

cap = cv2.VideoCapture(0)
# to capture from file, use cv2.VideoCapture("movie.avi")

print(cap.isOpened())

while cap.isOpened():
    ret, frame = cap.read()

    # get properties
    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # convert to grayscale image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame", gray)

    # press q to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
