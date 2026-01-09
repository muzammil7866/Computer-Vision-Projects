# Image Processing Fundamentals

This repository contains solution files for Computer Vision Assignment 1, extracted from the original Jupyter Notebook.

## Tasks Overview

### 1. Binary Thresholding (`binary_thresholding.py`)
Explores how different threshold values affect binary image conversion.
- **Lower threshold**: Results in brighter images with larger white regions.
- **Higher threshold**: Results in darker images with fewer white regions.

### 2. Contrast Enhancement (`contrast_enhancement.py`)
Compare Power-law transformation, Contrast Stretching, and Histogram Equalization.
- **Power-law (gamma < 1)**: Brightens dark pixels.
- **Contrast Stretching**: Linear rescaling of intensity values.
- **Histogram Equalization**: Non-linear redistribution of intensities for uniform histogram.

### 3. Edge Detection Basics (`edge_detection_basics.py`)
Comparison between Finite Difference and Sobel methods.
- **Finite Difference**: Simple subtraction, sensitive to noise.
- **Sobel**: Uses 3x3 kernel with smoothing, better noise resistance and edge localization.

### 4. Noise Removal (`noise_removal.py`)
Implementation and comparison of Mean and Gaussian filters.
- **Gaussian Filter**: Preserves edges better by weighting center pixels more.
- **Mean Filter**: Averaging filter, tends to blur edges more.

### 5. Sobel Edge Detection (`sobel_edge_detection.py`)
Manual implementation of Sobel filters to calculate gradient magnitude and direction.
- compares results with Finite Difference method.

### 6. Canny Edge Detection (`canny_edge_detection.py`)
Step-by-step implementation of Canny Edge Detector:
1.  Gaussian Smoothing
2.  Gradient Magnitude & Direction (Sobel)
3.  Non-Maximum Suppression
4.  Double Thresholding + Hysteresis

## Usage
Each file is valid Python code extracted from the notebook. Ensure you have the necessary libraries installed (e.g., `opencv-python`, `numpy`, `matplotlib`).

```bash
pip install opencv-python numpy matplotlib
```

Run specific tasks:
```bash
python binary_thresholding.py
```
