from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # small, fast model

results = model("images/test.jpg", save=True)

print("Detection complete.")
