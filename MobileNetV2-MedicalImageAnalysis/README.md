# MobileNetV2 - Medical Image Analysis (MURA X-ray Classification)

Production-ready deep learning pipeline for binary classification of musculoskeletal radiographs (X-rays) as normal or abnormal using MobileNetV2 transfer learning.

## Overview

This project addresses a critical medical imaging challenge: automated classification of X-ray images to identify musculoskeletal abnormalities. It integrates proper data validation, cleaning, and medical imaging best practices with transfer learning.

## Dataset: MURA-v1.1

- **MURA**: Musculoskeletal Radiographs (X-ray images)
- **Source**: Stanford Multi-Modality Annotated Medical Imaging Database
- **Binary Classes**: Normal vs Abnormal X-rays
- **Image Type**: Grayscale radiographs converted to RGB for MobileNetV2 compatibility

## Data Processing Pipeline

1. **Data Validation**: Identifies and removes corrupted image files
2. **Train/Val/Test Split**: 80% / 10% / 10% stratified split
3. **Image Preprocessing**: Resize to 224×224, normalize to ImageNet mean/std
4. **Data Augmentation**: Rotation, zoom, brightness, contrast adjustments
5. **Class Imbalance Handling**: Proper weighting if needed

## Model Architecture

- **Base Model**: MobileNetV2 pre-trained on ImageNet
- **Transfer Learning**: Frozen base with custom dense head
- **Custom Head**: Global Average Pooling → Dense(128) → Dropout(0.5) → Dense(1, sigmoid)
- **Binary Classification**: Normal vs Abnormal

## Features

- Robust image validation (removes corrupted files)
- Proper dataset stratification
- Comprehensive data augmentation
- ROC curve analysis
- Confusion matrix and classification metrics
- Production-ready error handling

## Metrics

- Accuracy: Classification accuracy on test set
- ROC-AUC: Area under receiver operating characteristic curve
- Specificity & Sensitivity: Critical for medical imaging
- Confusion Matrix: TN, FP, FN, TP analysis

## Requirements

- TensorFlow/Keras
- NumPy
- Matplotlib / Seaborn
- scikit-learn
- PIL/Pillow (image processing)

## Files

- `MURA-MedicalImageClassification.ipynb`: Complete pipeline
- MURA-v1.1 dataset (external download required)

## Medical Imaging Best Practices

✓ Data validation before preprocessing  
✓ Proper train/val/test stratification  
✓ Appropriate metrics (ROC-AUC, sensitivity, specificity)  
✓ Data augmentation for robustness  
✓ Class imbalance handling  
✓ Clear documentation of pipeline  

## Dataset Citation

**Rajpurkar et al.**, MURA: Large Benchmark for Abnormality Detection in Musculoskeletal Radiographs. *arXiv:1712.06957*, 2017.

## Usage

1. Download MURA-v1.1 dataset from Stanford
2. Run notebook to validate data, train model, evaluate
3. Model can be exported for deployment

## Notes

- Medical AI applications require regulatory considerations
- This is a demonstration project
- Real clinical deployment requires clinical validation
- Appropriate data anonymization required for protected health information
