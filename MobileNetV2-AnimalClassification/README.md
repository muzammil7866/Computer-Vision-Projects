# MobileNetV2 - Multi-Class Animal Classification

Production-ready transfer learning implementation using MobileNetV2 pre-trained on ImageNet for multi-class animal classification.

## Overview

This project showcases transfer learning best practices using MobileNetV2, a lightweight deep learning model optimized for mobile and edge devices. The approach freezes the pre-trained base model and trains only a custom classification head.

## Architecture

- **Base Model**: MobileNetV2 (pre-trained on ImageNet, imagenet weights)
- **Input**: 224×224 RGB images
- **Feature Extraction**: Frozen MobileNetV2 layers (98 million+ parameters)
- **Custom Head**: Global average pooling → Dense(128) → Dropout → Dense(num_classes)
- **Output**: 4-class softmax classification

## Features

- Transfer learning with frozen base model (efficient training)
- Data augmentation (rotation, shift, zoom, flip) during training
- Dropout regularization to prevent overfitting
- Validation monitoring during training
- Class balance considerations
- 25 epochs training with early stopping potential

## Dataset

Multi-class animal classification:
- Cat
- Dog
- Lion
- Tiger

224×224 resolution images with proper train/validation/test split.

## Files

- `MobileNetV2-MultiClassAnimalClassifier.ipynb`: Complete notebook with training and evaluation

## Requirements

- TensorFlow/Keras
- NumPy
- Matplotlib (visualization)
- scikit-learn (metrics)

## Usage

1. Run the notebook to train the model
2. The model will be saved after training
3. Use for inference on new animal images

## Performance

- Leverages 1.4M parameters from pre-trained MobileNetV2
- Fast training on moderate hardware
- Excellent accuracy-efficiency trade-off
- Deployable on mobile devices

## Transfer Learning Workflow

This implementation demonstrates:
- Loading pre-trained weights
- Freezing base model layers
- Adding custom dense layers
- Training with validation monitoring
- Evaluating on test set
