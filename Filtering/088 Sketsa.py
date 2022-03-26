import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('../datasets/pemandangan.jpg', 0)
kernel = np.array([[1, 2,  1], [2, -12, 2], [1, 2, 1]])
dst = cv2.filter2D(img, -1, kernel)
sketsa = 255 - dst

plt.subplot(121)
plt.imshow(img, cmap='gray', vmin='0', vmax='255')
plt.title("Original")
plt.xticks([0]), plt.yticks([0])
plt.subplot(122)
plt.imshow(sketsa, cmap='gray', vmin='0', vmax='255')
plt.title("Sketsa")
plt.xticks([0]), plt.yticks([0])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
