import cv2
import matplotlib.pyplot as plt

def main():
    # Load the image
    img = cv2.imread('wheel.png', cv2.IMREAD_GRAYSCALE)
    
    if img is None:
        print("Error: 'wheel.png' not found. Please ensure the image is in the same directory.")
        return

    # Apply Sobel Edge Detection
    sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    
    sobel_v = cv2.convertScaleAbs(sobel_x)
    sobel_h = cv2.convertScaleAbs(sobel_y)
    
    # Combined Horizontal and Vertical
    sobel_hv = cv2.addWeighted(sobel_h, 0.5, sobel_v, 0.5, 0)

    # Plotting
    fig, axs = plt.subplots(1, 4, figsize=(20, 5))
    images = [img, sobel_h, sobel_v, sobel_hv]
    titles = ['Original', 'Sobel Horizontal', 'Sobel Vertical', 'Sobel Combined']

    for ax, im, title in zip(axs, images, titles):
        ax.imshow(im, cmap='gray')
        ax.set_title(title)
        ax.axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
