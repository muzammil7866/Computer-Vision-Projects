# LT04 — Difference of Gaussian and Laplacian of Gaussian

**Course:** AI4002 — Computer Vision Lab  
**Institution:** National University of Computer and Emerging Sciences, Chiniot-Faisalabad Campus  
**Department:** Artificial Intelligence and Data Science

## Overview

This lab implements two classical edge and feature enhancement operators — Difference of Gaussian (DoG) and Laplacian of Gaussian (LoG) — from scratch using manual 2D convolution. Both operators are applied to a grayscale image and the results are displayed side-by-side for comparison.

## Topics Covered

- Gaussian kernel construction with configurable size and sigma
- Laplacian kernel (4-connected, second-order derivative approximation)
- Manual 2D convolution with boundary handling
- **DoG**: Original image minus its Gaussian-smoothed version — highlights edges and blobs
- **LoG**: Laplacian applied to the Gaussian-smoothed image — second-derivative edge detector
- Normalization to uint8 for visualization

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
| Q1 | Compute DoG (Original − Gaussian); compute LoG (Laplacian of Gaussian smoothed image); display all three side-by-side |
