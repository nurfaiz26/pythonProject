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

ax = fig.add_subplot(2, 3, 1)
plt.imshow(new_img1)
ax.set_title("Gambar Original")

new_img2 = np.zeros((height, width, 3), np.uint8)
new_img3 = np.zeros((height, width, 3), np.uint8)
new_img4 = np.zeros((height, width, 3), np.uint8)
new_img5 = np.zeros((height, width, 3), np.uint8)
new_img6 = np.zeros((height, width, 3), np.uint8)

new_img1=cv2.cvtColor(new_img1, cv2.COLOR_BGR2RGB)

# copy image
for i in range(height):
    for j in range(width):
        for k in range(3):
            new_img2[i, j][k] = img[i, j][k]

ax = fig.add_subplot(2, 3, 2)
plt.imshow(new_img2)
ax.set_title("Gambar Copy")

new_img2=cv2.cvtColor(new_img1, cv2.COLOR_BGR2RGB)

# cv2 rotate 90 clockwise
new_img3 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# cv2 rotate 90 counter clockwise
new_img4 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

# cv2 get rotation matrix 2D
new_img5 = cv2.getRotationMatrix2D((0, 0), 45, 1.0)

# cv2 warp affine
new_img6 = cv2.warpAffine(img, new_img5, (width, height))

ax = fig.add_subplot(2, 3, 3)
plt.imshow(new_img3)
ax.set_title("cv2 rotate 90 clockwise")
ax = fig.add_subplot(2, 3, 4)
plt.imshow(new_img4)
ax.set_title("cv2 rotate 90 counter clockwise")
ax = fig.add_subplot(2, 3, 6)
plt.imshow(new_img6)
ax.set_title("cv2 get rotation matrix 2D dan cv2 warp affine")

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()