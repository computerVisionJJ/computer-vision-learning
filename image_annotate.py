import cv2

# Load the image
img = cv2.imread("images/test.jpg")

# Validate image loaded
if img is None:
    raise ValueError("Image failed to load. Check file path.")

# Draw a rectangle (bounding box)
# Arguments: image, top-left corner, bottom-right corner, color (B,G,R), thickness
cv2.rectangle(img, (50, 50), (300, 300), (0, 255, 0), 2)

# Add text label
# Arguments: image, text, position, font, font scale, color, thickness
cv2.putText(img, "Object", (50, 45), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

# Show the image
cv2.imshow("Annotated", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save annotated image.111
cv2.imwrite("outputs/test_annotated.jpg", img)
