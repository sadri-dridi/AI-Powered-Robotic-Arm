import cv2
import torch
from yolo_config import load_yolo_model

class ObjectDetection:
    def __init__(self, model_path):
        self.model = load_yolo_model(model_path)

    def detect_objects(self, frame):
        detections = self.model.predict(frame)
        for det in detections:
            label, confidence, bbox = det
            x, y, w, h = bbox
            cv2.rectangle(frame, (x, y), (0, 255, 0), 2)
            cv2.putText(frame, f"{label} {confidence:.2f}", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        return frame
