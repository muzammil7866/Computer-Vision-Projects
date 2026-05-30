# LT09 — Panorama Stitching with SIFT and Homography

**Course:** AI4002 — Computer Vision Lab  
**Institution:** National University of Computer and Emerging Sciences, Chiniot-Faisalabad Campus  
**Department:** Artificial Intelligence and Data Science

## Overview

This lab implements a full image stitching pipeline to create a panoramic image from a sequence of overlapping photographs. The pipeline uses SIFT for feature detection, brute-force matching with Lowe's ratio test for correspondence filtering, and RANSAC-based homography estimation for image warping and blending.

## Topics Covered

- SIFT keypoint detection and 128-dim descriptor computation with `cv2.SIFT_create()`
- Brute-force k-NN feature matching with `cv2.BFMatcher`
- Lowe's ratio test (threshold 0.75) to filter false matches
- Homography matrix estimation with `cv2.findHomography()` using RANSAC
- Perspective warping with `cv2.warpPerspective()`
- Sequential pairwise stitching of four overlapping images into a single panorama

## Technologies Used

- Python
- OpenCV (`cv2`)
- NumPy
- Google Colab (`cv2_imshow`)

## Requirements

```
opencv-python
numpy
```

## Tasks

| Question | Description |
|----------|-------------|
| Q1 | Implement `stitch_images(img1, img2)` using SIFT + BFMatcher + RANSAC homography; chain-stitch four overlapping images into a panorama |
