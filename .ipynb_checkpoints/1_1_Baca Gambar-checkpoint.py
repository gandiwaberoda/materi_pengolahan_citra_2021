import cv2

path_gambar = "./sample/robot_ball.jpg"
img = cv2.imread(path_gambar)

cv2.imshow("Raw Gambar", img)
cv2.waitKey()
cv2.destroyWindow("Raw Gambar")