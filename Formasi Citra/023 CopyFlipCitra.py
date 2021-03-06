import cv2
import numpy as np

img = cv2.imread("../datasets/jambu.jpg")

print("Ukuran Image ", img.shape)

height, width = img.shape[0], img.shape[1]

print("Tipe data ", img.dtype)

cv2.imshow("Image Original", img)

print(img[136, 413])

new_img1 = np.zeros((height, width, 3), np.uint8)
new_img1 = img.copy()
new_img1[136:146, 413:423] = (0, 255, 0)

cv2.imshow("Image SetPixel", new_img1)

new_img2 = np.zeros((height, width, 3), np.uint8)
new_img3 = np.zeros((height, width, 3), np.uint8)
new_img4 = np.zeros((height, width, 3), np.uint8)

new_img1=cv2.cvtColor(new_img1, cv2.COLOR_BGR2RGB)

# copy image
for i in range(height):
    for j in range(width):
        for k in range(3):
            new_img2[i, j][k] = img[i, j][k]

cv2.imshow("Image Copy",  new_img2)

new_img2=cv2.cvtColor(new_img1, cv2.COLOR_BGR2RGB)

# flip horizontal
for i in range(height):
    for j in range(width):
        for k in range(3):
            new_img3[i, j][k] = img[height-1-i, j][k]

# flip vertikal
for i in range(height):
    for j in range(width):
        for k in range(3):
            new_img4[i, j][k] = img[i, width-1-j][k]

cv2.imshow("Image Flip Horizontal",  new_img3)
cv2.imshow("Image Flip Vertikal",  new_img4)

cv2.waitKey(0)
cv2.destroyAllWindows()
