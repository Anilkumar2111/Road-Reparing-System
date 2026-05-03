from ultralytics import YOLO
import cv2

# Load trained model
model = YOLO("runs/detect/train-3/weights/best.pt")

# Start webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print(" Camera not working")
    exit()

print("🎥 Camera Started... Press ESC to exit")

while True:
    ret, frame = cap.read()
    
    if not ret:
        print(" Failed to grab frame")
        break

    # YOLO detection
    results = model(frame)

    # Draw boxes
    annotated_frame = results[0].plot()

    # Show output
    cv2.imshow("🚧 AI Road Detection", annotated_frame)

    # Exit on ESC
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()