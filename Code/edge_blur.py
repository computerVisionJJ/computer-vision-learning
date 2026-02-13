import cv2

img = cv2.imread("images/test.jpg")

if img is None:
    raise ValueError("Image failed to load. Check file path.")

# Blur (reduce noise)
blur = cv2.GaussianBlur(img, (7, 7), 0)

# Edge detection
edges = cv2.Canny(blur, 50, 150)

cv2.imshow("Original", img)
cv2.imshow("Blur", blur)
cv2.imshow("Edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()