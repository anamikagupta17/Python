import cv2

vdo = cv2.VideoCapture(0,cv2.CAP_DSHOW)
print(vdo)
cv2.namedWindow("testAnamika")

counterr = 0

while True:
    ret, frame = vdo.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("testAnamika", frame)

    k = cv2.waitKey(1)
    if k % 256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k % 256 == 32:
        # SPACE pressed
        img_name = "image_{}.png".format(counterr)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        counterr += 1

vdo.release()

cv2.destroyAllWindows()