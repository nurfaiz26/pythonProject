import  cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from urllib3.connectionpool import xrange

img = mpimg.imread("../datasets/jambu.jpg")

b = img.copy()
b[:, :, 1] = 0
b[:, :, 2] = 0

g = img.copy()
g[:, :, 0] = 0
g[:, :, 2] = 0

r = img.copy()
r[:, :, 0] = 0
r[:, :, 1] = 0

# cv2.imshow("B-RGB", img1[:, :, 0])
# cv2.imshow("G-RGB", img1[:, :, 1])
# cv2.imshow("R-RGB", img1[:, :, 2])

titles = [
    'Original Image',
    'B-RGB',
    'G-RGB',
    'R-RGB'
]

images = [
    img,
    r,
    g,
    b
]

for i in xrange(4):
    plt.subplot(2, 2, i+1), plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()