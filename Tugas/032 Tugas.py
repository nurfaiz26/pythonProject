import  cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from urllib3.connectionpool import xrange

img1 = mpimg.imread("../datasets/penguin.jpg")
img2 = mpimg.imread("../datasets/batu.jpg")
img3 = mpimg.imread("../datasets/tulip.jpg")
img4 = mpimg.imread("../datasets/koala.jpg")

def b_rgb(img_src):
    b = img_src.copy()
    b[:, :, 1] = 0
    b[:, :, 2] = 0
    return b

def g_rgb(img_src):
    g = img_src.copy()
    g[:, :, 0] = 0
    g[:, :, 2] = 0
    return g

def r_rgb(img_src):
    r = img_src.copy()
    r[:, :, 0] = 0
    r[:, :, 1] = 0
    return r

# penguin
b1 = b_rgb(img1)
g1 = g_rgb(img1)
r1 = r_rgb(img1)

# batu
b2 = b_rgb(img2)
g2 = g_rgb(img2)
r2 = r_rgb(img2)

# tulip
b3 = b_rgb(img3)
g3 = g_rgb(img3)
r3 = r_rgb(img3)

# koala
b4 = b_rgb(img4)
g4 = g_rgb(img4)
r4 = r_rgb(img4)

titles = [
    'Penguin Image', 'Penguin B-RGB', 'Penguin G-RGB', ' Penguin R-RGB',
    'Batu Image', 'Batu B-RGB', 'Batu G-RGB', ' Batu R-RGB',
    'Tulip Image', 'Tulip B-RGB', 'Tulip G-RGB', ' Tulip R-RGB',
    'Koala Image', 'Koala B-RGB', 'Koala G-RGB', ' Koala R-RGB'
]

images = [
    img1, r1, g1, b1,
    img2, r2, g2, b2,
    img3, r3, g3, b3,
    img4, r4, g4, b4
]

for i in xrange(16):
    plt.subplot(4, 4, i+1), plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()