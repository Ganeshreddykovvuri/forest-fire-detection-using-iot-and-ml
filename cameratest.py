import cv2

# Open the camera using the correct device path
cap = cv2.VideoCapture(0)  # Try /dev/video1 if /dev/video0 doesn't work

if not cap.isOpened():
    print("Error: Camera not detected!")
else:
    print("Camera opened successfully.")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Camera Feed", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
