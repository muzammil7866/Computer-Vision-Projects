# OpenCV Comprehensive Overview

A hands-on Jupyter notebook covering core OpenCV image processing operations — color spaces, geometric transformations, interpolation methods, and dataset loading utilities.

## Notebook

**`openCV Comprehensive Overview.ipynb`**

## Topics Covered

### 1. Color Spaces and Channel Operations
- Reading images and converting between BGR, RGB, and HSV color spaces using `cv2.cvtColor`
- Splitting images into individual channels (`cv2.split`) and merging them back (`cv2.merge`)
- Visualizing R, G, B and H, S, V channels separately

### 2. Image Resizing and Interpolation
Resizing images in both RGB and HSV spaces using four interpolation methods:
- `cv2.INTER_NEAREST` — nearest-neighbor, fastest but blocky
- `cv2.INTER_LINEAR` — bilinear, good general-purpose default
- `cv2.INTER_CUBIC` — bicubic, sharper at the cost of compute
- `cv2.INTER_LANCZOS4` — highest quality, best for downscaling

### 3. Geometric Transformations
Applying affine and perspective transformations using `cv2.warpAffine` and `cv2.warpPerspective`:
- **Rotation** — `cv2.getRotationMatrix2D` with configurable angle and scale
- **Translation** — shifting images along x/y axes
- **Scaling** — shrinking and enlarging with `cv2.resize`
- **Shearing** — horizontal and vertical shear via custom transformation matrices
- **Reflection** — flipping horizontally and vertically using `cv2.flip` and perspective matrices
- **Cropping** — extracting ROIs via NumPy array slicing

### 4. Dataset Loading Utility
- Loading labelled image datasets from a directory structure using `cv2.imread` and `tqdm`
- Splitting into train/test sets with `sklearn.model_selection.train_test_split`

## Requirements

```bash
pip install opencv-python numpy matplotlib scikit-learn tqdm
```

## Usage

Open the notebook in Jupyter and run cells sequentially. Cells expect a `test.jpg` file in the same directory as the notebook.

```bash
jupyter notebook "openCV Comprehensive Overview.ipynb"
```
