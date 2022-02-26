import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from urllib3.connectionpool import xrange

img = mpimg.imread("../datasets/jambu.jpg")

B, G, R = cv2.split(img)

titles = [
    'Original Image',
    'Channel B',
    'Channel G',
    'Channel R'
]

images = [
    img,
    R,
    G,
    B
]

for i in xrange(4):
    plt.subplot(2, 2, i+1), plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()