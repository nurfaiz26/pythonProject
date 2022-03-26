import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("../datasets/underwater.jpg", 0)
# img_gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

x_min = np.min(img)
x_max = np.max(img)
print (x_min)
print (x_max)
sk = 255. / (x_max-x_min)
img1 = sk * (img-x_min)
img1 = np.uint8(img1)

hist2 = cv2.calcHist([img1], [0], None, [256], [0, 256])
hist1 = cv2.calcHist([img], [0], None, [256], [0, 256])

plt.subplot(221)
plt.imshow(img)
plt.axis('off')
plt.title("Original")
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.subplot(222)
plt.plot(hist1)
plt.grid()
plt.xlim([0, 255])

plt.subplot(223)
plt.imshow(img1)
plt.axis('off')
plt.title("Enhanced")
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.subplot(224)
plt.plot(hist2)
plt.grid()
plt.xlim([0, 255])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()