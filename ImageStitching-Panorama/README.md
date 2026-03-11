# Image Stitching - Panorama Creation

Advanced computer vision pipeline for creating panoramic images by stitching multiple overlapping photographs using SIFT features and homography estimation.

## Overview

This project implements the complete image stitching pipeline, a classical computer vision technique used in panorama creation. It combines feature detection, matching, geometric alignment, and image warping to create seamless panoramic images.

## Algorithm Pipeline

1. **SIFT Detection & Description**: Extract distinctive scale-invariant features from both images
2. **Feature Matching**: Use BFMatcher (Brute Force Matcher) with k-NN to find potential feature correspondences
3. **Lowe's Ratio Test**: Filter ambiguous matches to retain only high-quality correspondences
4. **Homography Estimation**: Use RANSAC (Random Sample Consensus) to compute the geometric transformation
5. **Image Warping**: Warp and blend images to create seamless panorama

## Features

- Scale-Invariant Feature Transform (SIFT) for robust matching
- RANSAC for robust homography estimation
- Perspective transformation and image warping
- Proper handling of image blending
- Well-commented code for educational purposes

## Implementation Details

- **SIFT Detector**: Detects distinctive keypoints and 128-D descriptors
- **BFMatcher**: Brute-force matching with k=2 for ratio test
- **Lowe's Ratio Test**: Typically uses 0.7 threshold to filter ambiguous matches
- **RANSAC Homography**: Robust estimation resistant to outliers
- **OpenCV Warpaffine/Perspective**: Warps image to align with panorama

## Usage

Provide two overlapping images and run the notebook to:
1. Extract and match features
2. Compute homography transformation
3. Warp and blend images
4. Display resulting panorama

## Requirements

- OpenCV (cv2)
- NumPy
- Matplotlib (visualization)

## Notes

- Works best with images that have significant overlap
- Image order matters (left-to-right or right-to-left)
- SIFT may require additional OpenCV contrib modules
- Can be extended to multi-image panoramas

## Educational Value

Demonstrates:
- Feature detection and description
- Geometric alignment and transformation
- Robust estimation under outliers (RANSAC)
- Classical computer vision pipeline design
