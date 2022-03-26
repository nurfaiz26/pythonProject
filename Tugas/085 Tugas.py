import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("../datasets/bunga.jpg", 0)
kernel1 = np.ones([5, 5], np.float32) / 25
img_blur = cv2.filter2D(img, -1, kernel1)
kernel2a = 2 * np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
kernel2b = np.transpose(kernel2a)
kernel2 = kernel2a + kernel2b
img_edge = cv2.filter2D(img, -1, kernel2)
img_edge = np.uint8(img_edge)
img_sharp = cv2.add(img_blur, img_edge)/2

plt.subplot(121)
plt.imshow(img, cmap='gray', vmin='0', vmax='255')
plt.title("Original")
plt.xticks([0]), plt.yticks([0])
plt.subplot(122)
plt.imshow(img_sharp, cmap='gray', vmin='0', vmax='255')
plt.title("Sharpeness (2*LPF + HPF)/2")
plt.xticks([0]), plt.yticks([0])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
