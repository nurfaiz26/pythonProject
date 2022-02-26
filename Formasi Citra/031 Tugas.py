import  cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from urllib3.connectionpool import xrange

img1 = mpimg.imread("../datasets/penguin.jpg")
img2 = mpimg.imread("../datasets/batu.jpg")
img3 = mpimg.imread("../datasets/tulip.jpg")
img4 = mpimg.imread("../datasets/koala.jpg")

def sepia(img_src):
    b = img_src[:, :, 0]
    g = img_src[:, :, 1]
    r = img_src[:, :, 2]
    rnew = (b + g + r)/3
    img_src[:, :, 0] = 2 * rnew
    img_src[:, :, 1] = 1.8 * rnew
    img_src[:, :, 2] = rnew
    return img_src

# penugin
img1 = sepia(img1)

# batu
img2 = sepia(img2)

# tulip
img3 = sepia(img3)

# koala
img4 = sepia(img4)

titles = [
    'Penguin Sepia',
    'Batu Sepia',
    'Tulip Sepia',
    'Koala Sepia'
]

images = [
    img1,
    img2,
    img3,
    img4,
]

for i in xrange(4):
    plt.subplot(2, 2, i+1), plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()