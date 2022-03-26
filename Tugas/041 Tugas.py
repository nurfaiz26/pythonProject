import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from urllib3.connectionpool import xrange

img = mpimg.imread("../datasets/jambu.jpg")
height, width = img.shape[0], img.shape[1]

# rata rata derajat keabuan
r, g, b = cv2.split(img)
gray_rate = (r + g + b) / 3
gray_rate = gray_rate.astype(np.uint8)
img_gray_rate = cv2.cvtColor(gray_rate, cv2.COLOR_GRAY2RGB)

new_img1 = np.zeros((height, width, 3), np.uint8)
new_img2 = np.zeros((height, width, 3), np.uint8)
new_img3 = np.zeros((height, width, 3), np.uint8)

for i in range(height):
    for j in range(width):
        for k in range(3):
            if img[i, j][k] < 100:
                gray = 0
            else:
                gray = 192
            new_img1[i, j][k] = np.uint8(gray)

for i in range(height):
    for j in range(width):
        for k in range(3):
            if img[i, j][k] < 200:
                gray = 0
            else:
                gray = 192
            new_img2[i, j][k] = np.uint8(gray)

for i in range(height):
    for j in range(width):
        for k in range(3):
            if img[i, j][k] < img_gray_rate[i, j][k]:
                gray = 0
            else:
                gray = 192
            new_img3[i, j][k] = np.uint8(gray)

titles = [
    'Original Image', 'Threshold = 100', 'Threshold = 200', 'Threshold = Grayscale Rate'
]

images = [
    img, new_img1, new_img2, new_img3
]

for i in xrange(4):
    plt.subplot(2, 2, i + 1), plt.imshow(images[i], cmap='gray', vmin='0', vmax='255')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()