# 🏀 AI-Powered Basketball Match Analysis System

### Robotics Club Summer Project | Computer Vision & Sports Analytics

## 🎥 Demo Video

[![Watch Demo](https://img.shields.io/badge/Watch-Demo%20Video-red?style=for-the-badge\&logo=google-drive)](https://drive.google.com/file/d/1y1imgGHqqAk9wsFZVhN0CWAGIfunT7ix/view?usp=drive_link)

**Demo Link:**
https://drive.google.com/file/d/1y1imgGHqqAk9wsFZVhN0CWAGIfunT7ix/view?usp=drive_link

> Watch the complete AI pipeline perform player detection, ball tracking, team assignment, possession analysis, and automated video annotation on real basketball footage.

---

# 📖 Introduction

The **AI Basketball Match Analysis System** is an end-to-end computer vision pipeline that automatically analyzes basketball match footage and extracts meaningful gameplay insights.

Traditional sports analytics systems often rely on expensive tracking hardware and proprietary software. This project demonstrates how modern AI and computer vision techniques can generate useful basketball analytics directly from video footage.

The system combines:

* Object Detection
* Multi-Object Tracking
* Team Classification
* Ball Possession Analysis
* Video Annotation

to transform raw basketball videos into structured analytical outputs.

---

# 🎯 Problem Statement

Basketball performance analysis is typically expensive, manual, and inaccessible to smaller teams, schools, and amateur players.

The objective of this project was to create an affordable AI-powered solution capable of:

* Detecting players and the basketball automatically
* Tracking player movement throughout a game
* Identifying teams based on jersey appearance
* Determining ball possession
* Generating an annotated output video without manual intervention

---

# ✨ Features

## 🏃 Player Detection

Detects basketball players using a custom-trained YOLO model.

## 🏀 Ball Detection

Uses a dedicated basketball detector trained specifically for fast-moving basketball footage.

## 🎯 Multi-Object Tracking

Maintains player identities across frames to track movement and gameplay behavior.

## 👕 Automatic Team Assignment

Uses Fashion-CLIP and visual feature extraction to classify players into teams based on jersey appearance.

## 🤝 Ball Possession Detection

Determines which player currently possesses the basketball using spatial analysis between players and the ball.

## 🎥 Automated Video Annotation

Generates a fully annotated output video containing:

* Player Bounding Boxes
* Tracking IDs
* Team Labels
* Ball Indicators

## ⚡ Stub-Based Development

Caches tracking outputs to speed up development and debugging without rerunning expensive detection models.

---

# 📊 Results

The system successfully performs:

✅ Player Detection using YOLO

✅ Basketball Detection using a custom-trained detector

✅ Multi-Object Tracking across video frames

✅ Automatic Team Classification using CLIP

✅ Ball Possession Estimation

✅ Annotated Video Generation

### Sample Analytics Generated

* Player trajectories
* Ball movement tracking
* Team classification
* Possession sequences
* Annotated gameplay footage

---

# 🧠 Technology Stack

## Programming

* Python

## Computer Vision

* OpenCV
* NumPy

## Deep Learning

* PyTorch
* Ultralytics YOLO

## Tracking

* Supervision Library
* ByteTrack-based Tracking Pipeline

## Classification

* Hugging Face Transformers
* Fashion-CLIP

## Dataset & Training

* Roboflow
* Google Colab

## Development Tools

* Git
* GitHub
* VS Code
* PyCharm

---

# ⚙️ System Pipeline

```text
Input Video
      │
      ▼
Player Detection (YOLO)
      │
      ▼
Ball Detection (YOLO)
      │
      ▼
Multi-Object Tracking
      │
      ▼
Team Assignment (Fashion-CLIP)
      │
      ▼
Ball Possession Detection
      │
      ▼
Video Annotation
      │
      ▼
Output Analytics Video
```

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/AKHIL-20243566/AI_BASKETBALL__ANALYSIS.git
cd AI_BASKETBALL__ANALYSIS
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment:

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 📦 Model Weights

Due to GitHub file size limitations, trained model weights are hosted externally.

Download the models and place them inside:

```text
models/
├── ball_detector_model.pt
└── player_detector_model.pt
```

### Ball Detector

https://drive.google.com/file/d/1KejdrcEnto2AKjdgdo1U1syr5gODp6EL/view

### Player Detector

https://drive.google.com/file/d/1fVBLZtPy9Yu6Tf186oS4siotkioHBLHy/view

---

# 🎓 Training the Models

Training notebooks used for experimentation and model development are included in:

```text
training_notebooks/
```

### Basketball Player Detection

* Dataset Preparation
* Data Augmentation
* YOLO Training
* Performance Evaluation

### Basketball Ball Detection

* Motion Blur Augmentation
* Fast-Moving Object Detection
* YOLO Fine-Tuning

Training was performed using Google Colab GPU environments.

---

# 🚀 Usage

Run the complete basketball analysis pipeline:

```bash
python main.py
```

The pipeline performs:

1. Video Loading
2. Player Detection
3. Ball Detection
4. Object Tracking
5. Team Assignment
6. Ball Possession Analysis
7. Video Annotation
8. Output Video Generation

Generated videos are saved in:

```text
output_videos/
```

---

# 🏗️ Project Structure

```text
AI_BASKETBALL__ANALYSIS/
│
├── input_videos/
├── output_videos/
│
├── models/
│
├── trackers/
├── team_assigner/
├── ball_acquisition/
├── drawers/
├── utils/
│
├── training_notebooks/
├── stubs/
│
├── main.py
└── README.md
```

---

# 🎓 What We Learned

This project provided hands-on experience in building a complete AI-powered computer vision system from data collection to deployment.

### Key Takeaways

* End-to-end Computer Vision Pipeline Design
* Training and Fine-Tuning YOLO Models
* Multi-Object Tracking Techniques
* Sports Analytics Applications
* Zero-Shot Image Classification
* Video Processing with OpenCV
* Large Project Debugging
* Team Collaboration in AI Projects
* Dataset Preparation and Evaluation

One of the biggest challenges was integrating multiple AI components into a single workflow while maintaining synchronization between detections, tracking IDs, team assignments, and possession analytics.

---

# 👨‍💻 Team Contributions

## Akhil Prakash

### Responsibilities

* End-to-end pipeline integration
* Detection and tracking workflow implementation
* Team assignment integration
* Ball possession analysis pipeline
* System debugging and testing
* Project architecture and repository management

### Challenges Faced

* Dependency conflicts involving PyTorch, NumPy, SciPy, and Ultralytics
* Integration of multiple AI modules into a single pipeline
* Tracking consistency across frames
* Managing cached tracking stubs during development
* Debugging model inference workflows

### Learnings

* Practical Computer Vision Engineering
* AI Pipeline Design
* Multi-Object Tracking Systems
* Real-world debugging and deployment workflows

---

## Anshika Sharma

### Responsibilities

* Dataset preparation
* Data cleaning and validation
* Model experimentation
* Training support

### Challenges Faced

* Data quality and annotation consistency
* Training parameter optimization
* Performance evaluation

### Learnings

* Dataset engineering
* Deep learning experimentation
* Model validation techniques

---

## Pragya Agarwal

### Responsibilities

* Research and analytics workflow
* Testing and validation
* Documentation support
* Project evaluation

### Challenges Faced

* Coordinating project modules
* Understanding end-to-end workflow interactions
* Validating analytical outputs

### Learnings

* AI project lifecycle
* Computer vision applications
* Collaborative software development

---

# 🔮 Future Improvements

Several enhancements can make the system significantly more powerful:

### Gameplay Analytics

* Shot Detection
* Pass Detection
* Turnover Analysis
* Assist Tracking
* Rebound Tracking

### Advanced Player Analytics

* Speed Estimation
* Distance Covered
* Movement Heatmaps
* Player Efficiency Metrics

### Tactical Analysis

* Team Formation Detection
* Offensive and Defensive Pattern Recognition
* Top-Down Court Visualization

### System Improvements

* Real-Time Live Match Processing
* Interactive Web Dashboard
* Cloud Deployment
* API Integration
* Automated Report Generation

---

# 🏆 Project Highlights

* Presented at **Sankalp**, the annual Robotics Club event at MNNIT Allahabad.
* Demonstrates the practical application of AI in sports analytics.
* Integrates deep learning, tracking, classification, and video processing into a single system.
* Showcases real-world software engineering, debugging, and teamwork experience.

---

# 👥 Team Members

* Akhil Prakash
* Anshika Sharma
* Pragya Agarwal

**Robotics Club Summer Project**
**Motilal Nehru National Institute of Technology Allahabad**
