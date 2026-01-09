import os
"""
# Question 3
## Q4: Why can noise produce false edges in gradient computation?

Noise introduces sudden pixel intensity changes.

Since gradients rely on differences between neighbors, noise creates sharp changes → interpreted as edges (false positives).

## Q5 Comparison: Finite Difference vs. Sobel for Edge Localization

The finite difference method simply subtracts adjacent pixel values. While this captures sudden changes in intensity, it is:

Very sensitive to noise (even small pixel fluctuations look like edges).

Provides edges that are thin but unstable.

The Sobel operator uses a 3×3 kernel with weighted coefficients. This has two important effects:

Smoothing effect: The averaging inside the kernel reduces the influence of noise.

Stronger response at real edges: Because it considers more neighboring pixels, it produces clearer and more continuous edge lines.

Therefore, Sobel localizes edges better than the simple finite difference because it balances derivative computation with local smoothing, giving more accurate and stable edges.

## Q6: Compare with OpenCV’s cv2.Sobel

The OpenCV Sobel is optimized and more robust.

Differences:

Finite difference = raw, noisier, weaker edges.

Manual Sobel = improved edges, smoother.

OpenCV Sobel = strongest, most stable edges because of optimized implementation.
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = os.path.join(os.path.dirname(__file__), "..", "assets", "image.jpg")
image = cv2.imread(image_path)

Gx = np.zeros_like(image, dtype=float)
Gy = np.zeros_like(image, dtype=float)

Gx[:, :-1] = image[:, 1:] - image[:, :-1]
Gy[:-1, :] = image[1:, :] - image[:-1, :]

gradient_magnitude = np.sqrt(Gx**2 + Gy**2)
edge_image = (gradient_magnitude / gradient_magnitude.max() * 255).astype(np.uint8)

sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
sobel_magnitude = np.sqrt(sobelx**2 + sobely**2)
sobel_edge = (sobel_magnitude / sobel_magnitude.max() * 255).astype(np.uint8)

opencv_sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0)
opencv_sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1)
opencv_sobel_mag = np.sqrt(opencv_sobelx**2 + opencv_sobely**2)
opencv_sobel_edge = (opencv_sobel_mag / opencv_sobel_mag.max() * 255).astype(np.uint8)

plt.figure(figsize=(15,5))
plt.subplot(1,4,1); plt.imshow(image, cmap='gray'); plt.title('Original'); plt.axis('off')
plt.subplot(1,4,2); plt.imshow(edge_image, cmap='gray'); plt.title('Finite Difference'); plt.axis('off')
plt.subplot(1,4,3); plt.imshow(sobel_edge, cmap='gray'); plt.title('Manual Sobel'); plt.axis('off')
plt.subplot(1,4,4); plt.imshow(opencv_sobel_edge, cmap='gray'); plt.title('OpenCV Sobel'); plt.axis('off')
plt.show()
