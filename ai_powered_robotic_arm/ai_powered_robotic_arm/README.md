# AI-Powered Robotic Arm

This project demonstrates an AI-powered robotic arm that autonomously performs high-precision object sorting and assembly tasks.

## Features
- Real-time object detection with YOLOv4.
- Accurate trajectory planning for smooth arm movements.
- Integrated motor control for precise actuation.

## How to Use
1. Install dependencies using `pip install -r requirements.txt`.
2. Upload `motor_control.ino` to Arduino.
3. Run `main.py` to start the robotic arm system.

## Structure
- `datasets/`: Training data and annotations.
- `src/`: Source code for vision and control systems.
- `models/`: Pre-trained YOLOv4 weights.
- `results/`: Output metrics, visuals, and demos.

## License
MIT License.
