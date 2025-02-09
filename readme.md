# Question

1. Subset the clear water and rock portion with the dimension of (18x18).
2. Print the DN values from the subset image.
3. Degrade image with addition of noise .
4. Apply restoration method to restore image using suitable filtering techniques.
---
## Dependencies

- NumPy (`numpy`)
- Matplotlib (`matplotlib`)
- OpenCV (`cv2`)

## Code Overview

The code performs the following main operations:

1. Image Loading and Region Extraction
2. Noise Addition
3. Image Restoration
4. Visualization

### Detailed Workflow

#### 1. Image Loading and Region Extraction

```python
img = cv2.imread("path_to_image", cv2.IMREAD_GRAYSCALE)
```
- Loads a grayscale image using OpenCV
- Extracts a small region of interest (ROI) from the center of the image
- ROI size is set to 18x18 pixels

The region extraction process:
- Calculates center coordinates of the image
- Defines a subset size (18 pixels)
- Extracts the region using array slicing
- Displays the Digital Number (DN) values of the extracted region

#### 2. Noise Addition

```python
noisy_img = img + np.random.normal(loc=0, scale=25, size=img.shape)
```
- Adds Gaussian noise to the original image
- Parameters:
  - `loc=0`: Mean of the Gaussian distribution
  - `scale=25`: Standard deviation of the noise
  - `size=img.shape`: Matches the image dimensions
- Values are clipped to valid pixel range (0-255)

#### 3. Image Restoration

```python
restored_img = cv2.medianBlur(noisy_img, 3)
```
- Uses median filtering to remove noise
- Kernel size of 3x3 pixels
- Preserves edges while removing noise

#### 4. Visualization

The code creates a figure with four subplots:
1. Original grayscale image
2. Extracted subset region
3. Image with added noise
4. Restored image after median filtering

## Usage

1. Replace the image path with your desired image:
```python
img = cv2.imread("your_image_path", cv2.IMREAD_GRAYSCALE)
```

2. Adjust the subset size if needed:
```python
subset_size = 18  # Change this value for different ROI sizes
```

3. Modify noise parameters if required:
```python
scale = 25  # Adjust for different noise levels
```

## Output

The code generates a figure with four subplots showing:
- Original image
- Extracted center region
- Noisy version of the image
- Restored version after denoising

## Technical Notes

- The code assumes the input image is readable and has sufficient dimensions for the subset extraction
- Gaussian noise is used to simulate image degradation
- Median filtering is chosen for restoration due to its effectiveness in removing salt-and-pepper noise while preserving edges

## Limitations

- Works only with grayscale images
- Fixed region of interest size
- Basic noise model and restoration technique
- Center-focused region extraction

## Possible Improvements

1. Add support for color images
2. Implement dynamic ROI selection
3. Add more advanced noise models
4. Implement additional restoration techniques
5. Add error handling for image loading and processing
