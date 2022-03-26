import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("../datasets/pemandangan.jpg", 0)
noise = np.random.randn(*img.shape) * 10
img_noise = np.abs(img + noise)
img_noise = np.uint8(img_noise)

plt.subplot(121)
plt.imshow(img, cmap='gray', vmin='0', vmax='255')
plt.title("Original")
plt.xticks([0]), plt.yticks([0])
plt.subplot(122)
plt.imshow(img_noise, cmap='gray', vmin='0', vmax='255')
plt.title("Image Noise")
plt.xticks([0]), plt.yticks([0])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
