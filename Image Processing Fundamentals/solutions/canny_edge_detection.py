import os
"""
# Question 6 (BONUS)
## 1. Gaussian Smoothing

We first reduce noise so that false edges don’t appear.
## 2. Gradient Magnitude & Direction (Sobel)
## 3. Non-Maximum Suppression

Thins edges → keep only local maxima along gradient direction.
## 4. Double Thresholding + Hysteresis

Classify pixels as strong edges, weak edges, or non-edges.
## 5. Compare with OpenCV’s Canny
### Why do we need two thresholds in Canny instead of one?

One threshold → misses weak edges or includes too much noise.

Two thresholds →

High threshold: keeps only strong edges.

Low threshold: allows weak edges to be kept only if they connect to strong edges.

This ensures balance between noise removal and edge connectivity.

### Why does non-maximum suppression thin edges instead of completely removing them?

It suppresses pixels that are not the local maximum along gradient direction.

Keeps only the strongest response → edges become 1-pixel thin, but not deleted entirely.

### How does hysteresis help in connecting weak edges with strong edges?

Some weak edges are real but faint (like low contrast).

Hysteresis keeps them if they are connected to strong edges.

Prevents breaking of continuous edges and ensures edge connectivity.
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = os.path.join(os.path.dirname(__file__), "..", "assets", "image.jpg")
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
img = img.astype(np.float32) / 255.0

def gaussian_kernel(size=5, sigma=1):
    ax = np.linspace(-(size//2), size//2, size)
    xx, yy = np.meshgrid(ax, ax)
    kernel = np.exp(-(xx**2 + yy**2)/(2*sigma**2))
    return kernel / np.sum(kernel)

def apply_filter(img, kernel):
    k = kernel.shape[0]
    pad = k // 2
    padded = np.pad(img, pad, mode="constant")
    filtered = np.zeros_like(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            region = padded[i:i+k, j:j+k]
            filtered[i,j] = np.sum(region * kernel)
    return filtered

blurred = apply_filter(img, gaussian_kernel(5,1))


sobel_x = np.array([[-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1]], dtype=np.float32)

sobel_y = np.array([[-1, -2, -1],
                    [ 0,  0,  0],
                    [ 1,  2,  1]], dtype=np.float32)

Gx = apply_filter(blurred, sobel_x)
Gy = apply_filter(blurred, sobel_y)

magnitude = np.sqrt(Gx**2 + Gy**2)
magnitude = (magnitude / magnitude.max()) * 255

direction = np.arctan2(Gy, Gx)

print("Magnitude: ", magnitude)
print("Direction: ", direction)


def non_maximum_suppression(mag, dir):
    Z = np.zeros_like(mag)
    angle = dir * 180. / np.pi
    angle[angle < 0] += 180
    for i in range(1, mag.shape[0]-1):
        for j in range(1, mag.shape[1]-1):
            q = 255
            r = 255
            if (0 <= angle[i,j] < 22.5) or (157.5 <= angle[i,j] <= 180):
                q = mag[i, j+1]
                r = mag[i, j-1]
            elif (22.5 <= angle[i,j] < 67.5):
                q = mag[i+1, j-1]
                r = mag[i-1, j+1]
            elif (67.5 <= angle[i,j] < 112.5):
                q = mag[i+1, j]
                r = mag[i-1, j]
            elif (112.5 <= angle[i,j] < 157.5):
                q = mag[i-1, j-1]
                r = mag[i+1, j+1]
            if (mag[i,j] >= q) and (mag[i,j] >= r):
                Z[i,j] = mag[i,j]
            else:
                Z[i,j] = 0
    return Z

nms = non_maximum_suppression(magnitude, direction)


def threshold(img, lowRatio=0.05, highRatio=0.15):
    high = img.max() * highRatio
    low = high * lowRatio
    res = np.zeros_like(img)
    strong = 255
    weak = 75
    strong_i, strong_j = np.where(img >= high)
    weak_i, weak_j = np.where((img <= high) & (img >= low))
    res[strong_i, strong_j] = strong
    res[weak_i, weak_j] = weak
    return res, weak, strong

def hysteresis(img, weak, strong=255):
    for i in range(1, img.shape[0]-1):
        for j in range(1, img.shape[1]-1):
            if img[i,j] == weak:
                if ((img[i+1, j-1] == strong) or (img[i+1, j] == strong) or 
                    (img[i+1, j+1] == strong) or (img[i, j-1] == strong) or 
                    (img[i, j+1] == strong) or (img[i-1, j-1] == strong) or 
                    (img[i-1, j] == strong) or (img[i-1, j+1] == strong)):
                    img[i,j] = strong
                else:
                    img[i,j] = 0
    return img

dt, weak, strong = threshold(nms)
canny_manual = hysteresis(dt, weak, strong)


canny_cv = cv2.Canny((img*255).astype(np.uint8), 100, 200)

plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.title("Manual Canny")
plt.imshow(canny_manual, cmap="gray")
plt.axis("off")

plt.subplot(1,2,2)
plt.title("OpenCV Canny")
plt.imshow(canny_cv, cmap="gray")
plt.axis("off")

plt.show()
