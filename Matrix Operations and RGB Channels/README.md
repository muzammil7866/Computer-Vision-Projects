# Lab 01: Image Processing Basics

This project demonstrates fundamental computer vision and image processing techniques using Python, OpenCV, and Matplotlib.

## Overview

The lab covers the following concepts:
- **Matrix Operations**: Custom implementation of matrix transformations (e.g., modifying elements based on even/odd parity).
- **Color Space Conversions**: Converting images between BGR (OpenCV default) and RGB/GBR formats.
- **Image Visualization**: Displaying images using Matplotlib.

## Project Structure

- `matrix_operations.py`: a script performing element-wise operations on a sample 3x3 matrix.
- `color_schemes.py`: A script that loads an image, manipulates its color channels (BGR to GBR), and visualizes the results.
- `image.jpg`: Sample input image used for the transformations.
- `requirements.txt`: List of Python dependencies.

## Installation

1. Clone the repository and navigate to this folder:
   ```bash
   cd Lab01_Image_Processing_Basics
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Run Matrix Operations
```bash
python matrix_operations.py
```

### Run Color Scheme Transformations
```bash
python color_schemes.py
```
*Note: This will open a window showing the original and transformed images.*
