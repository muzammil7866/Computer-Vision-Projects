import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    # Load the image
    img = cv2.imread('wheel.png', cv2.IMREAD_GRAYSCALE)
    
    if img is None:
        print("Error: 'wheel.png' not found. Please ensure the image is in the same directory.")
        return

    # Prewitt Kernels
    prewitt_x = np.array([[-1, 0, 1],
                          [-1, 0, 1],
                          [-1, 0, 1]], dtype=np.float32)
                          
    prewitt_y = np.array([[1, 1, 1],
                          [0, 0, 0],
                          [-1, -1, -1]], dtype=np.float32)

    # Apply Kernels
    prewitt_v = cv2.convertScaleAbs(cv2.filter2D(img, cv2.CV_64F, prewitt_x))
    prewitt_h = cv2.convertScaleAbs(cv2.filter2D(img, cv2.CV_64F, prewitt_y))
    
    # Combined (Optional, but good for visualization)
    prewitt_hv = cv2.addWeighted(prewitt_h, 0.5, prewitt_v, 0.5, 0)

    # Plotting
    fig, axs = plt.subplots(1, 4, figsize=(20, 5))
    images = [img, prewitt_h, prewitt_v, prewitt_hv]
    titles = ['Original', 'Prewitt Horizontal', 'Prewitt Vertical', 'Prewitt Combined']

    for ax, im, title in zip(axs, images, titles):
        ax.imshow(im, cmap='gray')
        ax.set_title(title)
        ax.axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
