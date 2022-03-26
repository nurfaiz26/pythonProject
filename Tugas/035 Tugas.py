import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from urllib3.connectionpool import xrange

img1 = mpimg.imread("../datasets/penguin.jpg", 0)
img1_grey = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = mpimg.imread("../datasets/batu.jpg", 0)
img2_grey = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
img3 = mpimg.imread("../datasets/tulip.jpg", 0)
img3_grey = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
img4 = mpimg.imread("../datasets/koala.jpg", 0)
img4_grey = cv2.cvtColor(img4, cv2.COLOR_BGR2GRAY)


def biner_v127(img_src):
    b = cv2.threshold(img_src, 127, 255, cv2.THRESH_BINARY)
    return b


def mean(img_src):
    m = cv2.adaptiveThreshold(img_src, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 5)
    return m


def gauss(img_src):
    g = cv2.adaptiveThreshold(img_src, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 3, 5)
    return g


# penguin
ret, thresh1_1 = biner_v127(img1_grey)
thresh2_1 = mean(img1_grey)
thresh3_1 = gauss(img1_grey)

# batu
ret, thresh1_2 = biner_v127(img2_grey)
thresh2_2 = mean(img2_grey)
thresh3_2 = gauss(img2_grey)

# tulip
ret, thresh1_3 = biner_v127(img3_grey)
thresh2_3 = mean(img3_grey)
thresh3_3 = gauss(img3_grey)


# koala
ret, thresh1_4 = biner_v127(img4_grey)
thresh2_4 = mean(img4_grey)
thresh3_4 = gauss(img4_grey)

titles = [
    'Penguin Image', 'Penguin V = 127', 'Penguin Mean', 'Penguin Gaussian',
    'Batu Image', 'Batu V = 127', 'Batu Mean', 'Batu Gaussian',
    'Tulip Image', 'Tulip V = 127', 'Tulip Mean', 'Tulip Gaussian',
    'Koala Image', 'Koala V = 127', 'Koala Mean', 'Koala Gaussian'
]

images = [
    img1, thresh1_1, thresh2_1, thresh3_1,
    img2, thresh1_2, thresh2_2, thresh3_2,
    img3, thresh1_3, thresh2_3, thresh3_3,
    img4, thresh1_4, thresh2_4, thresh3_4
]

for i in xrange(16):
    plt.subplot(4, 4, i + 1), plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()