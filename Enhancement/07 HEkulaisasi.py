import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("../datasets/pemandangan.jpg", 0)

hist, bins = np.histogram(img.flatten(), 256, [0, 256])
cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) / cdf.max()
img1 = cv2.equalizeHist(img)
hist2, bins = np.histogram(img1.flatten(), 256, [0, 256])
cdf2 = hist2.cumsum()
cdf_normalized2= cdf2 * float(hist2.max()) / cdf2.max()

plt.subplot(2, 3, 1)
plt.imshow(img, cmap = 'gray', vmin = 0, vmax = 255)
plt.title('Citra Gray')
plt.axis('off')
plt.subplot(2, 3, 4)
plt.imshow(img1, cmap = 'gray', vmin = 0, vmax = 255)
plt.title('Citra Equalisasi')
plt.axis('off')
plt.subplot(2, 3, 2)
plt.hist(img.flatten(), 256, [0, 256], color='r')
plt.title('Histogram Gray')
plt.subplot(2, 3, 5)
plt.hist(img1.flatten(), 256, [0, 256], color='r')
plt.title('Histogram Equalisasi')
plt.subplot(2, 3, 3)
plt.plot(cdf_normalized, color="b")
plt.title('CDF')
plt.subplot(2, 3, 6)
plt.plot(cdf_normalized2, color="b")
plt.title('CDF')

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()