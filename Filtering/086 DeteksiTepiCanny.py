import cv2
import matplotlib.pyplot as plt

img = cv2.imread("../datasets/pemandangan.jpg", 0)
sobel_x = cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)
sobel_y = cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)
sobel = cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)
sobel = cv2.convertScaleAbs(sobel)

canny = cv2.Canny(img, 100, 200)
im_lap = cv2.Laplacian(img, ksize=5, ddepth=cv2.CV_64F)
im_lap = cv2.convertScaleAbs(im_lap)

plt.subplot(221)
plt.imshow(img, cmap='gray', vmin='0', vmax='255')
plt.title("Grayscale")
plt.xticks([0]), plt.yticks([0])
plt.subplot(222)
plt.imshow(sobel, cmap='gray', vmin='0', vmax='255')
plt.title("Sobel")
plt.xticks([0]), plt.yticks([0])
plt.subplot(223)
plt.imshow(canny, cmap='gray', vmin='0', vmax='255')
plt.title("Canny")
plt.xticks([0]), plt.yticks([0])
plt.subplot(224)
plt.imshow(im_lap, cmap='gray', vmin='0', vmax='255')
plt.title("Laplacian")
plt.xticks([0]), plt.yticks([0])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
