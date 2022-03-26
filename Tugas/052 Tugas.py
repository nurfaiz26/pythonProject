import cv2
import numpy as np
import  matplotlib.pyplot as plt

img = cv2.imread("../datasets/pemandangan.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

img1 = 40*np.log(0.5*img_gray)
img1 = np.uint8(img1)
img2 = 40.*np.exp(0.5*img1)
img2 = np.uint8(img2)

plt.subplot(1, 3, 1)
plt.imshow(img_gray, cmap='gray')
plt.title("(a) Original Image")
plt.xticks([]), plt.yticks([])

plt.subplot(1, 3, 2)
plt.imshow(img1, cmap='gray', vmin='0', vmax='255')
plt.title("(b) log a=40 b= 0.5")
plt.xticks([]), plt.yticks([])

plt.subplot(1, 3, 3)
plt.imshow(img2, cmap='gray', vmin='0', vmax='255')
plt.title("(c) log inv a=40 b= 0.5")
plt.xticks([]), plt.yticks([])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
