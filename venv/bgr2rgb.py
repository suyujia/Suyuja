import cv2

for x in range(0,147):
    img = cv2.imread("D:\\auto_press_down_gun\\cap\\{}.png".format(str(x)))
    img2 = img[:, :, :: -1]
    cv2.imwrite("D:\\auto_press_down_gun\\rgb\\{}.png".format(str(x)), img2)

