from ultralytics import YOLO

# Load base model (auto-download)
model = YOLO("yolov8n.pt")

# Train model
model.train(
    data="data/dataset1/data.yaml",
    epochs=10,
    imgsz=640
)