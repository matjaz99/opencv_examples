import cv2
import datetime

cap = cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

while cap.isOpened():
    ret, frame = cap.read()

    if ret == True:

        font = cv2.FONT_HERSHEY_SIMPLEX
        # try displaying static text like width or height or date and time (with running milliseconds)
        #text = "W: " + str(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) + " H: " + str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) \
        text = str(datetime.datetime.now());
        frame = cv2.putText(frame, text, (10, 50), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow("frame", frame)

        # press q to exit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
