# nsfw-screen-guardian
> An AI-powered real-time NSFW content detection system that monitors the user’s screen using a mss and prevents exposure to inappropriate content by locking the device.
> https://youtu.be/qCTQZGpU8Mo

## 🚀 Features

- 🔍 Screen monitoring via mms library
- 🧠 Trained CNN model (ResNet) to classify NSFW content
- ⛔ Automatic response upon detection 
- 📊 Model accuracy reporting and easy retraining with your dataset
- 🔐 Supports adding parental controls or productivity blockers

## 📦 Tech Stack

- Python 🐍
- PyTorch / FastAI 🧠
- OpenCV 📷
- PIL 🖼️
- Torchvision 📦

## 📁 Dataset

This project uses a labeled dataset of images for training NSFW vs Safe classifiers.
You can replace it with your own by placing it in `nsfw_dataset_v1/` and using appropriate class folders like:
nsfw_dataset_v1/
├── porn/
├── neutral/

## 🏁 Getting Started

```bash
git clone https://github.com/yourusername/screen-sentinel.git
cd screen-sentinel
pip install -r requirements.txt
python train.py
python run_detector.py
