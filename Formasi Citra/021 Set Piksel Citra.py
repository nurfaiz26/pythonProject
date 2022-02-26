import cv2

img = cv2.imread("../datasets/hagiasophia.jpg")

print("Ukuran Image ", img.shape)
print("Tipe data ", img.dtype)

cv2.imshow("Image Original", img)

print(img[136, 413])

cv2.waitKey(0)
cv2.destroyAllWindows()
