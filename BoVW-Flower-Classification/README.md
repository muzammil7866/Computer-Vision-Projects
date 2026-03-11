# Bag of Visual Words Flower Classification

A classical computer vision machine learning pipeline implementing image classification using SIFT features, k-means clustering codebook, and Support Vector Machine classifier.

## Overview

This project demonstrates the complete Bag of Visual Words (BoVW) pipeline for flower species classification. It's a foundational computer vision approach that bridges low-level feature extraction with machine learning.

## Features

- **SIFT Feature Extraction**: Detects and computes Scale-Invariant Feature Transform descriptors
- **K-Means Clustering**: Builds a visual vocabulary (codebook) with 120 clusters from SIFT descriptors
- **BoVW Histogram**: Converts raw SIFT features to fixed-size histograms for ML model input
- **Linear SVM Classifier**: Trains a Support Vector Machine for multi-class classification
- **Fallback ORB**: Gracefully falls back to ORB features if SIFT is unavailable

## Dataset

- **Classes**: 5 flower species (daisy, dandelion, roses, sunflowers, tulips)
- **Train/Test Split**: Organized in separate Train/ and Test/ directories
- **Pre-trained Models**: Includes serialized joblib models (kmeans codebook and SVM classifier)

## Files

- `FlowerClassification-BoVW.ipynb`: Main notebook with complete pipeline
- `Train/`: Training images organized by class
- `Test/`: Test images for evaluation
- `bovw_kmeans.joblib`: Pre-trained k-means codebook
- `bovw_svm.joblib`: Pre-trained SVM classifier
- `label_encoder.joblib`: Label encoding for class names

## Usage

Run the Jupyter notebook to train the model or use pre-trained models for inference.

## Requirements

- OpenCV (cv2)
- scikit-learn
- NumPy
- joblib

## Performance

The model achieves competitive accuracy on the flower classification task using classical computer vision techniques without deep learning.
