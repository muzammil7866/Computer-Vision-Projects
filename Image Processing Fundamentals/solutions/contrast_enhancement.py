import os
"""
# Question 2
## If γ < 1 in power-law transformation, what happens to dark pixels and why?

When γ < 1, dark pixels become brighter.

This happens because raising a small value (like 0.2) to a power less than 1 increases it (0.2^0.5 = 0.45).

As a result, the transformation stretches low-intensity values upward, brightening dark areas while keeping already bright regions almost unchanged.
## Contrast stretching and histogram equalization both improve contrast. How are they conceptually different?

Contrast Stretching:

A linear mapping of the current intensity range to the full [0, 255] range.

It only rescales based on min and max pixel values.

Example: If values are between 50–180, they are stretched to 0–255.

Histogram Equalization:

A non-linear mapping based on the image’s histogram.

Redistributes pixel intensities so the histogram becomes more uniform.

Enhances global contrast, especially when intensities are clustered in a narrow range.
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = os.path.join(os.path.dirname(__file__), "..", "assets", "image.jpg")
image = cv2.imread(image_path)
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
R, G, B = rgb_image[:,:,0], rgb_image[:,:,1], rgb_image[:,:,2]
gray_image = (0.299*R + 0.587*G + 0.114*B).astype(np.uint8)

gamma = 0.5
normalized = gray_image / 255.0
power_law = np.power(normalized, gamma)
power_law_img = np.uint8(power_law * 255)

min_val, max_val = np.min(gray_image), np.max(gray_image)
contrast_stretch = ((gray_image - min_val) / (max_val - min_val) * 255).astype(np.uint8)

hist, bins = np.histogram(gray_image.flatten(), 256, [0,256])
cdf = hist.cumsum()
cdf_normalized = cdf * 255 / cdf[-1]
hist_eq_img = np.interp(gray_image.flatten(), bins[:-1], cdf_normalized).reshape(gray_image.shape).astype(np.uint8)

plt.figure(figsize=(15,6))

plt.subplot(2,4,1); plt.imshow(gray_image, cmap='gray'); plt.title('Original Gray'); plt.axis('off')
plt.subplot(2,4,2); plt.imshow(power_law_img, cmap='gray'); plt.title('Power-law (γ=0.5)'); plt.axis('off')
plt.subplot(2,4,3); plt.imshow(contrast_stretch, cmap='gray'); plt.title('Contrast Stretching'); plt.axis('off')
plt.subplot(2,4,4); plt.imshow(hist_eq_img, cmap='gray'); plt.title('Histogram Equalization'); plt.axis('off')

plt.subplot(2,4,5); plt.hist(gray_image.ravel(),256,[0,256]); plt.title('Original Histogram')
plt.subplot(2,4,6); plt.hist(power_law_img.ravel(),256,[0,256]); plt.title('Power-law Histogram')
plt.subplot(2,4,7); plt.hist(contrast_stretch.ravel(),256,[0,256]); plt.title('Contrast Stretch Histogram')
plt.subplot(2,4,8); plt.hist(hist_eq_img.ravel(),256,[0,256]); plt.title('Hist Equalization Histogram')

plt.tight_layout()
plt.show()
