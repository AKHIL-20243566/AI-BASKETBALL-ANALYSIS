# 🏀 AI-Powered Basketball Match Analysis System  
### Robotics Club Summer Project

An automated computer vision pipeline that analyzes basketball match footage and extracts tactical and gameplay insights using deep learning.

This project was developed as part of the **Robotics Club Summer Project** and demonstrates how basketball analytics can be generated directly from video footage using machine learning.

---

# 📁 Table of Contents

- Introduction  
- Features  
- Technology Stack  
- Installation  
- Pretrained Models  
- Training the Models  
- Usage  
- Project Structure  
- Future Work  
- Contributors  

---

# 📖 Introduction

The **AI Basketball Match Analysis System** is an end-to-end computer vision pipeline designed to analyze basketball match videos and extract structured analytics.

Traditional sports analytics systems rely on expensive motion tracking hardware and proprietary software. This project demonstrates that meaningful basketball insights can be generated directly from broadcast footage using modern computer vision techniques.

The system combines:

- Object Detection  
- Multi-Object Tracking  
- Zero-Shot Classification  
- Ball Possession Analysis  
- Video Annotation  

to automatically analyze gameplay.

---

# ✨ Features

### Player and Ball Detection
Detects basketball players and the ball using trained **YOLO models**.

### Multi-Object Tracking
Tracks players and the ball across frames to understand movement patterns.

### Automatic Team Assignment
Uses **zero-shot classification** to group players by jersey color.

### Ball Possession Detection
Determines which player currently controls the ball.

### Video Annotation
Draws bounding boxes, ball pointers, player IDs, and team labels directly on frames.

### Fast Development with Stubs
Intermediate results can be cached to avoid recomputing detections during development.

---

# 🧠 Technology Stack

- Python
- Ultralytics YOLO (v5 / v8)
- OpenCV
- NumPy
- Roboflow
- Hugging Face Transformers (CLIP)

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/AKHIL-20243566/AI_BASKETBALL__ANALYSIS.git
cd AI_BASKETBALL__ANALYSIS
```

Create a virtual environment (recommended):

```bash
python -m venv .venv
```

Activate the environment:

**Windows**

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 📦 Pretrained Models

Due to GitHub file size limitations, trained model weights are hosted externally.

Download the models and place them inside the **models/** folder.

### Ball Detector
https://drive.google.com/file/d/1KejdrcEnto2AKjdgdo1U1syr5gODp6EL/view

### Player Detector
https://drive.google.com/file/d/1fVBLZtPy9Yu6Tf186oS4siotkioHBLHy/view

After downloading, place them here:

```
models/
├── ball_detector_model.pt
└── player_detector_model.pt
```

---

# 🎓 Training the Models

This repository contains notebooks used to train the detection models.

Location:

```
training_notebooks/
```

### Basketball Ball Detection

```
basketball_ball_training.ipynb
```

Trains a YOLO model to detect basketballs in game footage.

Includes motion blur augmentation to improve detection on fast moving balls.

### Player Detection

```
basketball_player_detection_training.ipynb
```

Trains a YOLO model to detect players across video frames.

Training can be performed using **Google Colab or any GPU environment**.

---

# 🚀 Usage

Run the full basketball analysis pipeline with:

```bash
python main.py
```

The pipeline performs:

1. Video loading  
2. Player detection  
3. Ball detection  
4. Object tracking  
5. Team assignment  
6. Ball possession detection  
7. Video annotation  
8. Export annotated video  

Output videos are saved to:

```
output_videos/
```

---

# 🏗 Project Structure

```
AI_BASKETBALL__ANALYSIS/
│
├── input_videos/          # Input basketball videos
├── output_videos/         # Generated annotated videos
│
├── models/                # YOLO detection models
│
├── trackers/              # Player and ball tracking
├── team_assigner/         # Jersey color based team classification
├── ball_acquisition/      # Ball possession detection logic
├── drawers/               # Visualization utilities
├── utils/                 # Helper functions
│
├── training_notebooks/    # Model training notebooks
│
├── main.py                # Main pipeline script
└── README.md
```

---

# 🔮 Future Work

Future improvements planned for the project include:

- Player **speed and distance estimation**
- Player **movement heatmaps**
- Advanced **pass and interception detection**
- Tactical **top-down court visualization**
- Web-based **interactive analytics dashboard**

---

# 👨‍💻 Contributors

Robotics Club Summer Project

**Akhil Prakash**  
**Anshika Sharma**  
**Pragya Agarwal**
