import cv2
from vision.object_detection import ObjectDetection
import serial
from control.trajectory_planning import cubic_spline

# Initialize vision and serial communication
detector = ObjectDetection("models/yolov4_weights.pth")
arduino = serial.Serial('/dev/ttyUSB0', 9600)

# Capture video
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detect objects
    frame = detector.detect_objects(frame)

    # Simulate motor command
    motor_command = cubic_spline(0, 200, num_points=1)
    arduino.write(str(int(motor_command[0])).encode())

    cv2.imshow("AI-Powered Robotic Arm", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
