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


def biner(img_src):
    b = cv2.threshold(img_src, 127, 255, cv2.THRESH_BINARY)
    return b


def biner_inv(img_src):
    b_inv = cv2.threshold(img_src, 127, 255, cv2.THRESH_BINARY_INV)
    return b_inv


def trunc(img_src):
    t = cv2.threshold(img_src, 127, 255, cv2.THRESH_TRUNC)
    return t


def tozero(img_src):
    tz = cv2.threshold(img_src, 127, 255, cv2.THRESH_TOZERO)
    return tz


def tozero_inv(img_src):
    tz_inv = cv2.threshold(img_src, 127, 255, cv2.THRESH_TOZERO_INV)
    return tz_inv


# penguin
ret, thresh1_1 = biner(img1_grey)
ret, thresh2_1 = biner_inv(img1_grey)
ret, thresh3_1 = trunc(img1_grey)
ret, thresh4_1 = tozero(img1_grey)
ret, thresh5_1 = tozero_inv(img1_grey)

# batu
ret, thresh1_2 = biner(img2_grey)
ret, thresh2_2 = biner_inv(img2_grey)
ret, thresh3_2 = trunc(img2_grey)
ret, thresh4_2 = tozero(img2_grey)
ret, thresh5_2 = tozero_inv(img2_grey)

# tulip
ret, thresh1_3 = biner(img3_grey)
ret, thresh2_3 = biner_inv(img3_grey)
ret, thresh3_3 = trunc(img3_grey)
ret, thresh4_3 = tozero(img3_grey)
ret, thresh5_3 = tozero_inv(img3_grey)

# koala
ret, thresh1_4 = biner(img4_grey)
ret, thresh2_4 = biner_inv(img4_grey)
ret, thresh3_4 = trunc(img4_grey)
ret, thresh4_4 = tozero(img4_grey)
ret, thresh5_4 = tozero_inv(img4_grey)

titles = [
    'Penguin Image', 'Penguin Binary', 'Penguin BinaryINV', 'Penguin Trunc', 'Penguin Tozero', 'Penguin TozeroINV',
    'Batu Image', 'Batu Binary', 'Batu BinaryINV', 'Batu Trunc', 'Batu Tozero', 'Batu TozeroINV',
    'Tulip Image', 'Tulip Binary', 'Tulip BinaryINV', 'Tulip Trunc', 'Tulip Tozero', 'Tulip TozeroINV',
    'Koala Image', 'Koala Binary', 'Koala BinaryINV', 'Koala Trunc', 'Koala Tozero', 'Koala TozeroINV'
]

images = [
    img1, thresh1_1, thresh2_1, thresh3_1, thresh4_1, thresh5_1,
    img2, thresh1_2, thresh2_2, thresh3_2, thresh4_2, thresh5_2,
    img3, thresh1_3, thresh2_3, thresh3_3, thresh4_3, thresh5_3,
    img4, thresh1_4, thresh2_4, thresh3_4, thresh4_4, thresh5_4
]

for i in xrange(24):
    plt.subplot(4, 6, i + 1), plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
