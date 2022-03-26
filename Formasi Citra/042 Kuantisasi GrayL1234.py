import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from urllib3.connectionpool import xrange

img = mpimg.imread("../datasets/jambu.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_gray = 128 * np.floor(img/128)
gray1 = img_gray
img_gray = 64 * np.floor(img/64)
gray2 = np.uint8(img_gray)
img_gray = 32 * np.floor(img/32)
gray3 = np.uint8(img_gray)
img_gray = 16 * np.floor(img/16)
gray4 = np.uint8(img_gray)

titles = [
    '(a) Kuantisasi Gray L1',
    '(b) Kuantisasi Gray L2',
    '(c) Kuantisasi Gray L3',
    '(d) Kuantisasi Gray L4'
]

images = [
    gray1, gray2, gray3, gray4
]

for i in xrange(4):
    plt.subplot(2, 2, i + 1), plt.imshow(images[i], cmap='gray', vmin='0', vmax='255')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()