# LT07 — Morphological Operations on Binary Images

**Course:** AI4002 — Computer Vision Lab  
**Institution:** National University of Computer and Emerging Sciences, Chiniot-Faisalabad Campus  
**Department:** Artificial Intelligence and Data Science

## Overview

This lab explores six fundamental morphological operations applied to binary images using OpenCV. A structurally justified rectangular structuring element is used, and each operation result is shown side-by-side with the original binary image.

## Topics Covered

- Binary thresholding with `cv2.threshold()`
- Structuring element creation with `cv2.getStructuringElement()`
- **Erosion**: shrinks foreground regions
- **Dilation**: expands foreground regions
- **Opening** (Erosion → Dilation): removes small noise blobs
- **Closing** (Dilation → Erosion): fills small holes within objects
- **Internal Boundary**: foreground minus its erosion
- **External Boundary**: dilation minus foreground

## Technologies Used

- Python
- OpenCV (`cv2`)
- NumPy
- Matplotlib

## Sample Images

| File | Purpose |
|------|---------|
| `blobs.png` | Binary blob image used for all morphological operations |

## Requirements

```
opencv-python
numpy
matplotlib
```

## Tasks

| Question | Description |
|----------|-------------|
| Q1 | Apply Erosion, Dilation, Opening, Closing, Internal Boundary, and External Boundary to `blobs.png`; display each result alongside the original |
