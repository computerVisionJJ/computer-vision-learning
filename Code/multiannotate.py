import cv2

img = cv2.imread("images/test.jpg")

if img is None:
    raise ValueError("Image failed to load. Check file path.")

# Fake YOLO-style detections: (x1, y1, x2, y2, label, confidence)
detections = [
    (50, 50, 200, 200, "Person", 0.87),
    (220, 80, 380, 260, "Dog", 0.74),
    (100, 220, 260, 380, "Bag", 0.65)
]

for x1, y1, x2, y2, label, conf in detections:
    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    text = f"{label} {int(conf*100)}%"
    cv2.putText(img, text, (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

cv2.imshow("Multiple Detections", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("outputs/test_multi_annotated.jpg", img)
