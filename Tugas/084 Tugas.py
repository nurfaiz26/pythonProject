import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("../datasets/bunga.jpg", 0)


def dstInv(dst):
    return 255 - dst


kernel_v_robert = np.array([-5, 5])
kernel_h_robert = np.transpose(kernel_v_robert)
dst_v_robert = cv2.filter2D(img, -1, kernel_v_robert)
dst_h_robert = cv2.filter2D(img, -1, kernel_h_robert)
dst_robert = cv2.add(dst_h_robert, dst_v_robert)

kernel_v_prewitt = np.array([[-5, 0, 5], [-5, 0, 5], [-5, 0, 5]])
kernel_h_prewitt = np.transpose(kernel_v_prewitt)
dst_v_prewitt = cv2.filter2D(img, -1, kernel_v_prewitt)
dst_h_prewitt = cv2.filter2D(img, -1, kernel_h_prewitt)
dst_prewitt = cv2.add(dst_h_prewitt, dst_v_prewitt)

# kernel_v_sobel = np.array([[-1, 0, -1], [-2, 0, 2], [-1, 0, 1]])
# kernel_h_sobel = np.transpose(kernel_v_sobel)
# dst_v_sobel = cv2.filter2D(img, -1, kernel_v_sobel)
# dst_h_sobel = cv2.filter2D(img, -1, kernel_h_sobel)
# dst_sobel = cv2.add(dst_h_sobel, dst_v_sobel)
dst_sobel = cv2.Sobel(img, cv2.CV_64F, 1, 1, ksize=5)
dst_sobel = cv2.convertScaleAbs(dst_sobel)

# kernel_laplacian = np.array([[1, -2, 1], [-2, 4, -2], [1, -2, 1]])
# dst_laplacian = cv2.filter2D(img, -1, kernel_laplacian)
dst_laplacian = cv2.Laplacian(img, cv2.CV_64F, ksize=5)
dst_laplacian = cv2.convertScaleAbs(dst_laplacian)

plt.subplot(231)
plt.imshow(img, cmap='gray', vmin='0', vmax='255')
plt.title("Original")
plt.xticks([0]), plt.yticks([0])
plt.subplot(232)
plt.imshow(dstInv(dst_robert), cmap='gray', vmin='0', vmax='255')
plt.title("Inv Dst Robert")
plt.xticks([0]), plt.yticks([0])
plt.subplot(233)
plt.imshow(dstInv(dst_prewitt), cmap='gray', vmin='0', vmax='255')
plt.title("Inv Dst Prewitt")
plt.xticks([0]), plt.yticks([0])
plt.subplot(234)
plt.imshow(dstInv(dst_sobel), cmap='gray', vmin='0', vmax='255')
plt.title("Inv Dst Sobel")
plt.xticks([0]), plt.yticks([0])
plt.subplot(235)
plt.imshow(dstInv(dst_laplacian), cmap='gray', vmin='0', vmax='255')
plt.title("Inv Dst Laplacian")
plt.xticks([0]), plt.yticks([0])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
