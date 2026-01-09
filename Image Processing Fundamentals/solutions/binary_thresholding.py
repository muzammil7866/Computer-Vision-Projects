import os
"""
# Question 1
## If we choose a different threshold for binary conversion:

Lower threshold (e.g., 50):
Many pixels will be greater than 50, so most of them will be converted to white (255).
→ The binary image will look brighter with larger white regions.

Higher threshold (e.g., 200):
Only very bright pixels will be above 200, so most pixels will become black (0).
→ The binary image will look darker with fewer white regions.

Why?
Because thresholding decides which pixels are kept as white vs. black. A lower threshold accepts more pixels as “bright enough,” while a higher threshold is stricter and only allows the brightest pixels to remain white.
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = os.path.join(os.path.dirname(__file__), "..", "assets", "image.jpg")
image = cv2.imread(image_path)
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

R = rgb_image[:, :, 0]
G = rgb_image[:, :, 1]
B = rgb_image[:, :, 2]

gray_image = (0.299 * R + 0.587 * G + 0.114 * B).astype(np.uint8)

threshold = 128
binary_image = np.where(gray_image >= threshold, 255, 0).astype(np.uint8)

plt.figure(figsize=(12,4))

plt.subplot(1,3,1)
plt.imshow(rgb_image)
plt.title('Original RGB')
plt.axis('off')

plt.subplot(1,3,2)
plt.imshow(gray_image, cmap='gray')
plt.title('Grayscale')
plt.axis('off')

plt.subplot(1,3,3)
plt.imshow(binary_image, cmap='gray')
plt.title(f'Binary (Threshold={threshold})')
plt.axis('off')

plt.show()
