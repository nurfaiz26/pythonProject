import cv2
import numpy as np

img = cv2.imread("../datasets/jambu.jpg")

print("Ukuran Image ", img.shape)

height, width = img.shape[0], img.shape[1]

print("Tipe data ", img.dtype)

cv2.imshow("Image Original", img)

print(img[136, 413])

new_img = np.zeros((height, width, 3), np.uint8)
new_img = img.copy()
new_img[136:146, 413:423] = (0, 255, 0)

cv2.imshow("Image Set Piksel", new_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
