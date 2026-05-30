# LT03 — Gaussian Filter Kernel Convolution

**Course:** AI4002 — Computer Vision Lab  
**Institution:** National University of Computer and Emerging Sciences, Chiniot-Faisalabad Campus  
**Department:** Artificial Intelligence and Data Science

## Overview

This lab implements a 5×5 Gaussian filter from scratch and applies it to a grayscale image via manual convolution. Two normalization strategies are explored: dividing by a fixed constant (1/25) and dividing by the sum of kernel weights. Results are compared side-by-side against the original image.

## Topics Covered

- Gaussian kernel construction (5×5 with non-uniform weights)
- Manual 2D convolution with zero-padding
- Two normalization methods: fixed-divisor vs. kernel-sum normalization
- Smoothing and noise reduction with Gaussian blur
- Side-by-side visualization of original and filtered images

## Technologies Used

- Python
- OpenCV (`cv2`)
- NumPy
- Matplotlib

## Sample Images

| File | Purpose |
|------|---------|
| `unnamed.jpg` | Primary test image |
| `gaussian_noise_practice_image.jpg` | Practice image with Gaussian noise |

## Requirements

```
opencv-python
numpy
matplotlib
```

## Tasks

| Question | Description |
|----------|-------------|
| Q1 (Code 1) | Convolve a 5×5 Gaussian kernel normalized by 1/25; compare with original |
| Q1 (Code 2) | Convolve the same kernel normalized by its element sum; compare with original |
