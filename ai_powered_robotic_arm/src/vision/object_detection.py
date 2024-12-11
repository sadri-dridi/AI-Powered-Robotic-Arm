import cv2
import torch
from yolo_config import YOLOv4

class ObjectDetection:
    def __init__(self, model_path):
        self.model = YOLOv4()
        self.model.load_model(model_path)

    def detect_objects(self, frame):
        detections = self.model.predict(frame)
        for det in detections:
            label, confidence, bbox = det
            x, y, w, h = bbox
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, f"{label} {confidence:.2f}", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        return frame
