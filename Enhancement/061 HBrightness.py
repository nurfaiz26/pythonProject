import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("../datasets/pemandangan.jpg", 0)
#img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img1 = np.abs(img - 30.)
img1 = np.uint8(img1)
img2 = img + 30.
img2 = np.uint8(img2)
hist1 = cv2.calcHist([img1], [0], None, [256], [0, 256])
hist2 = cv2.calcHist([img], [0], None, [256], [0, 256])
hist3 = cv2.calcHist([img2], [0], None, [256], [0, 256])

plt.subplot(321)
plt.axis('off')
plt.imshow(img1, cmap='gray', vmin=0, vmax=255)
plt.title("-30")
plt.subplot(322)
plt.plot(hist1)
plt.grid()
plt.xlim([0, 255])

plt.subplot(323)
plt.axis('off')
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.title("-Original")
plt.subplot(324)
plt.plot(hist2)
plt.grid()
plt.xlim([0, 255])

plt.subplot(325)
plt.axis('off')
plt.imshow(img2, cmap='gray', vmin=0, vmax=255)
plt.title("+30")
plt.subplot(326)
plt.plot(hist3)
plt.grid()
plt.xlim([0, 255])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()