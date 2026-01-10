import cv2
import matplotlib.pyplot as plt

def main():
    # Load the image
    img = cv2.imread('wheel.png', cv2.IMREAD_GRAYSCALE)
    
    if img is None:
        print("Error: 'wheel.png' not found. Please ensure the image is in the same directory.")
        return

    # Apply Scharr Edge Detection
    # Scharr is essentially a specific variation of Sobel with better rotational symmetry
    scharr_x = cv2.Scharr(img, cv2.CV_64F, 1, 0)
    scharr_y = cv2.Scharr(img, cv2.CV_64F, 0, 1)
    
    scharr_v = cv2.convertScaleAbs(scharr_x)
    scharr_h = cv2.convertScaleAbs(scharr_y)
    
    # Combined
    scharr_hv = cv2.addWeighted(scharr_h, 0.5, scharr_v, 0.5, 0)

    # Plotting
    fig, axs = plt.subplots(1, 4, figsize=(20, 5))
    images = [img, scharr_h, scharr_v, scharr_hv]
    titles = ['Original', 'Scharr Horizontal', 'Scharr Vertical', 'Scharr Combined']

    for ax, im, title in zip(axs, images, titles):
        ax.imshow(im, cmap='gray')
        ax.set_title(title)
        ax.axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
