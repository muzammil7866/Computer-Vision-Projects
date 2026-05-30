# LT10 — Face Detection and Recognition with Haar Cascade and LBPH

**Course:** AI4002 — Computer Vision Lab  
**Institution:** National University of Computer and Emerging Sciences, Chiniot-Faisalabad Campus  
**Department:** Artificial Intelligence and Data Science

## Overview

This lab implements a real-time face registration and recognition system. Five photos per person are uploaded, faces are detected using the Haar Cascade frontal face classifier, and an LBPH (Local Binary Pattern Histogram) face recognizer is trained on the detected regions. The trained model is then tested on a live image to identify which registered person appears.

## Topics Covered

- Haar Cascade Classifier face detection with `cv2.CascadeClassifier` and `haarcascade_frontalface_default.xml`
- Image collection and labeling for two subjects
- LBPH face recognizer training with `cv2.face.LBPHFaceRecognizer_create()`
- Model serialization and loading (`.yml` format)
- Face recognition with confidence scoring on test images
- Google Colab file upload workflow

## Technologies Used

- Python
- OpenCV (`cv2`, `opencv-contrib-python`)
- NumPy
- PIL / Pillow
- Google Colab (`files.upload()`)

## Requirements

```
opencv-contrib-python
numpy
Pillow
```

> **Note:** `opencv-contrib-python` (not the standard `opencv-python`) is required for `cv2.face.LBPHFaceRecognizer_create()`.

## Tasks

| Question | Description |
|----------|-------------|
| Q1 | Collect 5 photos each for two people; detect faces via Haar Cascade; train LBPH recognizer; save model; test recognition on a new image |
