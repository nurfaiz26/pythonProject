import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('../datasets/pemandangan.jpg', 0)
kernel = np.ones((7, 7), np.float32)/49
dst_blur = cv2.filter2D(img, -1, kernel)

kernel_v = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
kernel_h = np.transpose(kernel_v)
dst_h = cv2.filter2D(img, -1, kernel_h)
dst_v = cv2.filter2D(img, -1, kernel_v)
dst_edge = cv2.add(dst_v, dst_h)
img2=cv2.add(img, dst_edge)
img_inverse = 255-dst_edge

plt.subplot(151)
plt.imshow(img, cmap='gray', vmin='0', vmax='255')
plt.title("Original")
plt.xticks([0]), plt.yticks([0])
plt.subplot(152)
plt.imshow(dst_blur, cmap='gray', vmin='0', vmax='255')
plt.title("Filtered Blur")
plt.xticks([0]), plt.yticks([0])
plt.subplot(153)
plt.imshow(dst_edge, cmap='gray', vmin='0', vmax='255')
plt.title("Filtered Edge")
plt.xticks([0]), plt.yticks([0])
plt.subplot(154)
plt.imshow(img2, cmap='gray', vmin='0', vmax='255')
plt.title("Filtered Sharpeness")
plt.xticks([0]), plt.yticks([0])
plt.subplot(155)
plt.imshow(img_inverse, cmap='gray', vmin='0', vmax='255')
plt.title("Filtered Sketsa")
plt.xticks([0]), plt.yticks([0])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
