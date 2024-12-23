# AI-Powered-Robotic-Arm
# AI-Powered Robotic Arm

This project showcases an AI-powered robotic arm capable of sorting objects and performing basic assembly tasks. It integrates computer vision, trajectory optimization, and motor control for high-precision autonomous operations.

## Features
- Object detection and classification using YOLOv4.
- Real-time motor control for robotic arm movements.
- High-accuracy sorting and assembly tasks.

## System Requirements
- Python 3.8+
- Arduino Uno
- Stepper motors with encoders
- RGB camera
- OpenCV, PyTorch, and Arduino IDE

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/sadri-dridi/ai_powered_robotic_arm.git
   cd ai_powered_robotic_arm
Install Python dependencies:

bash
Copy code
pip install -r requirements.txt
Upload the Arduino motor control script (src/control/motor_control.ino) to your Arduino board.

Run the main program:

bash
Copy code
python src/main.py
Repository Structure
src/: Core code for vision and control systems.
datasets/: Training datasets and annotations for object detection.
models/: Pre-trained YOLOv4 model weights.
results/: Output metrics, visualizations, and demo videos.
