# LT08 — SIFT Feature Descriptor Extraction

**Course:** AI4002 — Computer Vision Lab  
**Institution:** National University of Computer and Emerging Sciences, Chiniot-Faisalabad Campus  
**Department:** Artificial Intelligence and Data Science

## Overview

This lab implements the SIFT (Scale-Invariant Feature Transform) descriptor extraction algorithm from scratch. Given pre-computed image gradients and a single interest point, the code manually constructs a 128-dimensional feature descriptor by dividing a 16×16 window around the point into 4×4 sub-blocks and building an 8-bin gradient orientation histogram for each block.

## Topics Covered

- SIFT descriptor geometry: 16×16 window, 4×4 sub-blocks, 8 orientation bins
- Gradient magnitude and orientation computation from `Gx`, `Gy`
- Histogram of Oriented Gradients (HOG) construction per sub-block
- Concatenation of 16 histograms into a 128-dimensional descriptor vector
- Validation and boundary-check handling for interest points near image borders

## Technologies Used

- Python
- OpenCV (`cv2`)
- NumPy
- Matplotlib

## Requirements

```
opencv-python
numpy
matplotlib
```

## Tasks

| Question | Description |
|----------|-------------|
| Q1 | Implement `compute_descriptor(Gx, Gy, x, y)` that extracts a 128-dim SIFT descriptor around a given interest point using manual HOG block construction |
