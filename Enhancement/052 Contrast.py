import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("../datasets/pemandangan.jpg", 0)

img1 = img * 0.5
img2 = img * 0.75
img3 = img * 1.25
img4 = img * 1.5

plt.subplot(151)
plt.imshow(img1, cmap='gray', vmin=0, vmax= 255)
plt.title('* 0.5')
plt.xticks([]), plt.yticks([])

plt.subplot(152)
plt.imshow(img2, cmap='gray', vmin=0, vmax=255)
plt.title('* 0.75')
plt.xticks([]), plt.yticks([])

plt.subplot(153)
plt.imshow(img, cmap='gray', vmin=0, vmax =255)
plt.title('* 1')
plt.xticks([]), plt.yticks([])

plt.subplot(154)
plt.imshow(img3, cmap='gray', vmin=0, vmax= 255)
plt.title('* 1.25')
plt.xticks([]), plt.yticks([])

plt.subplot(155)
plt.imshow(img4, cmap='gray', vmin=0, vmax=255)
plt.title('* 1.5')
plt.xticks([]), plt.yticks([])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()