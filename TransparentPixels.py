# you need the package open-contrib-python for opencv

import cv2

# flag 1 means show color. flag 0 means show in grayscale. flag -1 means show with alpha??
img = cv2.imread("zenvost1-2.png", 1)

# add alpha to the image
img_alpha = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
# to those pixels that are white, set their alpha to 0
for i in range(len(img_alpha)):
    for j in range(len(img_alpha[0])):
        # dont forget -- 16 bit image! so you want a pixel with value 2^16, not 2^8
        if img_alpha[i][j][0] == 255 and img_alpha[i][j][1] == 255 and img_alpha[i][j][2] == 255:
            img_alpha[i][j][3] = 0

cv2.imshow("Original Image", img)
cv2.imshow("Transformation", img_alpha)
cv2.imwrite("transformation.png", img_alpha)
# important so your image does not close instantly.
cv2.waitKey(0)