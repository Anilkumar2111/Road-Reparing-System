from ultralytics import YOLO

# Load your trained model
model = YOLO("runs/detect/train-3/weights/best.pt")

# Run detection on images
results = model("data/dataset1/valid/images", show=True)

# Save results
for r in results:
    r.save()