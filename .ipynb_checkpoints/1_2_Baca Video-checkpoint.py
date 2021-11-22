import cv2

path_video = "./sample/vid.mp4"
vcap = cv2.VideoCapture(path_video)

# Baca semua frame dalam video sampai habis
while True:
    ok, frame = vcap.read()
    cv2.imshow("Frame VideoX", frame)
    if cv2.waitKey(1) == ord('q'):
        break