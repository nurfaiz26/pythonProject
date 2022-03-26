import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread("../datasets/jambu.jpg")

print("Ukuran Image ", img.shape)

height, width = img.shape[0], img.shape[1]

print("Tipe data ", img.dtype)

# plt.imshow(img)

print(img[136, 413])

fig = plt.figure()

new_img1 = np.zeros((height, width, 3), np.uint8)
new_img1 = img.copy()
new_img1[136:146, 413:423] = (0, 255, 0)

ax = fig.add_subplot(2, 2, 1)
plt.imshow(new_img1)
ax.set_title("Gambar Original")

new_img2 = np.zeros((height, width, 3), np.uint8)
new_img3 = np.zeros((height, width, 3), np.uint8)
new_img4 = np.zeros((height, width, 3), np.uint8)

new_img1=cv2.cvtColor(new_img1, cv2.COLOR_BGR2RGB)

# copy image
for i in range(height):
    for j in range(width):
        for k in range(3):
            new_img2[i, j][k] = img[i, j][k]

ax = fig.add_subplot(2, 2, 2)
plt.imshow(new_img2)
ax.set_title("Gambar Copy")

new_img2=cv2.cvtColor(new_img1, cv2.COLOR_BGR2RGB)

# flip horizontal
for i in range(height):
    for j in range(width):
        for k in range(3):
            new_img3[i, j][k] = img[height-1-i, j][k]

# flip vertikal
for i in range(height):
    for j in range(width):
        for k in range(3):
            new_img4[i, j][k] = img[i, width-1-j][k]

ax = fig.add_subplot(2, 2, 3)
plt.imshow(new_img3)
ax.set_title("Flip Horizontal")
ax = fig.add_subplot(2, 2, 4)
plt.imshow(new_img4)
ax.set_title("Flip Vertikal")

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()