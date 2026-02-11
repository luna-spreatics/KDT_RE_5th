import cv2

cap = cv2.VideoCapture('OpenCV/images/video.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # 영상 프레임을 1.5배로 리사이즈
    # 보간법 - INTER_CUBIC
    resized_frame = cv2.resize(
        frame, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)

    cv2.imshow("Resized Video", resized_frame)

    if cv2.waitKey(33) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
