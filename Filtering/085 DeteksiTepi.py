import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("../datasets/pemandangan.jpg", 0)
kernel_v = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
kernel_h = np.transpose(kernel_v)
dst_h = cv2.filter2D(img, -1, kernel_h)
dst_v = cv2.filter2D(img, -1, kernel_v)
dst = cv2.add(dst_h, dst_v)

plt.subplot(221)
plt.imshow(img, cmap='gray', vmin='0', vmax='255')
plt.title("Original")
plt.xticks([0]), plt.yticks([0])
plt.subplot(222)
plt.imshow(dst_h, cmap='gray', vmin='0', vmax='255')
plt.title("Horizontal")
plt.xticks([0]), plt.yticks([0])
plt.subplot(223)
plt.imshow(dst_v, cmap='gray', vmin='0', vmax='255')
plt.title("Vertikal")
plt.xticks([0]), plt.yticks([0])
plt.subplot(224)
plt.imshow(dst, cmap='gray', vmin='0', vmax='255')
plt.title("Deteksi Tepi Prewitt")
plt.xticks([0]), plt.yticks([0])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
