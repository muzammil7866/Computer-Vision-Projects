import cv2
import matplotlib.pyplot as plt

def main():
    # Load the image
    img = cv2.imread('wheel.png', cv2.IMREAD_GRAYSCALE)
    
    if img is None:
        print("Error: 'wheel.png' not found. Please ensure the image is in the same directory.")
        return

    # Apply Canny Edge Detection
    # Thresholds 100 and 200 are common starting points, but can be tuned
    canny = cv2.Canny(img, 100, 200)

    # Plotting
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    images = [img, canny]
    titles = ['Original', 'Canny Edge Detection']

    for ax, im, title in zip(axs, images, titles):
        ax.imshow(im, cmap='gray')
        ax.set_title(title)
        ax.axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
