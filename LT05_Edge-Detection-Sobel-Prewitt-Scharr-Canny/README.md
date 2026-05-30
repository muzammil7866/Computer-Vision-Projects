# LT05 — Edge Detection: Sobel, Prewitt, Scharr, and Canny

**Course:** AI4002 — Computer Vision Lab  
**Institution:** National University of Computer and Emerging Sciences, Chiniot-Faisalabad Campus  
**Department:** Artificial Intelligence and Data Science

## Overview

This lab implements and compares four classical edge detection techniques on a grayscale image. Each method is applied both horizontally and vertically (where applicable), and all results are displayed in a unified side-by-side grid for visual comparison.

## Topics Covered

- **Sobel filter**: Horizontal, Vertical, and combined (H+V) using `cv2.Sobel()`
- **Prewitt filter**: Horizontal and Vertical via manual kernel + `cv2.filter2D()`
- **Scharr filter**: Horizontal and Vertical using `cv2.Scharr()` (higher-accuracy Sobel alternative)
- **Canny edge detector**: Multi-stage detector with Gaussian smoothing + hysteresis thresholding
- Absolute scale conversion with `cv2.convertScaleAbs()` and `cv2.addWeighted()`

## Technologies Used

- Python
- OpenCV (`cv2`)
- NumPy
- Matplotlib

## Sample Images

| File | Purpose |
|------|---------|
| `wirebond.tif` | Classic industrial edge detection test image (wirebond semiconductor) |

## Requirements

```
opencv-python
numpy
matplotlib
```

## Tasks

| Question | Description |
|----------|-------------|
| Q1 | Apply Sobel (H, V, H+V), Prewitt (H, V), Scharr (H, V), and Canny to a grayscale image; display all results in a grid |
