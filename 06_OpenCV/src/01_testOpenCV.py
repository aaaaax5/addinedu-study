import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 500)

while True:
    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)

    if cv2.waitKey(10) == 27:
        break

capture.release()
cv2.destroyAllWindows()
