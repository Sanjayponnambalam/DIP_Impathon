import numpy as np
import matplotlib.pyplot as plt
import cv2

# Load the image
img = cv2.imread("C:\\Users\\sanja\\OneDrive\\Desktop\\Career\\runne\\IMG147.jpg", cv2.IMREAD_GRAYSCALE)

# Define the region of interest (clear water and rock portion)
# Assuming the region is located around the center of the image
center_x, center_y = img.shape[1] // 2, img.shape[0] // 2
subset_size = 18
start_x, start_y = center_x - subset_size // 2, center_y - subset_size // 2
end_x, end_y = start_x + subset_size, start_y + subset_size

# Extract the subset image
subset_img = img[start_y:end_y, start_x:end_x]

# Print the DN values from the subset image
print("DN values from the subset image:")
print(subset_img)

# Add noise to the original image
noisy_img = img + np.random.normal(loc=0, scale=25, size=img.shape)
noisy_img = np.clip(noisy_img, 0, 255).astype(np.uint8)

# Restoration using median filtering
restored_img = cv2.medianBlur(noisy_img, 3)

# Plotting
plt.figure(figsize=(12, 8))

# Original Image
plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Subset Image
plt.subplot(2, 2, 2)
plt.imshow(subset_img, cmap='gray')
plt.title('Subset Image')
plt.axis('off')

# Noisy Image
plt.subplot(2, 2, 3)
plt.imshow(noisy_img, cmap='gray')
plt.title('Noisy Image')
plt.axis('off')

# Restored Image
plt.subplot(2, 2, 4)
plt.imshow(restored_img, cmap='gray')
plt.title('Restored Image')
plt.axis('off')

plt.tight_layout()
plt.show()
