import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("../datasets/pemandangan.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
img1 = 255 - img_gray
img2 = 255 - img1
img3 = 128 - img_gray

plt.subplot(131)
plt.imshow(img_gray, cmap='gray', vmin=0, vmax=255)
plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(132)
plt.imshow(img1, cmap='gray', vmin=0, vmax=255)
plt.title('Invers')
plt.xticks([]), plt.yticks([])

plt.subplot(133)
plt.imshow(img2, cmap='gray', vmin=0, vmax=255)
plt.title('Invers Background Gelap')
plt.xticks([]), plt.yticks([])

# plt.subplot(133)
# plt.imshow(img3, cmap='gray', vmin=0, vmax=255)
# plt.title('Invers -> 128-xg')
# plt.xticks([]), plt.yticks([])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()