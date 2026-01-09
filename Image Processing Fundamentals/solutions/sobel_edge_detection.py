import os
"""
# Question 5
## Manual Implementation of Sobel Filters
## Edge Magnitude and Direction

Magnitude: Shows how strong an edge is at each pixel.

Direction: Shows the orientation of the edge (horizontal, vertical, diagonal).
## 3. Comparison with Finite Difference (Q3)

### Finite Difference

Uses simple subtraction between neighboring pixels.

Very sensitive to noise.

Detects edges but often produces rough/thin edges.

### Sobel Operator

Uses weighted convolution (more weight on closer pixels, e.g., -2,2).

Reduces effect of noise.

Produces smoother and more continuous edges.

Better edge localization than raw finite difference.


## Observations

Sobel edges look cleaner and more defined compared to finite difference.

Sobel is less sensitive to random noise because of averaging effect.

Finite difference detects more edges (including false ones), while Sobel emphasizes stronger, meaningful edges.
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = os.path.join(os.path.dirname(__file__), "..", "assets", "image.jpg")
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
img = img.astype(np.float32) / 255.0

sobel_x = np.array([[-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1]], dtype=np.float32)

sobel_y = np.array([[-1, -2, -1],
                    [ 0,  0,  0],
                    [ 1,  2,  1]], dtype=np.float32)

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

Gx = apply_filter(img, sobel_x)
Gy = apply_filter(img, sobel_y)

magnitude = np.sqrt(Gx**2 + Gy**2)
magnitude = (magnitude / magnitude.max()) * 255
direction = np.arctan2(Gy, Gx)

plt.figure(figsize=(12,6))
plt.subplot(1,3,1); plt.title("Sobel Gx"); plt.imshow(Gx, cmap="gray"); plt.axis("off")
plt.subplot(1,3,2); plt.title("Sobel Gy"); plt.imshow(Gy, cmap="gray"); plt.axis("off")
plt.subplot(1,3,3); plt.title("Magnitude"); plt.imshow(magnitude, cmap="gray"); plt.axis("off")
plt.show()
