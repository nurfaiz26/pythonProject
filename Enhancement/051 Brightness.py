import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("../datasets/pemandangan.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

img1 = np.abs(img_gray - 30.)
img1 = np.uint8(img1)
img2 = img_gray + 30.
img2 = np.uint8(img2)
img3 = img_gray + 255
img3 = np.uint8(img3)

plt.subplot(141)
plt.imshow(img_gray, cmap='gray', vmin=0, vmax=255)
plt.title("Original Image")
plt.xticks([]), plt.yticks([])

plt.subplot(142)
plt.imshow(img1, cmap='gray', vmin=0, vmax=255)
plt.title("Brigtness -30")
plt.xticks([]), plt.yticks([])

plt.subplot(143)
plt.imshow(img2, cmap='gray', vmin=0, vmax=255)
plt.title("Brigtness +30")
plt.xticks([]), plt.yticks([])

plt.subplot(144)
plt.imshow(img3, cmap='gray', vmin=0, vmax=255)
plt.title("Brigtness +255")
plt.xticks([]), plt.yticks([])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()