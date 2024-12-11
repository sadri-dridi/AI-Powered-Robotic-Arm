from yolov4.model import YOLOv4

def load_yolo_model(weights_path):
    model = YOLOv4()
    model.load_model(weights_path)
    return model
