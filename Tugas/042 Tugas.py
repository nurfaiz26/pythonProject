import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from urllib3.connectionpool import xrange

img = mpimg.imread("../datasets/jambu.jpg")
height, width = img.shape[0], img.shape[1]

new_img1 = np.zeros((height, width, 3), np.uint8)
new_img2 = np.zeros((height, width, 3), np.uint8)
new_img3 = np.zeros((height, width, 3), np.uint8)
new_img4 = np.zeros((height, width, 3), np.uint8)
new_img5 = np.zeros((height, width, 3), np.uint8)
new_img6 = np.zeros((height, width, 3), np.uint8)

# L2
for i in range(height):
    for j in range(width):
        for k in range(3):
            if img[i, j][k] < 128:
                gray = 0
            else:
                gray = 255
            new_img1[i, j][k] = np.uint8(gray)

# L4
for i in range(height):
    for j in range(width):
        for k in range(3):
            if img[i, j][k] < 64:
                gray = 0
            elif img[i, j][k] < 128:
                gray = 64
            elif img[i, j][k] < 192:
                gray = 128
            else:
                gray = 192
            new_img2[i, j][k] = np.uint8(gray)

# L5
for i in range(height):
    for j in range(width):
        for k in range(3):
            if img[i, j][k] < 64:
                gray = 0
            elif img[i, j][k] < 128:
                gray = 64
            elif img[i, j][k] < 192:
                gray = 128
            else:
                gray = 192
            new_img3[i, j][k] = np.uint8(gray)
# L6
for i in range(height):
    for j in range(width):
        for k in range(3):
            if img[i, j][k] < 64:
                gray = 0
            elif img[i, j][k] < 128:
                gray = 64
            elif img[i, j][k] < 192:
                gray = 128
            else:
                gray = 192
            new_img4[i, j][k] = np.uint8(gray)

# L7
for i in range(height):
    for j in range(width):
        for k in range(3):
            if img[i, j][k] < 64:
                gray = 0
            elif img[i, j][k] < 128:
                gray = 64
            elif img[i, j][k] < 192:
                gray = 128
            else:
                gray = 192
            new_img5[i, j][k] = np.uint8(gray)

# L8
for i in range(height):
    for j in range(width):
        for k in range(3):
            if img[i, j][k] < 32:
                gray = 0
            elif img[i, j][k] < 96:
                gray = 32
            elif img[i, j][k] < 96:
                gray = 64
            elif img[i, j][k] < 128:
                gray = 96
            elif img[i, j][k] < 160:
                gray = 128
            elif img[i, j][k] < 192:
                gray = 160
            elif img[i, j][k] < 224:
                gray = 192
            else:
                gray = 224
            new_img6[i, j][k] = np.uint8(gray)

titles = [
    '(a) Original Image', '(b) Kuantisasi L2', '(c) Kuantisasi L4', '(d) Kuantisasi L5',
    '(e) Kuantisasi L6', '(f) Kuantisasi L7', '(g) Kuantisasi L8'
]

images = [
    img, new_img1, new_img2, new_img3, new_img4, new_img5, new_img6
]

for i in xrange(7):
    plt.subplot(2, 4, i + 1), plt.imshow(images[i], cmap='gray', vmin='0', vmax='255')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()