import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("../datasets/pemandangan.jpg", 0)
noise = np.random.randn(*img.shape) * 10
img_noise = np.abs(img + noise)
img_noise = np.uint8(img_noise)
dst_gauss = cv2.GaussianBlur(img_noise, [7, 7], 0)
dst_med = cv2.medianBlur(img_noise, 7)

plt.subplot(131)
plt.imshow(img_noise, cmap='gray', vmin='0', vmax='255')
plt.title("Image Noise")
plt.xticks([0]), plt.yticks([0])
plt.subplot(132)
plt.imshow(dst_gauss, cmap='gray', vmin='0', vmax='255')
plt.title("Gaussian")
plt.xticks([0]), plt.yticks([0])
plt.subplot(133)
plt.imshow(dst_med, cmap='gray', vmin='0', vmax='255')
plt.title("Median")
plt.xticks([0]), plt.yticks([0])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
