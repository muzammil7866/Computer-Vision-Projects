# Simple CNN - Binary Animal Classification

A beginner-friendly convolutional neural network implementation for binary image classification of lions vs tigers using TensorFlow/Keras.

## Overview

This project demonstrates the fundamentals of building a CNN from scratch with basic architecture: convolutional layers, max-pooling, and dense layers. It's ideal for learning CNN concepts without relying on transfer learning.

## Architecture

- **Input**: 80×80 RGB images
- **Layers**: Conv2D → MaxPooling → Conv2D → MaxPooling → Flatten → Dense layers
- **Output**: Binary classification (lion or tiger)
- **Training**: 10 epochs with validation monitoring

## Features

- Simple, interpretable CNN architecture
- Confusion matrix visualization
- Training/validation accuracy tracking
- Data augmentation implementation
- Proper train/test split methodology

## Dataset

Binary classification between two animal classes:
- Lion images
- Tiger images

## Files

- `SimpleCNN-LionTigerClassification.ipynb`: Complete notebook with model implementation
- Training and evaluation code

## Requirements

- TensorFlow/Keras
- NumPy
- Matplotlib (visualization)
- scikit-learn (metrics)

## Usage

Run the notebook to train the model from scratch and evaluate on test data. The saved model can be used for inference on new images.

## Learning Objectives

This project is great for understanding:
- CNN layer operations and shapes
- How convolution extracts features
- Pooling for dimensionality reduction
- Training dynamics and overfitting patterns
