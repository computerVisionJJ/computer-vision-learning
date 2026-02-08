import cv2

img = cv2.imread("images/test.jpg")

if img is None:
    raise ValueError("Image failed to load. Check file path.")

resized = cv2.resize(img, (640, 480))

cv2.imwrite("outputs/test_resized.jpg", resized)

cv2.imshow("Resized", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
