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
   git clone https://github.com/yourusername/ai_powered_robotic_arm.git
   cd ai_powered_robotic_arm
   ```
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Upload the Arduino motor control script (`src/control/motor_control.ino`) to your Arduino board.

4. Run the main program:
   ```bash
   python src/main.py
   ```

## Repository Structure
- `src/`: Core code for vision and control systems.
- `datasets/`: Training datasets and annotations for object detection.
- `models/`: Pre-trained YOLOv4 model weights.
- `results/`: Output metrics, visualizations, and demo videos.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
