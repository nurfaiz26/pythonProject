import cv2
import matplotlib.pyplot as plt

img = cv2.imread("../datasets/pemandangan.jpg", 0)
img_blur1 = cv2.blur(img, [5, 5])
img_blur2 = cv2.blur(img, [11, 11])

plt.subplot(131)
plt.imshow(img, cmap='gray', vmin='0', vmax='255')
plt.title("Original")
plt.xticks([0]), plt.yticks([0])
plt.subplot(132)
plt.imshow(img_blur1, cmap='gray', vmin='0', vmax='255')
plt.title("Blur 5x5")
plt.xticks([0]), plt.yticks([0])
plt.subplot(133)
plt.imshow(img_blur2, cmap='gray', vmin='0', vmax='255')
plt.title("Blur 11x11")
plt.xticks([0]), plt.yticks([0])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
