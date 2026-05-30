# LT02 — Mean Filter Convolution on Grayscale Images

**Course:** AI4002 — Computer Vision Lab  
**Institution:** National University of Computer and Emerging Sciences, Chiniot-Faisalabad Campus  
**Department:** Artificial Intelligence and Data Science

## Overview

This lab implements a 3×3 average (mean) filter from scratch and applies it to a grayscale image via manual convolution — without using any built-in blur functions. The filtered result is compared side-by-side against the original.

## Topics Covered

- Grayscale image loading and conversion
- Manual 2D convolution loop implementation
- Zero-padding to handle border pixels
- Construction of a uniform 3×3 averaging kernel (`1/9` weights)
- Visual comparison of original vs. filtered images

## Technologies Used

- Python
- OpenCV (`cv2`)
- NumPy
- Matplotlib

## Sample Images

| File | Purpose |
|------|---------|
| `unnamed.jpg` | Primary test image |
| `salt_n_pepper_practice_image_1.jpeg` | Practice image with salt-and-pepper noise |
| `salt_n_pepper_practice_image_2.jpeg` | Second practice image with salt-and-pepper noise |
| `bottles.jpg` | Additional practice image |

## Requirements

```
opencv-python
numpy
matplotlib
```

## Tasks

| Question | Description |
|----------|-------------|
| Q1 | Build a 3×3 average filter kernel; manually convolve with a grayscale image; display original and filtered side-by-side |
