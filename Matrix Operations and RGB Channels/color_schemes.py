import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread("image.jpg")

# Convert BGR (OpenCV default) to RGB for display
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Split into channels (BGR order in OpenCV)
b, g, r = cv2.split(image)

# Merge channels in GBR order
gbr_image = cv2.merge([g, b, r])

# Convert GBR to RGB for proper display in matplotlib
gbr_rgb = cv2.cvtColor(gbr_image, cv2.COLOR_BGR2RGB)

# Show both images side by side
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image_rgb)
plt.title("Original Image (RGB)")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(gbr_rgb)
plt.title("GBR Image")
plt.axis("off")

plt.show()
