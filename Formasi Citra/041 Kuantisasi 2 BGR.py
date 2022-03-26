import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from urllib3.connectionpool import xrange

img = mpimg.imread("../datasets/jambu.jpg")
height, width = img.shape[0], img.shape[1]

new_img = np.zeros((height, width, 3), np.uint8)

for i in range(height):
    for j in range(width):
        for k in range(3):
            if img[i, j][k] < 128:
                gray = 0
            else:
                gray = 192
            new_img[i, j][k] = np.uint8(gray)

titles = [
    'Original Image', 'New Image',
]

images = [
    img, new_img
]

for i in xrange(2):
    plt.subplot(1, 2, i + 1), plt.imshow(images[i], cmap='gray', vmin='0', vmax='255')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()