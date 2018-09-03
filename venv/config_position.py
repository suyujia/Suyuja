import os
import cv2
from PIL import Image
import numpy as np

image = cv2.imread('130.png')
weapon0 = image[186:226,2232:2552]
w0_muzzle = image[380:445,2192:2256]
w0_grip = image[380:445,2327:2393]
w0_magazine = image[380:445,2474:2540]
w0_scope = image[207:273,2554:2620]
w0_butt = image[380:445,2756:2822]

weapon1 = image[470:510,2232:2552]
w1_muzzle = image[665:730,2192:2256]
w1_grip = image[665:730,2327:2393]
w1_magazine = image[664:730,2474:2540]
w1_scope = image[490:555,2554:2620]
w1_butt = image[664:730,2756:2822]

cv2.imwrite("./test/weapon0.jpg",weapon0)
cv2.imwrite("./test/w0_muzzle.jpg",w0_muzzle)
cv2.imwrite("./test/w0_grip.jpg",w0_grip)
cv2.imwrite("./test/w0_magazine.jpg",w0_magazine)
cv2.imwrite("./test/w0_scope.jpg",w0_scope)
cv2.imwrite("./test/w0_butt.jpg",w0_butt)

cv2.imwrite("./test/weapon1.jpg",weapon1)
cv2.imwrite("./test/w1_muzzle.jpg",w1_muzzle)
cv2.imwrite("./test/w1_grip.jpg",w1_grip)
cv2.imwrite("./test/w1_magazine.jpg",w1_magazine)
cv2.imwrite("./test/w1_scope.jpg",w1_scope)
cv2.imwrite("./test/w1_butt.jpg",w1_butt)

img1 = cv2.imread("./test/weapon0.jpg")
img2 = cv2.imread("./test/weapon1.jpg")
shield1 = np.zeros_like(img1)
shield2 = np.zeros_like(img2)

for i, i_ in enumerate(img1):
    for j, j_ in enumerate(i_):
       if j_[0] < 240 and j_[1] < 240 and j_[2] < 240:
           shield1[i,j] = [0,0,0]
       else:
           shield1[i,j] = [255,255,255]

for i, i_ in enumerate(img2):
    for j, j_ in enumerate(i_):
       if j_[0] < 240 and j_[1] < 240 and j_[2] < 240:
           shield2[i,j] = [0,0,0]
       else:
           shield2[i,j] = [255,255,255]

cv2.imwrite('./test/shield1.png',shield1)
cv2.imwrite('./test/shield2.png',shield2)
cv2.imshow('',shield1)
cv2.imshow('',shield2)


