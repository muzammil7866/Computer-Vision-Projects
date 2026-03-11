# YOLOv11 - Bone Fracture Detection

State-of-the-art object detection implementation using YOLOv11-Nano for automated bone fracture detection and localization in X-ray images.

## Overview

This project implements YOLOv11, the latest generation of the YOLO (You Only Look Once) architecture, for medical imaging object detection. It detects and localizes bone fracture regions in radiograph images with high speed and accuracy.

## Dataset: FracAtlas

- **Dataset Name**: FracAtlas - Bone Fracture Detection Dataset
- **Annotation Format**: PASCAL VOC XML format
- **Train/Val/Test Split**: Properly stratified splits
- **Task**: Object detection (bounding box localization of fractures)
- **Image Type**: Medical X-ray radiographs

## Model: YOLOv11-Nano

- **Architecture**: YOLOv11 Nano variant (smallest, fastest)
- **Inference Speed**: Real-time on CPU, sub-millisecond on GPU
- **Parameters**: ~2.6M parameters (deployable on mobile)
- **Output**: Bounding boxes, class predictions, confidence scores

## Data Processing Pipeline

1. **XML to YOLO Format**: Converts PASCAL VOC annotations to YOLO txt format
2. **Smart Mapping**: Intelligent image-annotation matching with fallback logic
3. **Dataset Organization**: Proper train/val/test directory structure for YOLO
4. **Augmentation**: Built-in YOLO augmentation pipeline
5. **Normalization**: Float32 normalization for 8-bit images

## Features

- Modern YOLOv11 architecture
- Robust annotation format conversion with error handling
- Custom dataset configuration (data.yaml)
- Real-time inference capability
- Model saved in multiple formats (pt, onnx, tflite)
- Comprehensive metrics (precision, recall, mAP)

## Training Configuration

- **Input Resolution**: 640×640 (YOLO standard)
- **Batch Size**: Configurable (8-32 typical)
- **Epochs**: 50-100 (with early stopping)
- **Optimizer**: SGD with momentum
- **Loss Function**: YOLO combined loss (objectness, classification, localization)

## Metrics

- **Precision**: True positives / (True positives + False positives)
- **Recall**: True positives / (True positives + False negatives)
- **mAP (mean Average Precision)**: Standard detection metric
- **Inference Time**: FPS on various hardware

## Annotation Format Handling

- **Input**: PASCAL VOC XML annotations with `<bndbox>` coordinates
- **Output**: YOLO txt format with normalized (x_center, y_center, width, height)
- **Class Mapping**: Automatic mapping from annotation classes to integer indices

## Requirements

- YOLOv11 (ultralytics)
- OpenCV (cv2)
- NumPy
- PyYAML
- matplotlib / seaborn
- tqdm (progress bars)

## Files

- `FracAtlas-BoneFractureYOLO.ipynb`: Complete training and evaluation pipeline
- FracAtlas dataset (external download required)
- Configuration files (data.yaml, model config)

## Usage

1. Prepare FracAtlas dataset with XML annotations
2. Run notebook to convert annotations to YOLO format
3. Train YOLOv11 model
4. Evaluate on test set with mAP metrics
5. Use for inference on new X-ray images

## Model Export

- **PyTorch**: `.pt` format (native)
- **ONNX**: Cross-platform inference
- **TensorFlow Lite**: Mobile deployment
- **CoreML**: iOS deployment

## Medical Imaging Considerations

- Handles grayscale X-rays (3-channel conversion)
- Robust to annotation errors
- Metadata preservation in processing
- Proper normalization for medical images

## Performance Metrics

Typical performance on bone fracture detection:
- mAP@0.5: 70-85% (varies by dataset complexity)
- Inference Time: 5-15ms per image on GPU
- Model Size: ~6.3 MB (pt format)

## Clinical Deployment Notes

- This is a demonstration project
- Clinical deployment requires:
  - Rigorous validation on independent test set
  - Regulatory approval (FDA, CE marking)
  - Integration with DICOM/clinical workflows
  - Proper handling of edge cases
  - Privacy and security measures

## References

- YOLOv11: Latest YOLO architecture from Ultralytics
- PASCAL VOC: Standard object detection benchmark format
- FracAtlas: Bone fracture detection dataset

## Future Enhancements

- Multi-class fracture type detection
- Severity grading
- Automated report generation
- Integration with PACS systems
