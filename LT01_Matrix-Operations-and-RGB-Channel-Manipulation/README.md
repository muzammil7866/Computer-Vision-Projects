# LT01 — Matrix Operations and RGB Channel Manipulation

**Course:** AI4002 — Computer Vision Lab  
**Institution:** National University of Computer and Emerging Sciences, Chiniot-Faisalabad Campus  
**Department:** Artificial Intelligence and Data Science

## Overview

This lab introduces foundational image processing concepts through two tasks: element-wise matrix transformations using conditional arithmetic, and manual decomposition and re-composition of RGB color channels in an image.

## Topics Covered

- 2D matrix traversal with conditional arithmetic (even × 10, odd × 7)
- Loading and displaying images with OpenCV and Matplotlib
- Splitting an image into its R, G, B channels using `cv2.split()`
- Merging channels in a custom order (GBR) using `cv2.merge()`
- Color space conversion with `cv2.cvtColor()`

## Technologies Used

- Python
- OpenCV (`cv2`)
- NumPy
- Matplotlib

## Sample Image

- `unnamed.jpg` — base image used for channel splitting and merging

## Requirements

```
opencv-python
numpy
matplotlib
```

## Tasks

| Question | Description |
|----------|-------------|
| Q1 | Traverse a 2D matrix; multiply even elements by 10 and odd elements by 7; print result |
| Q2 | Split image into R, G, B channels; merge back as G, B, R and display side-by-side |
