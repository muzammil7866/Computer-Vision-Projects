import os
"""
# Question 4
## 1. Add Gaussian Noise
## 2a. Manual Mean Filter Implementation

## 2b. Manual Guassian Filter Implementation
## 3. Which filter is better and why?

Gaussian filter is better because it gives more weight to center pixels, preserving edges while still removing noise.

Mean filter blurs edges more since it averages all pixels equally.

## 4. Why does a larger filter (5×5 vs 3×3) remove more noise but blur edges more?

A larger kernel considers more neighbors, smoothing stronger → more noise reduction.

But edges are also high-frequency features → they get blurred as well.

## 5. Why does Gaussian filtering preserve edges better than mean filtering?

Gaussian gives higher weight to center pixels → nearby pixels influence more.

Mean filter treats all neighbors equally → strong blurring of edges.

## 6. In which situations is mean filtering preferable?

When noise is very strong and random (e.g., salt-and-pepper), mean filtering can smooth aggressively.

It is also simpler and faster → good for real-time, low-power systems.

## 7. Why does Sobel operator use larger weights for center pixels (-2, 2) compared to corners (-1, 1)?

Center pixels represent the main intensity change direction.

Larger weights make the operator more sensitive to edges while reducing noise influence from far pixels.
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = os.path.join(os.path.dirname(__file__), "..", "assets", "image.jpg")
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
img_norm = img / 255.0

mean = 0
var = 0.01
sigma = np.sqrt(var)

gaussian_noise = np.random.normal(mean, sigma, img_norm.shape)
noisy_img = img_norm + gaussian_noise
noisy_img = np.clip(noisy_img, 0, 1)

plt.figure(figsize=(10,5))
plt.subplot(1,2,1); plt.title("Original"); plt.imshow(img, cmap="gray"); plt.axis("off")
plt.subplot(1,2,2); plt.title("Noisy"); plt.imshow(noisy_img, cmap="gray"); plt.axis("off")
plt.show()


import numpy as np
import matplotlib.pyplot as plt

def mean_filter(img, ksize=3):
    pad = ksize // 2
    padded = np.pad(img, pad, mode="constant")
    filtered = np.zeros_like(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            region = padded[i:i+ksize, j:j+ksize]
            filtered[i,j] = np.mean(region)
    return filtered

mean_3 = mean_filter(noisy_img, 3)
mean_5 = mean_filter(noisy_img, 5)

plt.figure(figsize=(12,4))
plt.subplot(1,2,1); plt.title("Mean 3x3"); plt.imshow(mean_3, cmap="gray"); plt.axis("off")
plt.subplot(1,2,2); plt.title("Mean 5x5"); plt.imshow(mean_5, cmap="gray"); plt.axis("off")
plt.show()


import numpy as np
import matplotlib.pyplot as plt

def gaussian_kernel(ksize=3, sigma=1.0):
    ax = np.linspace(-(ksize // 2), ksize // 2, ksize)
    xx, yy = np.meshgrid(ax, ax)
    kernel = np.exp(-(xx**2 + yy**2) / (2 * sigma**2))
    return kernel / np.sum(kernel)

def apply_filter(img, kernel):
    ksize = kernel.shape[0]
    pad = ksize // 2
    padded = np.pad(img, pad, mode="constant")
    filtered = np.zeros_like(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            region = padded[i:i+ksize, j:j+ksize]
            filtered[i, j] = np.sum(region * kernel)
    return filtered

gauss3 = apply_filter(noisy_img, gaussian_kernel(3, 1.0))
gauss5 = apply_filter(noisy_img, gaussian_kernel(5, 1.0))

plt.figure(figsize=(12,4))
plt.subplot(1,2,1); plt.title("Gaussian 3x3"); plt.imshow(gauss3, cmap="gray"); plt.axis("off")
plt.subplot(1,2,2); plt.title("Gaussian 5x5"); plt.imshow(gauss5, cmap="gray"); plt.axis("off")
plt.show()
