import cv2
from ultralytics import YOLO
import time
import pygame  # For playing alert sound

# Load YOLOv8 model
model = YOLO(r"C:\Users\kovvu\OneDrive\Desktop\project\fire\best.pt")  # Replace with your model path

# Initialize webcam
cap = cv2.VideoCapture(0)

# Initialize pygame mixer
pygame.mixer.init()
pygame.mixer.music.load(r"C:\Users\kovvu\OneDrive\Desktop\project\fire\fire-alarm-33770_OyJkH2cA.mp3")  # Replace with your alert sound

fire_detected = False

print("🔥 Real-time Forest Fire Detection Started...")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run detection
    results = model(frame)[0]

    # Plot detections
    annotated_frame = results.plot()

    # Check for fire (any detection with confidence > 0.5)
    fire_now = any(float(box.conf[0]) > 0.75 for box in results.boxes)

    # Play alert sound only when fire is detected
    if fire_now and not fire_detected:
        print("🚨 Fire Detected! Playing alert...")
        pygame.mixer.music.play()
        fire_detected = True
    elif not fire_now:
        fire_detected = False
        pygame.mixer.music.stop()

    # Add visual alert
    if fire_now:
        cv2.putText(annotated_frame, "FIRE DETECTED!", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

    # Show output
    cv2.imshow("Forest Fire Detection", annotated_frame)

    # Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
