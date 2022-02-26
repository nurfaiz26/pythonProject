import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from urllib3.connectionpool import xrange

img = mpimg.imread("../datasets/jambu.jpg")

B, G, R = cv2.split(img)

img_gray1 = 0.33 * R + 0.33 * G + 0.33 * B
img_gray1 = img_gray1.astype(np.uint8)
img_RG1 = np.minimum(R, G)
img_gray2 = np.minimum(img_RG1, B)
img_RG2 = np.maximum(R, G)
img_gray3 = np.maximum(img_RG2, B)

titles = [
    'Original Image',
    'CIluminasi Rata Rata',
    'Iluminasi Minimum',
    'Iluminasi Maximum'
]

images = [
    img,
    img_gray1,
    img_gray2,
    img_gray3
]

for i in xrange(4):
    plt.subplot(2, 2, i+1), plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()